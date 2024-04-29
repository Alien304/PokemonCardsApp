# PokemonCardsApp
Pokemon cards app which can allow to control what card you have collected and which are missing

Summary:
  Pokemon cards images are collected from official site (https://www.pokemon.com/us) with python script.
  Data about number, names and category of cards is scrapped from site https://cardmavin.com.
  Collected data is send to internal MySQL database (using Postgresql).
  Site scrapping uses BeautifulSoup library.
  Interface is made by using library TKinter for Python language.

Still in works... 
Current state:
  Finished:
    Created Database in PostgreSQL
    Downloaded images from https://www.pokemon.com/us
    Data scrapping, connecting with database
    Importing images to the UI and setting in canvas
  In progress: 
     Creating functional UI (scrollbar and layout)
     Function of buttons which can set category of cards
     Function of making changes in status of owned cards and applying to database
    
