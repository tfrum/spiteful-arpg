import os
import pygame

# this function imports frames for animations
def import_folder(path):
    surface_list = []

    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            surface_list.append(pygame.image.load(file_path).convert_alpha())
        elif os.path.isdir(file_path):
            surface_list.append(import_folder(file_path))
    return surface_list

    surface_list