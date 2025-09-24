from rest_framework import serializers
from django.utils.text import slugify
from .models import Category, Job, Application

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "slug"]
        read_only_fields = ["id", "slug"]

    def create(self, validated_data):
        name = validated_data["name"]
        validated_data["slug"] = slugify(name)
        return super().create(validated_data)


class JobSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source="category", write_only=True
    )

    class Meta:
        model = Job
        fields = [
            "id", "title", "description", "company", "location", "job_type",
            "category", "category_id", "is_active", "created_at", "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at", "category"]


class ApplicationSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Application
        fields = ["id", "job", "user", "cover_letter", "resume_url", "status", "created_at"]
        read_only_fields = ["id", "user", "status", "created_at"]

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)
