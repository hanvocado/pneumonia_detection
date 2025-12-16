import matplotlib.pyplot as plt
import cv2
import os
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def show_images_in_3x3_grid(images, title_prefix='Image', header_title=None):
    num_images = len(images)
    
    fig, axes = plt.subplots(3, 3, figsize=(15, 15)) 
    
    if header_title:
        fig.suptitle(header_title, fontsize=16)
    
    for i, ax in enumerate(axes.flat):
        if i < num_images:
            # Hiển thị ảnh
            ax.imshow(images[i], cmap='gray')
            ax.set_title(f'{title_prefix} {i+1}')
            ax.axis('off')
        else:
            ax.axis('off')
    
    plt.tight_layout()
    plt.show()

def show_images_in_grid(images, title_prefix='Image', cols=3, header_title=None):
    num_images = len(images)
    rows = (num_images + cols - 1) // cols  # Tính số hàng cần thiết

    fig, axes = plt.subplots(rows, cols, figsize=(5*cols, 5*rows)) 
    
    if header_title:
        fig.suptitle(header_title, fontsize=16)
    
    for i, ax in enumerate(axes.flat):
        if i < num_images:
            # Hiển thị ảnh
            ax.imshow(images[i], cmap='gray')
            ax.set_title(f'{title_prefix} {i+1}')
            ax.axis('off')
        else:
            ax.axis('off')
    
    plt.tight_layout()
    plt.show()

def list_folder(folder_path):
    list_of_files = []
    with os.scandir(folder_path) as entries:
        for entry in entries:
            if entry.is_file():
                list_of_files.append(entry.name)

    return list_of_files