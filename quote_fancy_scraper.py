# pip install requests beautifulsoup4 

import requests
import pandas as pd
from bs4 import BeautifulSoup

URLs = ['https://quotefancy.com/motivational-quotes',
        'https://quotefancy.com/positive-quotes',
        'https://quotefancy.com/quotes-about-life']
status = requests.get(URLs[0])
print(status)

page = status.content
soup = BeautifulSoup(page, 'html.parser')
print(soup)

# Scraping Quotes and Authors

quote_elements = soup.find_all(class_='q-wrapper')
quotes_data = []

for quote_details in quote_elements:
    quote = {}

    # Verify if quote element is not a NoneType
    quote_element = quote_details.find(class_="quote-p")
    if quote_element and quote_element.find("a"):
        quote["Quote"] = quote_element.find("a").text.strip()
    else:
        quote["Quote"] = "N/A"  # Set the Quote value to N/A if not found

    # Verify if author element is not a NoneType
    author_element = quote_details.find(class_="author-p")
    if author_element and author_element.find("a"):
        quote["Author"] = author_element.find("a").text.strip()
    else:
        quote["Author"] = "N/A"  # Set the Author value to N/A if not found

    quotes_data.append(quote)  # Append the current quote to the list

print(quotes_data)

#Scraping wallpaper links

links = soup.find_all("a")
image_links = []

#  Verify if the url exists
for link in links:
    img_tag = link.find('img')
    if img_tag and img_tag.get("data-original"):
        image_links.append(img_tag["data-original"])
    else:
        # image_links.append("N/A")
        continue

print(image_links)

df = pd.DataFrame(quotes_data)
df2 = pd.DataFrame(image_links, columns= ['Wallpaper Links'])

print(df)
print(df2)

df.to_csv('Quotes.csv', index=False, encoding='utf-8')
df2.to_csv('Quotes_Wallpapers.csv', index=False, encoding='utf-8')

pd.read_csv('Quotes.csv')
pd.read_csv('Quotes_Wallpapers.csv')
