import requests
from bs4 import BeautifulSoup
import re

class API_self:

    def __init__(self,  user_url):
        self.user_url = user_url
        self.response = None
        self.soup = None


        # link = requests.get('https://www.bing.com/')
        # print(link)  # if response was true ,then It's ready to work with it
        #
        # url1 = 'https://www.bing.com/'
        # response1 = requests.get(url1)
        # soup = BeautifulSoup(response.text, 'html.parser')
        # print(soup.title.text)

    def check_url(self, second_input):

        self.response = requests.get(self.user_url)
        if self.response.status_code == 200:

            self.soup = BeautifulSoup(self.response.text, 'html.parser')

            h3_elements = self.soup.find_all('h3')
            elements = self.soup.find(second_input)

            if elements:
                for i, element in enumerate(elements):
                    text = re.sub(r'<[^>]*>', '', str(element))
                    print(f"Element {i + 1}: {text}")
            else:
                print(f"No matching elements with tag '{second_input}' found on the page.")

                # Find all h3 elements
            h3_elements = self.soup.find_all('h3','li',)
            for i, h3_element in enumerate(h3_elements):
                h3_text = re.sub(r'<[^>]*>', '', str(h3_element))
                print(f"H3 {i + 1}: {h3_text}")

            #h1_texts = [re.sub(r'<[^>]*>', '', str(h)) for h in h1_elements]


        else:
            print(f"Failed to retrieve the page. Status code: {self.response.status_code}")



user_url = input("Url: ")
instance = API_self(user_url)


second_input = input("what are u searching for in the url: ")
instance.check_url(second_input)





# Access response and soup outside the class
if instance.response is not None:
    # Use instance.response and instance.soup as needed
    print(instance.response.status_code)
    print(instance.soup.title.text)