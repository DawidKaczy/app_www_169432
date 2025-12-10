import graphene
from graphene_django import DjangoObjectType
from posts.models import Category, Topic, Post
from django.contrib.auth import get_user_model

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name")


class TopicType(DjangoObjectType):
    class Meta:
        model = Topic
        fields = ("id", "name", "category", "created")


class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "text",
            "topic",
            "slug",
            "created_at",
            "updated_at",
            "created_by",
        )


class Query(graphene.ObjectType):

    all_categories = graphene.List(CategoryType)
    all_topics = graphene.List(TopicType)
    all_posts = graphene.List(PostType)

    posts_by_title_phrase = graphene.List(PostType, phrase=graphene.String(required=True))
    count_posts_by_user = graphene.Int(user_id=graphene.Int(required=True))
    topics_by_category_name = graphene.List(TopicType, name=graphene.String(required=True))


    def resolve_all_categories(root, info):
        return Category.objects.all()

    def resolve_all_topics(root, info):
        return Topic.objects.select_related("category").all()

    def resolve_all_posts(root, info):
        return Post.objects.select_related("topic", "created_by").all()

    # 1. Filtr po fragmencie tytułu
    def resolve_posts_by_title_phrase(root, info, phrase):
        return Post.objects.filter(title__icontains=phrase)

    # 2. Liczba postów danego użytkownika
    def resolve_count_posts_by_user(root, info, user_id):
        return Post.objects.filter(created_by_id=user_id).count()

    # 3. Topic-i po nazwie kategorii
    def resolve_topics_by_category_name(root, info, name):
        return Topic.objects.filter(category__name__icontains=name)


class CreatePost(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        text = graphene.String(required=True)
        topic_id = graphene.Int(required=True)
        slug = graphene.String(required=True)

    post = graphene.Field(PostType)

    def mutate(self, info, title, text, topic_id, slug):
        user = info.context.user
        if user.is_anonymous:
            raise Exception("Musisz być zalogowany.")

        topic = Topic.objects.get(pk=topic_id)
        post = Post.objects.create(
            title=title,
            text=text,
            topic=topic,
            slug=slug,
            created_by=user
        )
        return CreatePost(post=post)


class UpdatePost(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        title = graphene.String()
        text = graphene.String()
        slug = graphene.String()

    post = graphene.Field(PostType)

    def mutate(self, info, id, **kwargs):
        user = info.context.user
        if user.is_anonymous:
            raise Exception("Musisz być zalogowany.")

        post = Post.objects.get(pk=id)

        # Kontrola autora
        if post.created_by != user:
            raise Exception("Nie możesz edytować cudzego posta.")

        for field, value in kwargs.items():
            setattr(post, field, value)

        post.save()
        return UpdatePost(post=post)


class DeletePost(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    ok = graphene.Boolean()

    def mutate(self, info, id):
        user = info.context.user
        if user.is_anonymous:
            raise Exception("Musisz być zalogowany.")

        post = Post.objects.get(pk=id)

        if post.created_by != user:
            raise Exception("Nie możesz usuwać cudzego posta.")

        post.delete()
        return DeletePost(ok=True)


class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()
    update_post = UpdatePost.Field()
    delete_post = DeletePost.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
