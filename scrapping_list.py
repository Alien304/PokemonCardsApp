import requests, psycopg2
from bs4 import BeautifulSoup

# Send an HTTP GET request to the page
url = 'https://cardmavin.com/pokemon/scarlet-violet/scarlet-violet-set-list'
response = requests.get(url)
connection_string = "dbname=pokemoncards user=postgres password=4645 host=localhost"
connection = psycopg2.connect(connection_string)
cursor = connection.cursor()

if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Create a list to store card data
    card_data = []

    expansionname = "SV01"
    owned_status = False

    # Define the number of cards to scrape
    num_cards = 258  # You can adjust this as needed
    idnum = 79

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
        imgurl = (f"SV01/card_{card[0]}.jpg")
        data_to_insert = (idnum, card[1], imgurl, owned_status, expansionname, card[0])
        insert_query = "INSERT INTO card (cardid, cardname, imageurl, owned, expansion, cardnumber) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(insert_query, data_to_insert)
        connection.commit()
        print(f'Card Number: {card[0]}, Card Name: {card[1]}')
        idnum = idnum + 1
else:
    print('Failed to retrieve the page.')

cursor.close()
connection.close()