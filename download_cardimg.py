import requests
import os  # Import the os module

# Directory where card images will be stored
image_directory = "E:\IT_stuff\PokemonCardsApp\PokemonCardsApp\Card_img\SWSH08"

# Create the directory if it doesn't exist
os.makedirs(image_directory, exist_ok=True)

# Base URL for the card images
base_url = "https://tcg.pokemon.com/assets/img/expansions/fusion-strike/cards/en-us/SWSH08_EN_NUMBER-2x.jpg"

# Specify the range of card numbers to download
start_card_number = 1
end_card_number = 284

# Download card images
for card_number in range(start_card_number, end_card_number + 1):
    # Generate the URL for the current card number
    card_image_url = base_url.replace("NUMBER", str(card_number))

    # Send an HTTP GET request to download the image
    response = requests.get(card_image_url)

    if response.status_code == 200:
        # Save the image to a file in the specified directory
        image_path = os.path.join(image_directory, f"card_{card_number}.jpg")
        with open(image_path, "wb") as f:
            f.write(response.content)
        print(f"Downloaded card {card_number}.")

print("Image download complete.")
