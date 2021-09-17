# Design & idea by Haider Alghifary www.haider.se
# Coding by <enter everything you want to put in here>

import sys
from PIL import Image
import PIL.ImageOps 
import tkinter as tk
from tkinter import messagebox
import os
from os import path

root= tk.Tk()
root.withdraw()

if len(sys.argv) == 1:
    messagebox.showinfo("Information", "Please run the program from the Windows Explorer context menu.")
    sys.exit()

img_full_path = sys.argv[2]
sep_pos = img_full_path.rfind(path.sep)
img_path = img_full_path[:sep_pos]
dot_pos = img_full_path.rfind(".")
img_name = img_full_path[sep_pos + 1 : dot_pos]
img_ext = img_full_path[dot_pos + 1 :].lower()

if img_ext == "jpeg" or img_ext == "jpg" or img_ext == "png" or img_ext == "tga":
    image = Image.open(img_full_path)    
    
    if sys.argv[1] == "invert_image":
        save_img_name = img_path + path.sep + img_name + "_invert." + img_ext
        
        if path.exists(save_img_name) :
            MsgBox = tk.messagebox.askquestion ('Warning','Are you sure you want to replace the existing image?',icon = 'warning')
            if MsgBox == 'no':
                sys.exit()

        if image.mode == 'RGBA':            
            r,g,b,a = image.split()
            rgb_image = Image.merge('RGB', (r,g,b))
            inverted_image = PIL.ImageOps.invert(rgb_image)
            r2,g2,b2 = inverted_image.split()
            final_transparent_image = Image.merge('RGBA', (r2,g2,b2,a))
            final_transparent_image.save(save_img_name)
        else:
            inverted_image = PIL.ImageOps.invert(image)
            inverted_image.save(save_img_name)

    elif sys.argv[1] == "invert_green_channel":
        save_img_name = img_path + path.sep + img_name + "_invert green." + img_ext

        if path.exists(save_img_name) :
            MsgBox = tk.messagebox.askquestion ('Warning','Are you sure you want to replace the existing image?',icon = 'warning')
            if MsgBox == 'no':
                sys.exit()

        if image.mode == 'RGBA':
            r,g,b,a = image.split()
            g = image.getchannel("G")
            g = PIL.ImageOps.invert(g)
            final_transparent_image = Image.merge('RGBA', (r,g,b,a))
            final_transparent_image.save(save_img_name)
        else:
            r,g,b = image.split()
            g = image.getchannel("G")
            g = PIL.ImageOps.invert(g)
            final_transparent_image = Image.merge('RGB', (r,g,b))
            final_transparent_image.save(save_img_name)
    