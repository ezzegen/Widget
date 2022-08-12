from PIL import Image, ImageSequence

background = Image.open('sea.jpg')  # .convert('RGBA')


def gifs(gif):
    animated_gif = Image.open(gif)
    all_frames = []
    for gif_frame in ImageSequence.Iterator(animated_gif):
        new_frame = background.copy()
        gif_frame = gif_frame.convert('RGBA')
        new_frame.paste(gif_frame, mask=gif_frame)
        all_frames.append(new_frame)
    return all_frames[0].save("image.gif", save_all=True, append_images=all_frames[1:], duration=50, loop=0)


if __name__ == '__main__':
    gifs('icons8-частичная-облачность.gif')
