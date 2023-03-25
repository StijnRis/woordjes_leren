'''
To start:
Set-ExecutionPolicy Unrestricted -Scope Process
d:/Programmeren/Websites/woordjes_leren/venv/Scripts/Activate.ps1
python manage.py runserver

Shell:
python manage.py shell
'''

#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


# python manage.py shell
'''
from quiz.models import List, Question
List.objects.all()
'''

# Where we left:
# https://docs.djangoproject.com/en/4.1/intro/tutorial04/
