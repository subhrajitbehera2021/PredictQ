from django.core.management.base import (
    BaseCommand
)

from apps.users.models import User

from shared.enums import UserRole


class Command(BaseCommand):

    help = "Create Super Admin"

    def handle(self, *args, **kwargs):

        username = input("Username: ")

        email = input("Email: ")

        password = input("Password: ")

        if User.objects.filter(
            username=username
        ).exists():

            self.stdout.write(
                self.style.ERROR(
                    "User already exists"
                )
            )

            return

        User.objects.create_superuser(
            username=username,
            email=email,
            password=password,
            role=UserRole.SUPER_ADMIN
        )

        self.stdout.write(
            self.style.SUCCESS(
                "Super Admin Created"
            )
        )