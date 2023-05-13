#!/usr/bin/env python
# coding: utf-8

# # Importerar moduler 
# 
# Importerar Pandas som pd. Gör det lättare när du skriver kod och är även det universella sättet som man importera Pandas på. Samma med PySimpleGui, matplotlib och tkinter.

# In[173]:


import pandas as pd
import PySimpleGUI as sg
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# # Skapat tabeller
# 
# Skapar tabeller av datan, som visar de mest populära spelen i det olika konsollerna. Här använder jag mig av matplotlib för att kunna skapa tabellerna.

# In[174]:


# Läser in en CSV-fil till en pandas DataFrame.
df = pd.read_csv("vgsales.csv")

def PS3_tabell():
    """Function som skapar och visar en matplotlib tabell för ps3."""
    
    # Filtrerar datan så att bara de rader
    # som har ps3 i dem under rubriken "Platform" visas
    # och visar bara det första 30 raderna av datan.
    ps3_data = df[df["Platform"] == 'PS3'].head(30)

    # Tar bort onödiga kolumner som inte är relevanta.
    ps3_data = ps3_data.drop(columns=["Genre", "NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Publisher", "Year"])

    # Skapar en figure och axis till tabellen
    fig, ax = plt.subplots(figsize=(15, 7))

    # Lägger tille rubrik till tabellen.
    ax.set_title("PS3 videospel ranking")

    # Rengör onödig information så att tabellen blir snyggare.
    ax.axis("off")

    # Skapar en tabell av datan och sparar tabellen i en variabel.
    tabell = ax.table(cellText=ps3_data.values, colLabels=ps3_data.columns, loc="center")

    # Ändrar storleken på texten i cellerna
    tabell.auto_set_font_size(False)
    tabell.set_fontsize(10)

    # Automatiskt ändrar storleken på kolumnerna.
    tabell.auto_set_column_width(True)

    # Gör så att texten i alla cellerna hamnar åt vänster.
    for cell in tabell._cells:
        tabell._cells[cell].set_text_props(ha='left')

    # Skapar en canvas widget och visar den.
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
      
    # Tar canvas widget och lägger den i ett fönster.
    canvas.get_tk_widget().place(x=17.5, y=200)


def Xbox360_tabell():
    """Function som skapar och visar en matplotlib tabell för XBOX 360."""
    
    xbox360_data = df[df["Platform"] == 'X360'].head(30)
    xbox360_data = xbox360_data.drop(columns=["Genre", "NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Publisher", "Year"])
    xbox360_data = pd.DataFrame(xbox360_data)

    fig, ax = plt.subplots(figsize=(15, 7))
    ax.set_title("Xbox 360 videospel ranking")
    ax.axis("off")

    tabell = ax.table(cellText=xbox360_data.values, colLabels=xbox360_data.columns, loc="center")
    tabell.auto_set_font_size(False)
    tabell.set_fontsize(10)
    tabell.auto_set_column_width(True)

    for cell in tabell._cells:
        tabell._cells[cell].set_text_props(ha='left')
        
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()

    canvas.get_tk_widget().place(x=18, y=200)

    
    
def Wii_tabell():
    """Function som skapar och visar en matplotlib tabell för Wii."""
    
    wii_data = df[df["Platform"] == 'Wii'].head(30)
    wii_data = wii_data.drop(columns=["Genre", "NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Publisher", "Year"])
    wii_data = pd.DataFrame(wii_data)

    fig, ax = plt.subplots(figsize=(15, 7))
    ax.set_title("Wii videospel ranking")
    ax.axis("off")

    tabell = ax.table(cellText=wii_data.values, colLabels=wii_data.columns, loc="center")
    tabell.auto_set_font_size(False)
    tabell.set_fontsize(10)
    tabell.auto_set_column_width(True)

    for cell in tabell._cells:
        tabell._cells[cell].set_text_props(ha='left')

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()

    canvas.get_tk_widget().place(x=18, y=200)
    


# # Skapar min GUI
# 
# Här skapar jag min GUI med hjälp av PysSimpleGUI och tkinter. Jag använder mig av funktionerna från förrut där mina tabeller är sparade och visar dem i GUIn.

# In[175]:


# Taget fån https://chat.openai.com/c/8d7ee06e-bc25-4a9b-98d7-b6be903747c4.
def close_window():
    """Stänger ned fönstret."""
    window.destroy()

# Skapar GUI fönster.
window = tk.Tk()
window.title("Videospel sälj-data")
window.attributes("-fullscreen", True)

text_label = tk.Label(window, text="Instruktioner:\n\n Klicka på en av knapparna ovan för att visa\n de 30 högst rankade spelen för vald spelkonsol mellan årtalen 1980-2020.\n Du ser också spelens globala försäljningsstatistik räknat i miljoner.", font=("Arial", 18))
text_label.place(x=375, y=200)

# Skapar en knapp för PS3.
PS3_knapp = tk.Button(window, text="PS3", font=("Calibri",14,"bold"), height = 2, width = 10, command = PS3_tabell).place(x=500, y=75)

# Skapar en knapp för Xbox 360.
Xbox360_knapp = tk.Button(window, text="Xbox 360", font=("Calibri",14,"bold"), height = 2, width = 10, command =  Xbox360_tabell).place(x=650, y=75)

# Skapar en knapp för Wii5
Wii_knapp = tk.Button(window, text="Wii", font=("Calibri",14,"bold"), height = 2, width = 10, command = Wii_tabell).place(x=800, y=75)

Stang_knapp = tk.Button(window, text="Stäng", font=("Calibri", 14, "bold"), height = 2, width = 10, command=close_window).place(x=950, y=75)

# Startar huvudloopen för GUI-fönstret.
window.mainloop()
