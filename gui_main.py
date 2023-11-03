import tkinter as tk
import psycopg2
from tkinter import PhotoImage
from PIL import Image, ImageTk
import os

# Connect to your PostgreSQL database
connection_string = "dbname=pokemoncards user=postgres password=4645 host=localhost"
conn = psycopg2.connect(connection_string)
cur = conn.cursor()

# Fetch a list of expansions with image paths from the database
cur.execute("SELECT setName, img_url FROM set;")
expansions = cur.fetchall()

# Close the database connection
cur.close()
conn.close()

# Create the main window with a fixed size
root = tk.Tk()
root.title("Pokémon TCG Collection")
height, width = 900, 900
root.geometry(f"{height}x{width}")  # Set the window size to 800x600 pixels
root.resizable(False, False) # Lock the window size

# Add the Pokémon TCG logo (replace 'logo.png' with the actual image path)
logo_image = PhotoImage(file="PokemonCardsApp/Card_img/main_logo.png")
resized_logo = logo_image.subsample(2)
logo_label = tk.Label(root, image=resized_logo)
logo_label.pack()

# Create a canvas with a vertical scrollbar
canvas = tk.Canvas(root)
canvas.pack(expand=True, fill="both")

scrollbar = tk.Scrollbar(canvas, command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame inside the canvas to hold the labels
#frame_in_canvas = tk.Frame(canvas, bg="lightgray")
#frame_in_canvas.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Add a frame inside the canvas to hold the labels
frame_in_canvas = tk.Frame(canvas, bg="lightgray")
frame_in_canvas.pack(fill="both", expand=True)

# Create a list to hold PhotoImage objects
expansion_images = []

# Create labels to display expansion images in a 2-column grid
columns = 2

# Create labels to display expansion images
for i, expansion in enumerate(expansions):
    expansion_name, image_path = expansion[0],  expansion[1]
    expansion_image = PhotoImage(file=f"PokemonCardsApp/Card_img/{image_path}")
    expansion_images.append(expansion_image)  # Store the PhotoImage objects in a list
    resized_expansion_image = expansion_image.subsample(2)
    expansion_label = tk.Label(frame_in_canvas, image=resized_expansion_image, compound="top", anchor="n")
    expansion_label.image = resized_expansion_image
    #expansion_label.pack(fill="both", expand = True)
    expansion_label.grid(row=i // columns, column=i % columns, padx=10, pady=10)

def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

canvas.bind("<Configure>", on_configure)

# Run the Tkinter main loop
root.mainloop()