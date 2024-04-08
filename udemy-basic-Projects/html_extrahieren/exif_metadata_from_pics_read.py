
# pip install exifread
#
# import exifread
# # "images/output.jpg"
# with open("output.jpg", "rb") as file:
# 	tags = exifread.process_file(file)
# 	print(tags)
# 	print(tags.get("Image DateTime", "No DateTime tag found"))
#



################################################ alternative with tags #################################################
"""
import exifread

def extract_metadata(image_path):
    with open(image_path, "rb") as file:
        tags = exifread.process_file(file)

        metadata_to_extract = [
            "Image Make",
            "Image Model",
            "Image Orientation",
            "Image XResolution",
            "Image YResolution",
            "Image ResolutionUnit",
            "Image Software",
            "Image DateTime",
            "EXIF ExposureTime",
            "EXIF FNumber",
            "EXIF ExposureProgram",
            "EXIF ISOSpeedRatings",
            "EXIF SensitivityType",
            "EXIF DateTimeOriginal",
            "EXIF DateTimeDigitized",
            "EXIF FocalLength",
            "EXIF ColorSpace",
            "EXIF ExifImageWidth",
            "EXIF ExifImageLength",
        ]

        extracted_metadata = {key: tags.get(key, "Not Found") for key in metadata_to_extract}
        return extracted_metadata

# Example: Extract metadata from an image
image_path = "./images/metadata.jpg"
metadata = extract_metadata(image_path)

# Print extracted metadata
for key, value in metadata.items():
    print(f"{key}: {value}")
"""

############################################  second way to get all infos infos #############################################
# ---> pip install exifread
import exifread

with open("./images/metadata.jpg", "rb") as file:
    tags = exifread.process_file(file)
    for key, value in tags.items():
        print(str(key) + " : " + str(value))

        