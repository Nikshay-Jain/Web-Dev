from bs4 import BeautifulSoup
import pandas as pd
import os

def get_data(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        t = soup.find('h2')
        try:
            name = t.get_text().split('\n')[0]
        except:
            return [None, None, None, None]
        
        price = soup.find('span', class_='a-price-whole').text
        rating = soup.find('span', attrs={'class': 'a-icon-alt'}).text
        url = f"https://amazon.in/{soup.find('a', class_='a-link-normal s-line-clamp-2 s-link-style a-text-normal')['href']}"

        return [name, price, rating, url]
    
    except Exception as e:
        print(f"Error: {e}")
        return [None, None, None, None]