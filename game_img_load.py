import os
import django
import requests
import urllib.parse
from django.conf import settings
from review_site.models.py import Game  

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'board_game_chronicle.settings')
django.setup()

def download_images():
    # Query your model to get instances with image URLs
    games = Game.objects.filter(image__isnull=False).exclude(image='')

    # Define a directory to store downloaded images
    image_dir = os.path.join(settings.BASE_DIR, 'static/css/media/images')  
    os.makedirs(image_dir, exist_ok=True)

    # Iterate through games and download images
    for game in games:
        image_url = game.image
        # Use urllib.parse.quote to safely encode the game name
        image_name = urllib.parse.quote(f"{game.game_name}.jpg", safe='')

        try:
            response = requests.get(image_url, stream=True)
            if response.status_code == 200:
                # Save the image to the local directory
                image_path = os.path.join(image_dir, image_name)
                with open(image_path, 'wb') as f:
                    for chunk in response.iter_content(1024):
                        f.write(chunk)
                print(f"Downloaded {image_name}")

                # Update the local_image_path in the Game model
                game.local_image_path = image_path
                game.save()
            else:
                print(f"Failed to download {image_url}")
        except Exception as e:
            print(f"Error downloading {image_url}: {e}")

if __name__ == "__main__":
    download_images()