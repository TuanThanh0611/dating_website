from django.core.management.commands.runserver import Command as RunserverCommand

from django.core.management.commands.runserver import Command as RunserverCommand

class Command(RunserverCommand):
    runserver = "8001"  # Chỉnh cổng mặc định ở đây