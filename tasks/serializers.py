from rest_framework import serializers
from .models import Task, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), write_only=True, source='category',required=False
    )

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'category', 'category_id', 'priority_score', 'deadline', 'status', 'created_at', 'updated_at']
