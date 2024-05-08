# extract_game_names.py

import json
from django.core.management.base import BaseCommand
from core.models import Games  # Replace 'myapp' with the name of your Django app

class Command(BaseCommand):
    help = 'Extracts names of games from the database and saves them in a JSON file'

    def handle(self, *args, **options):
        # Query the Games model to retrieve names of games
        game_names = Games.objects.values_list('name', flat=True)

        # Convert the queryset to a list
        game_names_list = list(game_names)

        # Define the output JSON file path
        output_file = 'game_names.json'

        # Write the game names to the JSON file
        with open(output_file, 'w') as json_file:
            json.dump(game_names_list, json_file)

        self.stdout.write(self.style.SUCCESS(f'Successfully extracted game names to {output_file}'))
