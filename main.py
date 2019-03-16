import os
import time

from annotator import Annotator

def get_image_path_from_user():
    done = False
    while not done:
        images_path = input("Enter image source directory path > ")
        if not os.path.isdir(images_path):
            print("Invalid directory path \"{}\", try again.".format(images_path))
        else:
            done = True
    return images_path

def main():

    images_path = get_image_path_from_user()
    
    annotator = Annotator(
        categories=["dog", "cat"],
        images_path=images_path
    )
    annotator.begin_annotation()
    # while True:
    #     # time.sleep(10)

if __name__ == "__main__":
    main()