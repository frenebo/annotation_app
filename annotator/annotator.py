import os
from PIL import Image
import time

from .annotator_gui import AnnotatorGui

class Annotator:
    def __init__(self, categories, images_path):
        assert isinstance(categories, list), "Assert categories is a list of strings"
        for category in categories:
            assert isinstance(category, str), "Assert categories is a list of strings"
        
        assert isinstance(images_path, str), "Assert images path is a string"
        assert os.path.isdir(images_path), "Assert images path is valid"
        
        self.categories = categories
        self.images_path = images_path
    
    def begin_annotation(self):
        self.gui = AnnotatorGui()
        for filename in os.listdir(self.images_path):
            filepath = os.path.join(self.images_path, filename)
            try:
                pil_img = Image.open(filepath)
            except Exception as e:
                raise e
            self.gui.show_image(pil_img)
            time.sleep(1)


            # if filename.endswith(".jpeg") or filename.endswith(".jpg"):
            #     pass
            # elif filename.endswith(".png"):
            #     pass

