from rest_framework import serializers
from .models import Listing

class ListingSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()
    is_favorite = serializers.SerializerMethodField()

    class Meta:
        model = Listing
        fields = ['id', 'title', 'description', 'price', 'owner', 'is_favorite']

        def get_is_favorite(self, obj):
            user = self.context['request'].user
            if user.is_authenticated:
                return obj.favorites.filter(id=user.id).exists()
            return False