import shutil
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog

def CreateWidgets():
    linkLabel = Label(root, text="SELECT THE FILE TO MOVE : ", bg="navajowhite3")
    linkLabel.grid(row=1, column=0, pady=5, padx=5)

    root.sourceText = Entry(root, width=50, textvariable=sourceLocation)
    root.sourceText.grid(row=1, column=1, pady=5, padx=5, columnspan = 2)

    source_browseButton = Button(root, text="BROWSE", command=SourceBrowse, width=15)
    source_browseButton.grid(row=1, column=3, pady=5, padx=5)

    destinationLabel = Label(root, text="SELECT THE DESTINATION : ", bg="navajowhite3")
    destinationLabel.grid(row=2, column=0, pady=5, padx=5)

    root.destinationText = Entry(root, width=50, textvariable=destinationLocation)
    root.destinationText.grid(row=2, column=1, pady=5, padx=5, columnspan = 2)

    dest_browseButton = Button(root, text="BROWSE", command=DestinationBrowse, width=15)
    dest_browseButton.grid(row=2, column=3, pady=5, padx=5)

    moveButton = Button(root, text="MOVE FILE", command=MoveFile, width=15)
    moveButton.grid(row=4, column=1, pady=5, padx=5)
