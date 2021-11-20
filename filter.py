from PIL import Image
import numpy as np


def get_average_intensity(a, b, size):
    avg_intensity = np.sum(arr[a: a + size, b: b + size])
    return int(avg_intensity // 3 // (size * size))


def paint(gray, size):
    rows = width - size + 1
    columns = height - size + 1
    for a in range(0, rows, size):
        for b in range(0, columns, size):
            average_intensity = get_average_intensity(a, b, size)
            arr[a: a + size, b: b + size] = np.full(3, int(average_intensity // gray) * gray)
    return arr


def output_image(arr):
    res = Image.fromarray(arr)
    res.save('res.jpg')


input_size = int(input("Your image size:"))
input_gray = int(input("Your gray effect value:"))
img = Image.open("img2.jpg")
arr = np.array(img)
width = len(arr)
height = len(arr[1])
arr = paint(input_gray, input_size)
output_image(arr)
