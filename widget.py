from PIL import Image, ImageTk, ImageDraw, ImageFont
from tkinter import Tk, ttk, Canvas, PhotoImage
from parse import today, weather

root = Tk()
root.geometry('500x250')
root.title('Погода в Самаре')
root.resizable(height=False, width=False)
root.iconphoto(True, PhotoImage(file='icon.png'))
canvas = Canvas(root, width=600,
                height=250)
img = Image.open('sea.jpg').resize((600, 250), Image.ANTIALIAS)

font = ImageFont.truetype('arial.ttf', 18)
drawer = ImageDraw.Draw(img)
drawer.text((10, 10), f'{today}\n\n{weather}' , font=font, fill='white')
photo = ImageTk.PhotoImage(img)
canvas.create_image(1, 1, image=photo, anchor='nw')
canvas.pack()

root.mainloop()
