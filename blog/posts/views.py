from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category, Topic, Post
from .serializers import CategorySerializer, TopicSerializer, PostSerializer



# 🔹 CATEGORY
class CategoryList(APIView):
    def get(self, request):
        search = request.query_params.get('search')
        categories = Category.objects.all()
        if search:
            categories = categories.filter(name__icontains=search)
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetail(APIView):
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return None

    def get(self, request, pk):
        category = self.get_object(pk)
        if not category:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def delete(self, request, pk):
        category = self.get_object(pk)
        if not category:
            return Response(status=status.HTTP_404_NOT_FOUND)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 🔹 TOPIC
class TopicList(APIView):
    def get(self, request):
        search = request.query_params.get('search')
        topics = Topic.objects.all()
        if search:
            topics = topics.filter(name__icontains=search)
        serializer = TopicSerializer(topics, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TopicDetail(APIView):
    def get_object(self, pk):
        try:
            return Topic.objects.get(pk=pk)
        except Topic.DoesNotExist:
            return None

    def get(self, request, pk):
        topic = self.get_object(pk)
        if not topic:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TopicSerializer(topic)
        return Response(serializer.data)

    def delete(self, request, pk):
        topic = self.get_object(pk)
        if not topic:
            return Response(status=status.HTTP_404_NOT_FOUND)
        topic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 🔹 POST
class PostsList(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostsDetail(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return None

    def get(self, request, pk):
        post = self.get_object(pk)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def delete(self, request, pk):
        post = self.get_object(pk)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)