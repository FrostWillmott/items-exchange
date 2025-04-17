from rest_framework import serializers
from .models import Ad, ExchangeProposal

class AdSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    image_url = serializers.URLField(required=False, allow_blank=True)

    class Meta:
        model = Ad
        fields = [
            'id', 'user', 'title', 'description',
            'image_url', 'category', 'condition',
            'created_at'
        ]
        read_only_fields = ['id', 'created_at']


class ExchangeProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeProposal
        fields = [
            'id', 'ad_sender', 'ad_receiver',
            'comment', 'status', 'created_at'
        ]
        # status is writable to allow receiver to accept/reject
        read_only_fields = ['id', 'created_at']