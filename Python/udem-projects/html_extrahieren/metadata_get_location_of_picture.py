import exifread
from fractions import Fraction

def extract_gps_info(image_path):
    # Open the image file for reading in binary mode
    with open(image_path, 'rb') as file:
        # Read the EXIF tags
        tags = exifread.process_file(file)

        # Check if GPSInfo is present
        if 'GPS GPSLatitude' in tags and 'GPS GPSLongitude' in tags:
            latitude = tags['GPS GPSLatitude'].values
            latitude_ref = tags['GPS GPSLatitudeRef'].values
            #print(latitude_ref)

            longitude = tags['GPS GPSLongitude'].values
            longitude_ref = tags['GPS GPSLongitudeRef'].values
            #print(longitude_ref)

            return latitude, longitude, latitude_ref, longitude_ref
        else:
            return "No GPS data found! :( "

def convert_dms_to_dd(dms):
    degrees, minutes, seconds = dms
    decimal_degrees = degrees + minutes/60 + seconds/3600
    return decimal_degrees

def format_dms(degrees, minutes, seconds, direction):
    # Convert seconds to a float before formatting
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
image_path = './images/IMG_0602.JPG'
gps_info = extract_gps_info(image_path)

if gps_info:
    latitude_dms, longitude_dms, latitude_ref, longitude_ref = gps_info
    formatted_latitude, formatted_longitude = gps_location_calc(latitude_dms, longitude_dms, latitude_ref, longitude_ref)
    print(f'GPS Coordinates: Latitude {formatted_latitude}, Longitude {formatted_longitude}')
else:
    print('No GPS information found in the metadata.')



# use the output cooridante in this website to get location
# https://openstreetmap.de/karte/#