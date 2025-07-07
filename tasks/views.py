from rest_framework import viewsets
from .models import Task, Category
from .serializers import TaskSerializer, CategorySerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-priority_score')
    serializer_class = TaskSerializer

    def create(self, request, *args, **kwargs):
        user_input = request.data

        # 1. Get recent context
        context_entries = ContextEntry.objects.order_by('-timestamp')[:5]
        context_text = "\n".join([entry.content for entry in context_entries])

        # 2. Call AI
        ai_result = generate_task_suggestion(user_input, context_text)

        if "error" in ai_result:
            return Response({"error": "AI failed to process task"}, status=500)

        if category := ai_result.get('suggested_category'):
            category_obj, created = Category.objects.get_or_create(name=category)
            category_obj.usage_count += 1
            category_obj.save()
            ai_result['category_id'] = category_obj.id

        # 3. Merge AI-enhanced fields into request
        enhanced_data = {
            "title": user_input.get("title"),
            "description": ai_result.get("enhanced_description") or user_input.get("description"),
            "category": ai_result.get("suggested_category"),
            "priority_score": ai_result.get("priority_score"),
            "deadline": ai_result.get("suggested_deadline"),
            "tags": ai_result.get("tags", []),
            "status": user_input.get("status", "pending")
        }

        # 4. Serialize and save to DB
        serializer = self.get_serializer(data=enhanced_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('-usage_count')
    serializer_class = CategorySerializer
    http_method_names = ['get', 'post']