from bs4 import BeautifulSoup as bs
import requests

url = 'http://ethans_fake_twitter_site.surge.sh/'
response = requests.get(url, timeout=5)
content = bs(response.content, "html.parser")

dataFile = open("dataFound.txt", "a")

#tweet = content.findAll('p', attrs={"class": "content"}).text
#print(tweet)
#print (content)
#data = content.find_all('p', class_= "content")
tweets = content.find_all('p', class_= "content")

for tweet in tweets:
    dataFile.write(tweet.text.encode('utf-8', 'ignore'))
    #dataFile.write(data)
    #data = content.find_all('p', class_= "content")
    #dataFile.write(data.text.encode('utf-8'))

dataFile.close()
