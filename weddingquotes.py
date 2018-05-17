from urllib2 import *
from BeautifulSoup import *

url = "http://quotes.yourdictionary.com/theme/marriage/"
response = urlopen(url).read()
soup = BeautifulSoup(response)

quotes = soup.findAll('p', attrs={'class': 'quoteContent'})
for quote in quotes[0:5]:
    print quote.text

