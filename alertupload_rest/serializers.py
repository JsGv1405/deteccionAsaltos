from rest_framework import serializers
from app.models import UploadAlert

# Serializer for UploadAlert Model
class UploadAlertSerializer(serializers.ModelSerializer):

    class Meta:
        model = UploadAlert
        fields = ('pk', 'image', 'user_ID', 'location', 'date_created', 'alert_receiver')