from rest_framework import serializers
from .models import Category, Topic, Post
import re

class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=150)
    text = serializers.CharField()
    topic = serializers.PrimaryKeyRelatedField(queryset=Topic.objects.all())
    slug = serializers.SlugField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    created_by = serializers.PrimaryKeyRelatedField(read_only=True)

    def validate_title(self, value):
        if not re.match(r'^[A-Za-zÀ-Żà-ż\s]+$', value):
            raise serializers.ValidationError('Tytuł może zawierać tylko litery i spacje.')
        return value

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.save()
        return instance

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=60)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class TopicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=60)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    created = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Topic.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance