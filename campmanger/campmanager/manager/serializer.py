from rest_framework.serializers import ModelSerializer
from manager.models import subscriber

class unsubscriber_serializer(ModelSerializer):
    class Meta:
        model = subscriber
        fields = "__all__"
