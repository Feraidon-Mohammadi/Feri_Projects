def get_firefox_path(file = "places.sqlite"):
    import sys
    import os
    
    folder = ""
    
    # Mac
    if sys.platform == "darwin":
        folder = os.path.expanduser("~") + "/Library/Application Support/Firefox/Profiles"
        
    # Linux
    elif sys.platform.startswith("linux"):
        folder = os.path.expanduser("~") + "/.mozilla/firefox"
        
    # Windows
    elif sys.platform == "win32" or sys.platform == "cygwin":
        folder = os.path.expanduser("~") + "/AppData/Roaming/Mozilla/Firefox/Profiles"
        
    profile = None
    profiles = os.listdir(folder)
    for element in profiles:
        if element == "Crash Reports":
            continue
        
        if element[0] == ".":
            continue
            
        if os.path.isdir(folder + "/" + element):
            if os.path.isfile(folder + "/" + element + "/places.sqlite"):
                profile = element
    
    if profile == None:
        raise Exception("Firefox folder could not be found")
    

    return folder + "/" + profile + "/" + file
   
