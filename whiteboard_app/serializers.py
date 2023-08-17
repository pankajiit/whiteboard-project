from rest_framework import serializers
from .models import Whiteboard, DrawingAction

class WhiteboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Whiteboard
        fields = '__all__'

class DrawingActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrawingAction
        fields = '__all__'
