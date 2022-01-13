import requests
from bs4 import BeautifulSoup
from requests.sessions import should_bypass_proxies

#need to install modules

class SearchYouTube:
  def __init__(self):
    self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}
    self.url = 'https://www.youtube.com/results?search_query='

  def key_words_search_words(self, user_message):
    words = user_message.split()[1:]
    keywords = '+'.join(words)
    search_words = ' '.join(words)
    #print(f'passed {keywords} + {search_words}')
    return keywords, search_words

  def search(self, keywords):
    # create requests and get the response
    print(self.url + keywords)
    response = requests.get(self.url + keywords, headers = self.headers)

    content = response.content
    #print(content)
    # pase the html and pull the data we want
    soup = BeautifulSoup(content, 'html.parser')

    print(soup)

    #result_links = soup.findAll('a')
    #print(soup.get_text())
    #for link in soup.findAll('a'):
      #print(link)



    #return result_links









