from django.http.request import HttpRequest
from .models import *
from django.contrib import admin

@admin.register(Advantage)
class AdventageAdmin(admin.ModelAdmin):
    list_display = ("id", "title", )
    list_display_links = ("id", "title")
    search_fields = ("title", )

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "name", )
    list_display_links = ("id", "name")
    search_fields = ("name", )
    list_filter = ("id", )

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "created_at", "author")
    list_display_links = ("id", "title", "category")
    search_fields = ("title", "category")
    list_filter = ("category", "created_at", "author")

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "name", )
    list_display_links = ("id", "name")

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", )
    list_display_links = ("id", "full_name")
    search_fields = ("full_name", )


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", )
    list_display_links = ("id", "title")
    search_fields = ("title", )


@admin.register(Way2Job)
class Way2JobAdmin(admin.ModelAdmin):
    list_display = ("id", "title", )
    list_display_links = ("id", "title")
    search_fields = ("title", )

    def has_add_permission(self, request: HttpRequest) -> bool:
        if Way2Job.objects.exists():
            return False
        return True


@admin.register(ApplicationForm)
class ApplicationFormAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "phone_number", )
    list_display_links = ("id", "full_name")
    search_fields = ("title", )


@admin.register(Category)
class CategorymAdmin(admin.ModelAdmin):
    list_display = ("id", "name" )
    list_display_links = ("id", "name")
    search_fields = ("name", )
