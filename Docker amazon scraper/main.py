import os
import pandas as pd
from get_multiple import scrape
from data_collector import get_data

if __name__ == '__main__':
    os.system("mkdir data")
    scrape()

    data = {"Name": [], "Price": [], "Rating": [], "URL": []}
    for file in os.listdir('data'):
        d = get_data(open(f"data/{file}", 'r', encoding='utf-8').read())
        data['Name'].append(d[0])
        data['Price'].append(d[1])
        data['Rating'].append(d[2])
        data['URL'].append(d[3])
        print(f"Data from data/{file} added to data.")
        
    pd.DataFrame(data).to_csv('data.csv', index=False)