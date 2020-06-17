from splinter import Browser
from bs4 import BeautifulSoup
import tweepy

executable_path = {"executable_path": "/Users/asa/Downloads/chromedriver"}

browser = Browser("chrome", **executable_path, headless=False)

def scrape():
    final_data = {}
    output = marsNews()


    final_data["mars_news"] = output[0]
    final_data["mars_paragraph"] = output[1]
    final_data["mars_image"] = marsImage()
    final_data["mars_weather"] = marsWeather()
    final_data["mars_facts"] = marsFacts()
    final_data["mars_hemisphere"] = marsHem()
    return final_data

def marsNews():
    news_url = "https://mars.nasa.gov/news/"

    browser.visit(news_url)
    html = browser.html

    soup = BeautifulSoup(html, "html.parser")
    article = soup.find("div", class_='list_text')
    newstitle = article.find("div", class_="content_title").text
    newsp = article.find("div", class_ ="article_teaser_body").text

    output = [newstitle, newsp]
    return output

def marsImage():
    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

    browser.visit(image_url)
    html = browser.html

    soup = BeautifulSoup(html, "html.parser")
    image = soup.find("img", class_="thumb")["src"]
    featuredimageurl = "https://www.jpl.nasa.gov" + image
    return featuredimageurl

def marsWeather():
    def get_file_contents(filename):
        try:
            with open(filename, 'r') as f:
                return f.read().strip()
        except FileNotFoundError:
            print("'%s' file not found" % filename)

    consumer_key = get_file_contents('consumer_key')
    consumer_secret = get_file_contents('consumer_secret')
    access_token = get_file_contents('access_token')
    access_token_secret = get_file_contents('access_token_secret')

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    target_user = "MarsWxReport"
    tweet = api.user_timeline(target_user, count =1)
    mars_weather = ((tweet)[0]['text'])
    return mars_weather

def marsFacts():
    import pandas as pd
    facts_url = "https://space-facts.com/mars/"

    browser.visit(facts_url)

    mars_data = pd.read_html(facts_url)
    mars_data = pd.DataFrame(mars_data[0])

    mars_data.columns = ["Description", "Value"]
    mars_data = mars_data.set_index("Description")
    mars_facts = mars_data.to_html(index = True, header =True)
    return mars_facts


def marsHem():
    import time 
    hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemispheres_url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    mars_hemisphere = []

    products = soup.find("div", class_ = "result-list" )
    hemispheres = products.find_all("div", class_="item")

    for hemisphere in hemispheres:

        title = hemisphere.find("h3").text
        title = title.replace("Enhanced", "")
        end_link = hemisphere.find("a")["href"]

        image_link = "https://astrogeology.usgs.gov/" + end_link    
        browser.visit(image_link)

        html = browser.html

        soup=BeautifulSoup(html, "html.parser")
        downloads = soup.find("div", class_="downloads")
        image_url = downloads.find("a")["href"]

        dictionary = {"title": title, "img_url": image_url}
        mars_hemisphere.append(dictionary)
        
    return mars_hemisphere