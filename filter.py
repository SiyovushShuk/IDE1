import math

import numpy as np
from PIL import Image


def get_filtered_img(arr: np.ndarray, height: int, width: int, pixel_height, pixel_width, gray_step):
    i = 0
    while i < height:
        j = 0
        while j < width:
            pixel_sum = 0
            pixel_bottom_border = arr_height if (i + pixel_height) > arr_height else i + pixel_height
            pixel_right_border = arr_width if (j + pixel_width) > arr_width else j + pixel_width
            for n in range(i, pixel_bottom_border):
                for k in range(j, pixel_right_border):
                    r, g, b = arr[n][k]
                    median = (int(r) + int(g) + int(b)) / 3
                    pixel_sum += median
            pixel_sum = int(int(pixel_sum // ((pixel_bottom_border - i) * (pixel_right_border - j))) // gray_step) * gray_step
            for n in range(i, pixel_bottom_border):
                for k in range(j, pixel_right_border):
                    arr[n][k] = [pixel_sum, pixel_sum, pixel_sum]
            j += pixel_width
        i += pixel_height
    return arr


img = Image.open("img2.jpg")

arr = np.array(img)
arr_height = len(arr)
arr_width = len(arr[0])

p_height, p_width = map(int, input().split(' '))
step = 256 // int(input('Please, input gradation count\n'))

extension = input('Please, input file extension (jpg, png, etc.)\n')

res = Image.fromarray(get_filtered_img(arr, arr_height, arr_width, p_height, p_width, step))
res.save(f'res.{extension}')
