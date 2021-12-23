import pandas as pd
import requests
import spacy
import streamlit as st

from spacy import displacy
from bs4 import BeautifulSoup
import yfinance as yf


st.title('Stocks overview')

nlp = spacy.load('en_core_web_sm')

## get data from RSS feed
def extract_text_from_rss(rss_link):
    """ Extracts the headlines from the links """
    headings = []
    rC = requests.get('https://www.cnbc.com/id/15839135/device/rss/rss.html?fbclid=IwAR2o0zeWtmgEwZob45_F6e02pkTVo9uBGL0VI1GQv8mPyScEFY-hn9t089Y')
    rY = requests.get('https://finance.yahoo.com/news/rssindex')
    rW = requests.get('https://feeds.a.dj.com/rss/RSSMarketsMain.xml?fbclid=IwAR17gY8vV2SdoTLP_35v7zGYmPireg5xIX_y1VEgPYRoXVd5jVouoKRlXAc')
    r1 = requests.get(rss_link)
    soupC = BeautifulSoup(rC.content, features='xml')
    soupY = BeautifulSoup(rY.content, features='xml')
    soupW = BeautifulSoup(rW.content, features='xml')
    soup1 = BeautifulSoup(r1.content, features='xml')
    headingsC = soupC.findAll('title')
    headingsY = soupY.findAll('title')
    headingsW = soupW.findAll('title')
    headings1 = soup1.findAll('title')
    headings = headingsC + headingsY + headingsW + headings1
    return headings


token_dict = {
    'Org': [],
    'Symbol': [],
    'currentPrice': [],
    'dayHigh': [],
    'dayLow': [],
    'forwardPE': [],
    'dividendYield': []
}
nlp = spacy.load("en_core_web_sm")

def generate_stock_info(headings):
    """ 
    Finding organizations in headlines and link them with SP 500 companies data
    Then, it get the market data about them from Yahoo
    Finally, it returns dataframe with stocks overview
    """
    Stock_info_dict = {
        'Org': [],
        'Symbol': [],
        'currentPrice': [],
        'dayHigh': [],
        'dayLow': [],
        'forwardPE': [],
        'dividendYield': []
    }
    
    stocks_df = pd.read_csv('./SP500.csv')
    for title in headings:
        doc = nlp(title.text)
        for ent in doc.ents:
            try:
                if stocks_df['Name'].str.contains(ent.text).sum():
                    symbol = stocks_df[stocks_df['Name'].str.contains(ent.text)]['Symbol'].values[0]
                    org_name = stocks_df[stocks_df['Name'].str.contains(ent.text)]['Name'].values[0]
                    stock_info = yf.Ticker(symbol).info
                    print(symbol)
                     
                    stock_info_dict['Org'].append(org_name)
                    stock_info_dict['Symbol'].append(symbol)
                        
                    stock_info_dict['currentPrice'].append(stock_info['currentPrice'])
                    stock_info_dict['dayHigh'].append(stock_info['dayHigh'])
                    stock_info_dict['dayLow'].append(stock_info['dayLow'])
                    stock_info_dict['forwardPE'].append(stock_info['forwardPE'])
                    stock_info_dict['dividendYield'].append(stock_info['dividendYield'])
                else:
                    pass
            except:
                pass

    overview_df = pd.DataFrame(Stock_info_dict)
    return overview_df



# add an input field to pass the RSS link
user_input = st.text_input("Type in RSS feed you want to analyze", 'https://www.investing.com/rss/news_25.rss')

# get the financial headlines
f_headings = extract_text_from_rss(user_input)

## output the financial info
output_df = generate_stock_info(f_headings)
output_df.drop_duplicates(inplace = True)
st.dataframe(output_df)

## Display the headlines
with st.expander("Expand for financial stocks news!"):
    for heading in f_headings:
        st.markdown("* " + heading.text)