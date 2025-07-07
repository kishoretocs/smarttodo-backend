from rest_framework.decorators import api_view
from rest_framework.response import Response
from ai.processor import generate_task_suggestion
from context.models import ContextEntry

@api_view(['POST'])
def ai_task_suggestions(request):
    task_data = request.data.get("task")
    if not task_data:
        return Response({"error": "Missing task data"}, status=400)

    # Get latest context entries (limit to 5 recent entries)
    context_entries = ContextEntry.objects.order_by('-timestamp')[:5]
    context_text = "\n".join([entry.content for entry in context_entries])

    ai_result = generate_task_suggestion(task_data, context_text)
    return Response(ai_result)
