from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    # image_url = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = '__all__'
        # fields = ['id', 'title', 'image', 'likes', 'image_url']

    # def get_image_url(self, obj):
    #     request = self.context.get('request')
    #     if request is not None and obj.image:
    #         return request.build_absolute_uri(obj.image.url)
    #     return None