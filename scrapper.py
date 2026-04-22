import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

data = []

for book in books:
    name = book.h3.a["title"]

    price = book.find("p", class_="price_color").text
    price = price.replace("£", "").replace("Â", "").strip()
    price = float(price)

    data.append({
        "Name": name,
        "Price": price
    })

df = pd.DataFrame(data)
df.to_csv("data.csv", index=False)

print("✅ Data scraped and saved!")