import os
import sys
import sqlite3
import pandas as pd


# Function to get the Firefox profile path
def get_firefox_path(file="places.sqlite"):
	# Determine the platform-specific Firefox profiles folder
	if sys.platform == "darwin":
		folder = os.path.expanduser("~/Library/Application Support/Firefox/Profiles/")
	elif sys.platform.startswith("linux"):
		folder = os.path.expanduser("~/.mozilla/firefox/")
	elif sys.platform == "win32" or sys.platform == "cygwin":
		folder = os.path.expanduser("~/AppData/Roaming/Mozilla/firefox/Profiles/")

	profile = None
	profiles = os.listdir(folder)
	for element in profiles:
		if element == "Crash Reports" or element[0] == ".":
			continue

		# Check if it's a directory and contains the specified file
		if os.path.isdir(os.path.join(folder, element)) and os.path.isfile(os.path.join(folder, element, file)):
			profile = element
			break

	if profile is None:
		raise Exception("Firefox folder could not be found")

	return os.path.join(folder, profile, file)


# Get the path to the places.sqlite file in the Firefox profile
paths = get_firefox_path("places.sqlite")

# Connect to the SQLite database
conn = sqlite3.connect(paths)

# Execute a SELECT query on the Moz_bookmarks table
cursor = conn.execute("SELECT * FROM moz_bookmarks")

# Fetch the results into a Pandas DataFrame
df = pd.read_sql("SELECT * FROM moz_bookmarks", conn)

# Print the DataFrame
print(df)
df.head()
df["firstname"]

for key, item in df.iterrows():
	print(key)
	print(item["firstname"] + " " + item["surname"])
	








############################################# chorom cache check #######################################################
#
# import os
# import sys
# import sqlite3
# import pandas as pd
#
#
# def get_chrome_path(file="Bookmarks"):
# 	if sys.platform == "darwin":
# 		folder = os.path.expanduser("~/Library/Application Support/Google/Chrome/Default/")
# 	elif sys.platform.startswith("linux"):
# 		folder = os.path.expanduser("~/.config/google-chrome/Default/")
# 	elif sys.platform == "win32" or sys.platform == "cygwin":
# 		folder = os.path.expanduser("~/AppData/Local/Google/Chrome/User Data/Default/")
#
# 	path = os.path.join(folder, file)
#
# 	if not os.path.exists(path):
# 		raise Exception("Chrome folder could not be found")
#
# 	return path
#
#
# # Get the path to the Bookmarks file in the Chrome profile
# path = get_chrome_path("Bookmarks")
#
# # Connect to the SQLite database
# conn = sqlite3.connect(path)
#
# # Execute a SELECT query on the bookmarks table
# cursor = conn.execute("SELECT * FROM bookmarks")
#
# # Fetch the results into a Pandas DataFrame
# df = pd.read_sql("SELECT * FROM bookmarks", conn)
#
# # Print the DataFrame
# print(df)

