import tkinter as tk
from PIL import ImageTk, Image

def _image_scale_to_fit_in_box(pil_img, new_width, new_height):
    horizontal_ratio = new_width/pil_img.width
    vertical_ratio = new_height/pil_img.height

    zoom_factor = min(horizontal_ratio, vertical_ratio)
    
    return zoom_factor


class AnnotatorGui:
    def __init__(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width = 300, height = 300)      
        self.canvas.pack()      
        self.root.update()
        
        pass

    
    def show_image(self, pil_image):
        zoom_factor = _image_scale_to_fit_in_box(pil_image, self.canvas.winfo_width(), self.canvas.winfo_height())
        
        pil_image = pil_image.resize([int(zoom_factor*s) for s in pil_image.size], Image.ANTIALIAS)

        tk_img = ImageTk.PhotoImage(pil_image)
        
        self.canvas.create_image(0, 0, anchor=tk.NW, image=tk_img)
        self.root.update()