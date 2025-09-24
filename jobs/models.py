from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Job(models.Model):
    class Type(models.TextChoices):
        FULL_TIME = "full_time", "Full-time"
        PART_TIME = "part_time", "Part-time"
        CONTRACT = "contract", "Contract"
        INTERNSHIP = "internship", "Internship"
        REMOTE = "remote", "Remote"

    title = models.CharField(max_length=200)
    description = models.TextField()
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    job_type = models.CharField(max_length=20, choices=Type.choices, default=Type.FULL_TIME)

    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="jobs")
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=["category", "is_active", "created_at"], name="job_cat_active_created_idx"),
            models.Index(fields=["location"], name="job_location_idx"),
            models.Index(fields=["title"], name="job_title_idx"),
        ]
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} @ {self.company}"


class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applications")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applications")
    cover_letter = models.TextField(blank=True)
    resume_url = models.URLField(blank=True)

    status = models.CharField(max_length=20, default="submitted")  # submitted|reviewed|accepted|rejected
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("job", "user")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user} → {self.job}"
