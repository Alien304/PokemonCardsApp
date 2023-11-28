import tkinter as tk
import psycopg2
from PIL import Image, ImageTk
from tkinter import PhotoImage
import os

class PokemonCollectionApp:
    def __init__(self, root):
        # Create the main window with a fixed size
        self.root = root
        self.root.title("Pokémon TCG Collection")
        self.root.geometry("1440x720")
        self.root.resizable(False, False)
        self.load_data_from_database()
        self.create_gui()
        
    def load_data_from_database(self):
        # Connect to your PostgreSQL database
        connection_string = "dbname=pokemoncards user=postgres password=4645 host=localhost"
        conn = psycopg2.connect(connection_string)
        cur_exp = conn.cursor()
        cur_card = conn.cursor()
        #Fetch a list of expansions with image paths from the database 
        cur_exp.execute("SELECT setName, img_url FROM set;")
        cur_card.execute("SELECT cardname, imageurl, owned, expansion, cardnumber FROM card;")
        self.cur_exp = cur_exp.fetchall()
        self.cur_card = cur_card.fetchall()
        # Close the database connection
        cur_exp.close()
        cur_card.close()
        conn.close()
    
    def create_gui(self):
        # Create a main frame
        main_Frame = tk.Frame(self.root)
        main_Frame.pack(fill="both")
        # Create a canvas with a vertical scrollbar
        canvas_expansion = tk.Canvas(main_Frame)
        canvas_expansion.pack(expand=True, side="left", fill="both")
        canvas_cards = tk.Canvas(main_Frame)
        canvas_cards.pack(expand=True, side="right", fill="both")
        # Add a scrollbar to the Canvas
        scrollbar = tk.Scrollbar(canvas_cards, orient="vertical", command=canvas_cards.yview)
        scrollbar.pack(side="right", fill="y")
        canvas_cards.configure(yscrollcommand=scrollbar.set)
        # Adding Frames to the canvas
        frame_in_canvas_sets = tk.Frame(canvas_expansion)
        frame_in_canvas_sets.pack(fill="both", expand=False, side="left", ipady=10, ipadx=10, padx=5, pady=20)
        frame_in_canvas_cards = tk.Frame(canvas_cards, bg="black")
        frame_in_canvas_cards.pack(fill="both", expand=True, side="right", ipady=10, ipadx=50)
        # Create a list to hold PhotoImage objects
        expansion_images = []
        pk_cards_images = []
        pk_cards_names = []
        pk_cards_owned = []
        columns = 3
        # Create labels to display expansion images
        for i, expansion in enumerate(self.cur_exp):
            expansion_name, image_path = expansion[0], expansion[1]
            expansion_image = PhotoImage(file=f"PokemonCardsApp/Card_img/{image_path}")
            expansion_images.append(expansion_image)
            resized_expansion_image = expansion_image.subsample(3)
            expansion_label = tk.Button(
                frame_in_canvas_sets,
                image=resized_expansion_image,
                text=expansion_name,
                compound="top",
            )
            expansion_label.image = resized_expansion_image
            expansion_label.grid(row=i, column=0, padx=5, pady=10)

        # Create labels to display pokemon cards
        for i, pk_card in enumerate(self.cur_card):
            # Set placement of cards in SQL table
            pk_card_name, image_path_pk_card, owncheckbox_value = pk_card[0], pk_card[1], pk_card[2] 
            # Open the image with Pillow
            pk_card_image_pil = Image.open(f"PokemonCardsApp/Card_img/{image_path_pk_card}")
            # Resize the image
            pk_card_image_pil = pk_card_image_pil.resize((330, 460))
            # Convert the Pillow image to Tkinter PhotoImage
            pk_card_image = ImageTk.PhotoImage(pk_card_image_pil)
            # Apppend values to arrays
            pk_cards_images.append(pk_card_image)
            pk_cards_names.append(pk_card_name)
            pk_cards_owned.append(pk_cards_owned)
            # Claim resized image as variable
            resized_pk_card_image = pk_card_image
            # Create frame for a card
            frame_for_card = tk.Frame(frame_in_canvas_cards)
            # Set pokemon card as Label
            pk_card_label = tk.Label(frame_for_card, 
                                     image=resized_pk_card_image, 
                                     text = pk_card_name , 
                                     compound="top", anchor="n")
            pk_card_label.image = resized_pk_card_image
            # Create a checkbox of owned cards
            owned_checkbox = tk.Checkbutton(frame_for_card,
                                            text="Owned",
                                            variable=owncheckbox_value,
                                            compound="bottom", anchor="n"
                                            )
            # Place in grid
            pk_card_label.pack(fill="both")
            owned_checkbox.pack(fill="both")
            frame_for_card.grid(row=i // columns, column=i % columns, padx=15, pady=10)
        # Set the scroll region to the bounding box of the frame
        canvas_cards.update_idletasks()
        canvas_cards.config(scrollregion=canvas_cards.bbox("all"))
if __name__ == "__main__":
    root = tk.Tk()
    # Add frame for main logo bar
    #logo_frame = tk.Frame(root)
    #logo_frame.pack(fill="both", expand="True")
    # Add the Pokémon TCG logo
    #logo_image = PhotoImage(file="PokemonCardsApp/Card_img/main_logo.png")
    #resized_logo = logo_image.subsample(4)
    #logo_label = tk.Label(logo_frame, image=resized_logo)
    #logo_label.pack(side="left")
    app = PokemonCollectionApp(root)
    root.mainloop()
