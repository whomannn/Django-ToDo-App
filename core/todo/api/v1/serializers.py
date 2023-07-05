from rest_framework import serializers
from todo.models import Task


class taskSerializer(serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ["id", "title", "done", "absolute_url"]

    def get_absolute_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.pk)
