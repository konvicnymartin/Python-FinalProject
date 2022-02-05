import pandas as pd
import requests
import spacy
import streamlit as st

from spacy import displacy
from bs4 import BeautifulSoup
import yfinance as yf
import matplotlib.pyplot as plt


st.title('Stocks overview')

nlp = spacy.load('en_core_web_sm')

@st.cache(suppress_st_warning=True)
def convert_df(df):
     return df.to_csv().encode('utf-8')

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
    'Sector': [],
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

    
    rSP = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soupSP = BeautifulSoup(rSP.text, 'lxml')
    tableSP=soupSP.find('table',{'id':'constituents'}).find('tbody').findAll('tr')[1:]

    stocks_df = pd.DataFrame()
    for row in tableSP:
        title = row.findAll('td')[1].text.strip()
        symbol = row.findAll('td')[0].text.strip()
        sector = row.findAll('td')[3].text.strip()
        row_ = pd.Series({"Name": title, "Symbol":symbol,"Sector":sector})
        stocks_df = pd.concat([stocks_df, row_], axis=1)

    stocks_df = stocks_df.T
    for title in headings:
        doc = nlp(title.text)
        for token in doc.ents:
            try:
                if stocks_df['Name'].str.contains(token.text).sum() and yf.Ticker(stocks_df[stocks_df['Name'].\
                                        str.contains(token.text)]['Symbol'].values[0]).info['currentPrice'] > 0:
                    symbol = stocks_df[stocks_df['Name'].\
                                        str.contains(token.text)]['Symbol'].values[0]
                    org_name = stocks_df[stocks_df['Name'].\
                                        str.contains(token.text)]['Name'].values[0]
                    token_dict['Org'].append(org_name)
                    print(symbol)
                    token_dict['Symbol'].append(symbol)
                    stock_info = yf.Ticker(symbol).info
                    token_dict['Sector'].append(stock_info['sector'])
                    token_dict['currentPrice'].append(stock_info['currentPrice'])
                    token_dict['dayHigh'].append(stock_info['dayHigh'])
                    token_dict['dayLow'].append(stock_info['dayLow'])
                    token_dict['forwardPE'].append(stock_info['forwardPE'])
                    token_dict['dividendYield'].append(stock_info['dividendYield'])
                else:
                    pass
            except:
                pass

    overview_df = pd.DataFrame(token_dict)
    return overview_df


# add an input field to pass the RSS link
user_input = st.text_input("Type in an additional RSS feed you want to analyze", 'https://seekingalpha.com/feed.xml')

# get the financial headlines
f_headings = extract_text_from_rss(user_input)

## output the financial info
output_df = generate_stock_info(f_headings)
output_df.drop_duplicates(subset = ['Symbol'], keep = 'first', inplace = True)
st.dataframe(output_df)

## download button for the dataframe
csv = convert_df(output_df)
st.download_button(
     label="Download data as CSV",
     data=csv,
     file_name='stocks_overview_df.csv',
     mime='text/csv',
 )

## Graph: Sectors
st.write('Sectors')
st.bar_chart(output_df.groupby('Sector').size())

## Display the headlines
with st.expander("Expand for financial stocks news!"):
    for heading in f_headings:
        st.markdown("* " + heading.text)