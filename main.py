'''
-----------------------------------------------------
PyTube Downloader - Youtube Video Downloader Program
-----------------------------------------------------

Version: 2.3.1

Author: Joa98

Email: joaquinpuente98@gmail.com

------------------------------------
MIT License

Copyright (c) 2025 Joaquín Puente.
------------------------------------


'''

# Libraries
import tkinter as tk
import customtkinter as ctk
from PIL import Image
from tkinter import ttk
from audio_module import _audio_tab
from video_module import _video_tab
import os
import sys

# Ensures the icon is found by Pyinstaller
def resource_path(icon_path):
    if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, icon_path)
    
    return os.path.join(os.path.abspath("."), icon_path)

# Main application window
def main():

    # Use the system appearance
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    
    # Create the main application window
    root = ctk.CTk()
    root.title("PyTube Downloader")
    root.resizable(False, False)
 
    # Load the window icon
    icon_path = resource_path("icon.ico")
    try:
        root.iconbitmap(icon_path)
    except Exception as e:
        print("Can't find the icon:", e)

    # Create a tab
    notebook = ctk.CTkTabview(root)

    # Call the video and audio tabs
    _video_tab(notebook)
    _audio_tab(notebook)
    
    # Pack the tab into the main window
    notebook.pack(expand=True, fill='both')

    # Start Tkinter main loop
    root.mainloop()


# Ensures only runs if the script is direclty executed
if __name__ == "__main__":
    main()
