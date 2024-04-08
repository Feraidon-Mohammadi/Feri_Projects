# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# def search_location(latitude, longitude):
#     # Create a new instance of the Chrome driver
#     driver = webdriver.Chrome()
#
#     try:
#         # Open the website
#         driver.get("https://openstreetmap.de/karte/#")
#
#         # Wait for the search box to be present
#         search_box = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.ID, "search"))
#         )
#
#         # Clear the search box and enter the location coordinates
#         search_box.clear()
#         search_box.send_keys(f"{latitude}%20{longitude}")
#
#         # Press Enter to submit the search
#         search_box.send_keys(Keys.RETURN)
#
#         # You can add more steps to interact with the website as needed
#
#     except Exception as e:
#         print(f"Error: {e}")
#
#     finally:
#         # Close the browser window when done
#         driver.quit()
#
# # Example usage
# latitude = "00°00'00.00\"N"
# longitude = "00°00'00.00\"E"
# search_location(latitude, longitude)


###################################################### alternative after afew second open  ############################

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time  # Added import for time.sleep

def search_location(latitude, longitude):
    # Create a new instance of the Chrome driver
    driver = webdriver.Firefox()

    try:
        # Open the website
        driver.get("https://openstreetmap.de/karte/#")

        # Wait for the search box to be present
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "search"))
        )

        # Clear the search box and enter the location coordinates
        search_box.clear()
        search_box.send_keys(f"{latitude}%20{longitude}")

        # Press Enter to submit the search
        search_box.send_keys(Keys.RETURN)

        # Add a delay to keep the browser open for a few seconds (adjust as needed)
        time.sleep(10)

        # You can add more steps to interact with the website as needed

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Comment out the line below to keep the browser window open for inspection
        # driver.quit()
        pass

# Example usage
latitude = "00°00'00.00\"N"
longitude = "00°00'00.00\"E"
search_location(latitude, longitude)


########################### alternative completed function

# def search_location(latitude, longitude):
#     driver = webdriver.Firefox()
#
#     try:
#         driver.get("https://openstreetmap.de/karte/#")
#
#         # Update this line with the correct ID or other attributes of the search box
#         search_box = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.ID, "new_correct_id"))
#         )
#
#         search_box.clear()
#         search_box.send_keys(f"{latitude}%20{longitude}")
#         search_box.send_keys(Keys.RETURN)
#
#         time.sleep(5)
#
#     except Exception as e:
#         print(f"Error: {e}")
#
#     finally:
#         # Comment out the line below to keep the browser window open for inspection
#         # driver.quit()
#         pass