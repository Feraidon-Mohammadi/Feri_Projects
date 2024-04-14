import exifread
from fractions import Fraction
from PIL import Image
import piexif
import os


"""-------------------------((READ)) show all exif data metadate and gps what exist worked-------------------------- """
"""----------------------------------------------------------------------------------------------------------------- """

def print_exif_tags(image_path):
    with open(image_path, 'rb') as file:
        tags = exifread.process_file(file, details=False)  # details=False to speed up processing
        for tag in tags.keys():
            print(f"{tag}: {tags[tag]}")

#
# print_exif_tags('./output/output_ggg.JPG')
print_exif_tags('./images/IMG_1609.JPG')
"""-----------------------((READ)) show all exif data metadate and gps what exist worked---------------------------- """
"""----------------------------------------------------------------------------------------------------------------- """




"""----------------------------------((READ)) just show all gps tags worked--------------------------------------- """
def print_gps_tags(image_path):
    with open(image_path, 'rb') as image_file:
        tags = exifread.process_file(image_file)

        # Print all GPS tags if available
        for tag in tags.keys():
            if tag.startswith("GPS"):
                print(f"{tag}: {tags[tag]}")
print_gps_tags('./images/IMG_3368.JPG')
"""----------------------------------just show all gps tags worked--------------------------------------- """




"""------------------- ((WRITE)) add some metadate to a picture or change worked ----------------------------------- """
"""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ add some metadate to a picture  worked $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ """
def add_custom_metadata(image_path, custom_metadata, output_path=None):
    try:
        abs_image_path = os.path.abspath(image_path)
        output_path = output_path if output_path else abs_image_path
        with Image.open(abs_image_path) as img:
            if 'exif' in img.info:
                exif_dict = piexif.load(img.info['exif'])
                print("Original EXIF data loaded.")
            else:
                exif_dict = {'0th': {}, 'Exif': {}, 'GPS': {}, '1st': {}, 'thumbnail': None}
                print("No EXIF data found, creating new EXIF structure.")

            # Update custom metadata
            exif_dict["0th"][piexif.ImageIFD.Make] = custom_metadata.get("Make", b'')
            exif_dict["0th"][piexif.ImageIFD.Model] = custom_metadata.get("Model", b'')
            exif_dict['GPS'][piexif.GPSIFD.GPSLatitude] = custom_metadata.get('GPSLatitude')
            exif_dict['GPS'][piexif.GPSIFD.GPSLatitudeRef] = custom_metadata.get('GPSLatitudeRef')
            exif_dict['GPS'][piexif.GPSIFD.GPSLongitude] = custom_metadata.get('GPSLongitude')
            exif_dict['GPS'][piexif.GPSIFD.GPSLongitudeRef] = custom_metadata.get('GPSLongitudeRef')

            exif_bytes = piexif.dump(exif_dict)
            img.save(output_path, exif=exif_bytes)
            print("Custom metadata added and image saved to:", output_path)
    except Exception as e:
        print(f"An error occurred: {e}")


# Example: Add custom metadata
custom_metadata = {
    "Make": b"MyCamera",
    "Model": b"Model123",
    'GPSLatitude': ((34, 1), (56, 1), (41903, 1000)),  # Example values
    'GPSLatitudeRef': b'N',  # North
    'GPSLongitude': ((48, 1), (2, 1), (3213, 100)),  # Example values
    'GPSLongitudeRef': b'W',  # West
}

# Assuming the image is in the same directory as your script or notebook
add_custom_metadata("images/fff.JPG", custom_metadata, "./output/output_ggg.JPG")
"""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ add some metadate to a picture  worked $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ """
"""---------------------------------- add some metadate to a picture  worked --------------------------------------- """








""" -----------------------------------------------------------------------------------------------------------------"""
""" ---------------------------((READ)) converting 4 coordinate in to 2 coordinate worked ---------------------------"""
def extract_gps_info(image_path):
    # Open the image file for reading in binary mode
    with open(image_path, 'rb') as file:
        # Read the EXIF tags
        tags = exifread.process_file(file)

        # Check if GPSInfo is present
        if 'GPS GPSLatitude' in tags and 'GPS GPSLongitude' in tags:
            latitude = tags['GPS GPSLatitude'].values
            latitude_ref = tags['GPS GPSLatitudeRef'].values[0]
            longitude = tags['GPS GPSLongitude'].values
            longitude_ref = tags['GPS GPSLongitudeRef'].values[0]
            return (latitude, longitude, latitude_ref, longitude_ref)
        else:
            return (None, None, None, None)  # Return a tuple with None values if no GPS data


