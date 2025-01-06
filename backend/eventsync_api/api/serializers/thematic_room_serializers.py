from rest_framework import serializers
from core.models import ThematicRoom


class ThematicRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThematicRoom
        fields = "__all__"
