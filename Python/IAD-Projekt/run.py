import os

from app import create_app



import webbrowser
from threading import Timer
def open_browser():
    url = 'http://127.0.0.1:5000/home'
    chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    edge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

    # Check if Chrome is installed by checking the existence of its executable
    if os.path.isfile(chrome_path):
        # Use the Chrome browser
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        browser = webbrowser.get('chrome')
    else:
        # Fallback to Edge if Chrome is not found
        webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
        browser = webbrowser.get('edge')

    browser.open_new(url)



app = create_app()

if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run(debug=False)
    # app.run(port="127.0.0.1:5000",debug=True)