import io
from django.core.management.base import BaseCommand
from quiz.serializers import WordlistSerializer
'''
python back_end/manage.py test
'''


class Command(BaseCommand):
    help = "Testing"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        data = {
            "name": "Test123",
            "visibility": "pl",
            "materials": [
                {
                    "translation": {
                        "from_word": {
                            "name": "lopen",
                            "language": {
                                "name": "Nederlands"
                            }
                        },
                        "to_word": {
                            "name": "to walk",
                            "language": {
                                "name": "English"
                            }
                        }
                    }
                },
                {
                    "translation": {
                        "from_word": {
                            "name": "spring",
                            "language": {
                                "name": "Nederlands"
                            }
                        },
                        "to_word": {
                            "name": "to jump",
                            "language": {
                                "name": "English"
                            }
                        }
                    }
                }
            ]
        }
        serializer = WordlistSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        user_serializer = WordlistSerializer(instance=user)
        print(user_serializer.data)
