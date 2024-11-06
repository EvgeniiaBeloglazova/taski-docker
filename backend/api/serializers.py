"""This class is responsible for managing the API."""

from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """This class is responsible for managing the API."""

    class Meta:
        """This class is responsible for managing the API."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
