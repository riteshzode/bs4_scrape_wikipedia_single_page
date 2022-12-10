import requests
from bs4 import BeautifulSoup



def get_text(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    website_title = soup.title.text
    website_text = " ".join(map(lambda p: p.text, soup.find_all("p")))

    return website_title, website_text


# we can give url as input
website_url = "https://en.wikinews.org/wiki/Global_markets_plunge"

title, text = get_text(website_url)

print("Title : " + title)
print("Summary : ")
print(text.strip())

print(f"\n\nLength of the summarized text: {str(len(text))}")

