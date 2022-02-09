from rest_framework import serializers
from todos.models import Todo


class TodoSerializer(serializers.ModelSerializer):

    created = serializers.ReadOnlyField()
    updated = serializers.ReadOnlyField()

    class Meta:
        model = Todo
        fields = (
            "id",
            "name",
            "description",
            "created",
            "updated",
            "status",
        )
