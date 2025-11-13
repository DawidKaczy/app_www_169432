from posts.models import Category, Post, Topic
from posts.serializers import CategorySerializer, PostSerializer
from rest_framework.renderers import JSONRenderer
from django.contrib.auth.models import User
from django.utils.text import slugify
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io

user, created = User.objects.get_or_create(username="admin")

category, _ = Category.objects.get_or_create(name="Python")
topic, _ = Topic.objects.get_or_create(name="Django REST Framework", category=category)

post, _ = Post.objects.get_or_create(
    title="Pierwszy post",
    text="To jest przykładowy post",
    topic=topic,
    slug=slugify("Pierwszy post"),
    created_by=user
)


serializer_post = PostSerializer(post)
print("Serializacja Post -> Python dict:")
print(serializer_post.data)

post_json = JSONRenderer().render(serializer_post.data)
print("Serializacja Post -> JSON:")
print(post_json)


category = Category(name='Kasia')
serializer = CategorySerializer(category)
serializer.data
print(serializer)

content = JSONRenderer().render(serializer.data)
print(content)

stream = io.BytesIO(content)
data = JSONParser().parse(stream)

deserializer = PostSerializer(data=data)
print(deserializer.is_valid())
print(deserializer.validated_data)