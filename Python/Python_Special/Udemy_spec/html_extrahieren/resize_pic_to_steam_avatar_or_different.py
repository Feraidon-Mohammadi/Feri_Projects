from PIL import Image
# --> pip install Pillow
def resize_image(input_path, output_path, width, height, resolution_width, resolution_height, bit_depth):
    try:
        # Open the image
        img = Image.open(input_path)

        # Resize the image
        new_size = (width, height)
        img = img.resize(new_size)

        # Set the image resolution
        info = img.info
        dpi = (resolution_width, resolution_height)
        info['dpi'] = dpi

        # Save the resized image
        img.save(output_path, dpi=dpi, bits=bit_depth)

        print(f"Image resized and saved successfully to {output_path}")

    except Exception as e:
        print(f"Error: {e}")

# Example usage
input_image_path = "./images/picture.jpg"  # Replace with your input image path
output_image_path = "./images/output_resized.jpg"  # Replace with your desired output image path

# Set custom parameters
custom_width = 184
custom_height = 184
custom_resolution_width = 96
custom_resolution_height = 96
custom_bit_depth = 24

# Resize the image with custom parameters
resize_image(input_image_path, output_image_path, custom_width, custom_height,
             custom_resolution_width, custom_resolution_height, custom_bit_depth)