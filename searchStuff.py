import requests
from bs4 import BeautifulSoup

#need to install modules

class SearchYouTube:
  def __init__(self):
    self.url = 'https://youtube.com/watch?'

  def key_words_search_words(self, user_message):
    words = user_message.split()[1:]
    keywords = '+'.join(words)
    search_words = ' '.join(words)
    #print(f'passed {keywords} + {search_words}')
    return keywords, search_words

  def search(self, keywords):
    # create requests and get the response
    response = requests.get(self.url+keywords)
    content = response.content
    #print(content)
    # pase the html and pull the data we want
    soup = BeautifulSoup(content, 'html.parser')
    result_links = soup.findAll('a')
    print(result_links.prettify())
    return result_links









