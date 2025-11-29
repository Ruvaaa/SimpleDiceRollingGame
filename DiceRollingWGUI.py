import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x300")
root.title("Dice Rolling game")

#Main label
mainLabel = tk.Label(root, text = "Dice Roller", font = ("Arial",20))
mainLabel.grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 10)


#Initialise 
root.mainloopt()