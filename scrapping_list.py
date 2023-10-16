import requests
from bs4 import BeautifulSoup

# Send an HTTP GET request to the page
url = 'https://cardmavin.com/pokemon/scarlet-violet/scarlet-violet-set-list'
response = requests.get(url)

if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Create a list to store card data
    card_data = []

    # Define the number of cards to scrape
    num_cards = 198  # You can adjust this as needed

    for i in range(1, num_cards + 1):
        row_class = f'row-{1 * i + 1}'
        row = soup.find(class_=row_class)

        if row:
            card_number = row.find(class_='column-1').text
            card_data.append(card_number)

        if row:
            card_name = row.find(class_='column-4').text
            card_data[i-1] = (card_data[i-1], card_name)
    
    # Print or process card data as needed
    for card in card_data:
        print(f'Card Number: {card[0]}, Card Name: {card[1]}')

else:
    print('Failed to retrieve the page.')
