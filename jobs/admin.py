from django.contrib import admin
from .models import Category, Job, Application

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("title", "company", "location", "category", "job_type", "is_active", "created_at")
    list_filter = ("category", "job_type", "is_active")
    search_fields = ("title", "company", "location")

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("job", "user", "status", "created_at")
    list_filter = ("status",)
    search_fields = ("job__title", "user__username")