def convert_dms_to_dd(dms):
    degrees = float(dms[0].num) / float(dms[0].den)
    minutes = float(dms[1].num) / float(dms[1].den)
    seconds = float(dms[2].num) / float(dms[2].den)
    decimal_degrees = degrees + minutes/60 + seconds/3600
    return decimal_degrees


def format_dms(degrees, minutes, seconds, direction):
    formatted_seconds = float(seconds)
    formatted_dms = f"{degrees}°{minutes}'{formatted_seconds:.2f}\"{direction}"
    return formatted_dms


def gps_location_calc(latitude_dms, longitude_dms, latitude_ref, longitude_ref):
    latitude_dd = convert_dms_to_dd(latitude_dms)
    longitude_dd = convert_dms_to_dd(longitude_dms)
    formatted_latitude = format_dms(*latitude_dms, latitude_ref)
    formatted_longitude = format_dms(*longitude_dms, longitude_ref)
    return formatted_latitude, formatted_longitude


# Example usage
image_path = './images/IMG_3366.JPG'
gps_info = extract_gps_info(image_path)

if gps_info and all(gps_info):  # This checks that none of the items in gps_info are None
    latitude_dms, longitude_dms, latitude_ref, longitude_ref = gps_info
    formatted_latitude, formatted_longitude = gps_location_calc(latitude_dms, longitude_dms, latitude_ref, longitude_ref)
    print(f'GPS Coordinates: Latitude {formatted_latitude}, Longitude {formatted_longitude}')
else:
    print('No GPS information found in the metadata.')


# use the output cooridante in this website to get location
# https://openstreetmap.de/karte/#
""" -----------------------------((READ)) converting 4 coordinate in to 2 coordinate worked---------------------------"""
""" -----------------------------------------------------------------------------------------------------------------"""





"""------------------------------------------------------------------------------------------------------------------"""
"""------------------------------ check file is original or copy worked------------------------------------"""
# import os
# import exifread
# from datetime import datetime
#
def file_metadata(file_path):
    # Get file stats
    file_stats = os.stat(file_path)
    print(f"File Size: {file_stats.st_size} bytes")
    print(f"Last Modified Time: {datetime.fromtimestamp(file_stats.st_mtime)}")
    print(f"Last Accessed Time: {datetime.fromtimestamp(file_stats.st_atime)}")
    print(f"Creation Time: {datetime.fromtimestamp(file_stats.st_ctime)}")

    # Check for EXIF data if it's an image
    if file_path.lower().endswith(('.jpg', '.jpeg', '.tiff')):
        with open(file_path, 'rb') as f:
            tags = exifread.process_file(f)
            if tags:
                print("EXIF Data Found:")
                for tag in tags.keys():
                    if tag not in ['JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote']:
                        print(f"  {tag}: {tags[tag]}")
            else:
                print("No EXIF data found.")
    else:
        print("File is not an image, or is in a format that does not typically contain EXIF data.")

# Replace 'path_to_your_image.jpg' with the path to the image file you want to check
file_metadata('./images/picture.JPG')
"""------------------------------((READ)) check file is original or copy ------------------------------------"""
"""------------------------------------------------------------------------------------------------------------------"""










"""------------------------------- Recovery metadata if removed not -worked-------------------------------------"""

# import os
# import exifread

# # Function to scan a directory for images and read any existing EXIF data
# def scan_and_recover_metadata(directory):
#     for root, dirs, files in os.walk(directory):
#         for filename in files:
#             if filename.lower().endswith(('.jpg', '.jpeg', '.tiff')):
#                 file_path = os.path.join(root, filename)
#                 try:
#                     with open(file_path, 'rb') as img_file:
#                         tags = exifread.process_file(img_file)
#                         if tags:
#                             print(f"Found metadata in: {file_path}")
#                             for tag in tags.keys():
#                                 if 'GPS' in tag or 'DateTimeOriginal' in tag:
#                                     print(f"  {tag}: {tags[tag]}")
#                 except Exception as e:
#                     print(f"Error processing {file_path}: {e}")
#
# scan_and_recover_metadata('./images/ggg.jpg')



# # read after changes
# def print_exif_tags(image_path):
#     with open(image_path, 'rb') as file:
#         tags = exifread.process_file(file, details=False)  # details=False to speed up processing
#         for tag in tags.keys():
#             print(f"{tag}: {tags[tag]}")
#
#
# #print_exif_tags('./output/output_ggg.JPG')
# print(f"\n after convert----------->\n")
# print_exif_tags('./images/IMG_3368.JPG')