#image = mapscript.imageObj(320, 240, 'GD/JPEG')

from PIL import Image
import glob, sys

# Create the frames
frames = []
imgs = sorted(glob.glob("./png/*.png"))
for i in imgs:
    new_frame = Image.open(i)
    frames.append(new_frame)

# Save into a GIF file that loops forever
frames[0].save('png_to_gif.gif', format='GIF',
               append_images=frames[1:],
               save_all=True,
               duration=300, loop=0)
