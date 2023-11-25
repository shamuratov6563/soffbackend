from rest_framework import serializers
from . import models
from datetime import  datetime

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Tag
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Author
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = "__all__"


class AdvantageListSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)


    class Meta:
        model = models.Advantage
        exclude = ("body", )

class AdventageDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Advantage
        fields = ("title",
                  "body",
                  )

class ArticleListSerializer(serializers.ModelSerializer):
    diff = serializers.SerializerMethodField(method_name="difference")
    tags = TagSerializer()
    category = CategorySerializer()
    author = AuthorSerializer()

    def difference(self, obj):
        result = obj.created_at
        r  = datetime.now().date() - result
        return r

    class Meta:

        model = models.Article
        fields = (
            "id",
            "poster",
            "title",
            "category",
            "tags",
            "created_at",
            "author",
            "diff", 
        )


class ArticleDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = models.Article
        fields = ("body",
                  "author",
                  )



class CourseListSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Course
        fields = "__all__"


class CourseDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Course
        fields = ("name",
                  "body",)


class ApplicationCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.ApplicationForm
        fields = "__all__"


class CategoryWithCountSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()

    def get_count(self, obj):
        return models.Article.objects.filter(category=obj).count()

    class Meta:
        model = models.Category
        fields = ("id", "name", "count")


class Way2JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Way2Job
        fields = "__all__"


class GallerySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Gallery
        fields = "__all__"