from PIL import Image

def resized_image(input_image, output_image, size):
    original = Image.open(input_image)
    resized = original.resize(size)
    resized.save(output_image)

input_image = 'PYTHON_FUNCTION.PY/images.jpg'
output_image = 'output.jpg'
new_size = (200, 200)

resized_image(input_image, output_image, new_size)
