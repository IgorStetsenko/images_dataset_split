import os
import glob
import random
import shutil


def create_folders(folder_list):
    """create folders"""
    for folder in folder_list:
        newpath = folder
        if not os.path.exists(newpath):
            os.makedirs(newpath)


def create_random_path_dataset():
    """create random path dataset"""
    path_dataset = [file for file in glob.glob("train/images/*")]
    random.shuffle(path_dataset)
    return path_dataset

if __name__ == "__main__":

    create_folders(['valid/images', 'valid/masks', 'test/images', 'test/masks'])

    list_images_path = create_random_path_dataset()
    valid_dataset = list_images_path[:int(len(list_images_path)*0.2)]
    for image in valid_dataset:
        image_name = os.path.basename(image)
        mask_path = 'train/masks/'+ image_name
        shutil.move(image, 'valid/images')
        shutil.move(mask_path, 'valid/masks')

    list_images_path = create_random_path_dataset()
    test_dataset = list_images_path[:int(len(list_images_path)*0.1)]
    for image in test_dataset:
        image_name = os.path.basename(image)
        mask_path = 'train/masks/'+ image_name
        shutil.move(image, 'test/images')
        shutil.move(mask_path, 'test/masks')
