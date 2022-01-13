import requests
from bs4 import BeautifulSoup
#from requests.sessions import should_bypass_proxies
headers = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
#need to install modules
#'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
class SearchYouTube:
  def __init__(self):
    self.headers = {
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
      'Accept-Encoding': 'gzip, deflate',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
      }
    self.url = 'https://www.google.com/search?q=youtube'
    self.url2 = 'https://www.google.com/search?q=youtube'

  def key_words_search_words(self, user_message):
    words = user_message.split()[1:]
    keywords = '+'.join(words)
    search_words = ' '.join(words)
    #print(f'passed {keywords} + {search_words}')
    return keywords, search_words

  def search(self, keywords):
    # create requests and get the response
    print(self.url + keywords, self.headers)
    list = []
    response = requests.get(self.url2 + keywords, headers = self.headers)

    content = response.content
    #print(content)
    # parse the html and pull the data we want
    soup = BeautifulSoup(content, 'html.parser')
    #print(soup)
    #result_links = soup.findAll('a')
    #print(soup.get_text())
    #link = soup.find_all('a')
    for link in soup.find_all('a'):
      if  link.get('href') != None and 'youtube.com/watch?' in link.get('href'):
        return link.get('href')
        #list.append(link.get('href'))




    return list









