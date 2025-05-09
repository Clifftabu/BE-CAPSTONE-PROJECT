from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'  # You can also list fields explicitly like ['id', 'title', 'description', 'completed']
