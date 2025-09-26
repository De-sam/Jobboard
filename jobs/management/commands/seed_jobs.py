import random
from django.core.management.base import BaseCommand
from jobs.models import Category, Job

class Command(BaseCommand):
    help = "Seed the database with categories and sample jobs"

    def handle(self, *args, **kwargs):
        categories = [
            "Engineering",
            "Design",
            "Marketing",
            "Sales",
            "Human Resources",
            "Finance",
            "Operations",
            "Customer Support",
            "IT",
            "Product Management",
        ]

        job_titles = [
            "Backend Engineer",
            "Frontend Developer",
            "UI/UX Designer",
            "Marketing Specialist",
            "Sales Associate",
            "HR Coordinator",
            "Financial Analyst",
            "Operations Manager",
            "Customer Support Agent",
            "Product Owner",
        ]

        companies = [
            "Acme Corp",
            "Techify",
            "DesignHub",
            "Marketify",
            "SalesForceX",
            "PeopleOps",
            "FinSolve",
            "OpsMasters",
            "HelpDeskPro",
            "ProdFlow",
        ]

        locations = [
            "Lagos",
            "Abuja",
            "Port Harcourt",
            "Remote",
            "London",
            "New York",
            "Berlin",
            "Toronto",
            "Nairobi",
            "Cape Town",
        ]

        job_types = ["full_time", "part_time", "contract", "internship", "remote"]

        # Seed categories
        category_objs = []
        for cat in categories:
            obj, _ = Category.objects.get_or_create(name=cat, slug=cat.lower().replace(" ", "-"))
            category_objs.append(obj)

        self.stdout.write(self.style.SUCCESS(f"Seeded {len(category_objs)} categories."))

        # Seed 50 jobs
        for i in range(50):
            Job.objects.create(
                title=random.choice(job_titles),
                description=f"This is a sample job description for job {i+1}.",
                company=random.choice(companies),
                location=random.choice(locations),
                job_type=random.choice(job_types),
                category=random.choice(category_objs),
                is_active=True,
            )

        self.stdout.write(self.style.SUCCESS("Successfully seeded 50 jobs."))
