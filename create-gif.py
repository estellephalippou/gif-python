import imageio.v3 as iio
from PIL import Image
import numpy as np

filenames = ['twitter-card.png', 'Untitled.png']
images = []

for filename in filenames:
    # read image as numpy array
    arr = iio.imread(filename)
    # convert to PIL Image for high-quality resize
    img = Image.fromarray(arr)
    # use a high-quality resampling filter
    resized = img.resize((256, 256), Image.LANCZOS)
    # convert back to numpy array for imageio
    images.append(np.array(resized))

# write animated GIF
iio.imwrite('bopcat.gif', images, duration=500, loop=0)