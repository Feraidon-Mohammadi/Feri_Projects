from PIL import Image
import piexif
import os

def add_custom_metadata(image_path, custom_metadata):
    
    # Get the absolute path of the image
    abs_image_path = os.path.abspath(image_path)

    # Open the image
    img = Image.open(abs_image_path)

    # Create an Exif data dictionary if it doesn't exist
    exif_dict = piexif.load(img.info.get('exif',b''))

    # Add or update custom metadata
    exif_dict["0th"][piexif.ImageIFD.Make] = custom_metadata.get("Make", b'')
    exif_dict["0th"][piexif.ImageIFD.Model] = custom_metadata.get("Model", b'')

    # Convert the Exif data back to bytes
    exif_bytes = piexif.dump(exif_dict)

    # Update the image with the new metadata
    img.info["exif"] = exif_bytes

    # Save the modified image
    img.save("output.jpg")

    print("Custom metadata added successfully.")

    

# Example: Add custom metadata
custom_metadata = {
    "Make": b"MyCamera",
    "Model": b"Model123",
}

# Assuming the image is in the same directory as your script or notebook
add_custom_metadata("steam.jpg", custom_metadata)


