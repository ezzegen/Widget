from PIL import Image, ImageTk, ImageDraw, ImageFont
from tkinter import Tk, ttk, Canvas, PhotoImage
from parse import today, weather, gif

root = Tk()
root.geometry('550x300')
root.title('Погода в Самаре')
root.resizable(height=False, width=False)
root.iconphoto(True, PhotoImage(file='icon.png'))
canvas = Canvas(root, width=550,
                height=300)
img = Image.open('sea.jpg').resize((550, 300), Image.ANTIALIAS)
font = ImageFont.truetype('beer_money.ttf', 19)
drawer = ImageDraw.Draw(img)
drawer.text((10, 10), f'{today}\n\n{weather}', font=font, fill='white')
photo1 = ImageTk.PhotoImage(img)
photo2 = ImageTk.PhotoImage(gif)
canvas.create_image(1, 1, image=photo1, anchor='nw')
canvas.create_image(30, 180, image=photo2, anchor='nw')
canvas.pack()


root.mainloop()
