from rest_framework import serializers
from .models import Book
from django.utils import timezone

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    

    def validate_publication_date(self, value):
        if value > timezone.now().date():
            raise serializers.ValidationError("Publication date cannot be in the future.")
        return value
    
    def partial_update(self, instance, validated_data):
            # Allow partial updates
            instance.title = validated_data.get('title', instance.title)
            instance.author = validated_data.get('author', instance.author)
            instance.publication_date = validated_data.get('publication_date', instance.publication_date)
            # Add any other fields you want to support partial updates for
            instance.save()
            return instance