{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c30d3e18",
   "metadata": {},
   "outputs": [],
   "source": [
    "from bs4 import BeautifulSoup # to parse external data\n",
    "import yfinance as yf\n",
    "import pandas as pd # to read CSV files\n",
    "import requests # to get data\n",
    "import spacy #to extraxt entities\n",
    "import streamlit as st"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "73661cfe",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator(_root_container=0, _provided_cursor=None, _parent=None, _block_type=None, _form_data=None)"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "st.title('Stocks overview')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "65476404",
   "metadata": {},
   "outputs": [],
   "source": [
    "nlp = spacy.load('en_core_web_sm')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "30413b36",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "def extract_text_from_rss(rss_link):\n",
    "    \"\"\" Extracts the headlines from the links \"\"\"\n",
    "    headings = []\n",
    "    r1 = requests.get('https://www.cnbc.com/id/15839135/device/rss/rss.html?fbclid=IwAR2o0zeWtmgEwZob45_F6e02pkTVo9uBGL0VI1GQv8mPyScEFY-hn9t089Y')\n",
    "    r2 = requests.get(rss_link)\n",
    "    soup1 = BeautifulSoup(r1.content, features='xml')\n",
    "    soup2 = BeautifulSoup(r2.content, features='xml')\n",
    "    headings1 = soup1.findAll('title')\n",
    "    headings2 = soup2.findAll('title')\n",
    "    headings = headings1 + headings2\n",
    "    return headings"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "d3fba9cd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Company Name</th>\n",
       "      <th>Industry</th>\n",
       "      <th>Symbol</th>\n",
       "      <th>Series</th>\n",
       "      <th>ISIN Code</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>3M India Ltd.</td>\n",
       "      <td>CONSUMER GOODS</td>\n",
       "      <td>3MINDIA</td>\n",
       "      <td>EQ</td>\n",
       "      <td>INE470A01017</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>ABB India Ltd.</td>\n",
       "      <td>INDUSTRIAL MANUFACTURING</td>\n",
       "      <td>ABB</td>\n",
       "      <td>EQ</td>\n",
       "      <td>INE117A01022</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>ACC Ltd.</td>\n",
       "      <td>CEMENT &amp; CEMENT PRODUCTS</td>\n",
       "      <td>ACC</td>\n",
       "      <td>EQ</td>\n",
       "      <td>INE012A01025</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>AIA Engineering Ltd.</td>\n",
       "      <td>INDUSTRIAL MANUFACTURING</td>\n",
       "      <td>AIAENG</td>\n",
       "      <td>EQ</td>\n",
       "      <td>INE212H01026</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>APL Apollo Tubes Ltd.</td>\n",
       "      <td>METALS</td>\n",
       "      <td>APLAPOLLO</td>\n",
       "      <td>EQ</td>\n",
       "      <td>INE702C01027</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            Company Name                  Industry     Symbol Series  \\\n",
       "0          3M India Ltd.            CONSUMER GOODS    3MINDIA     EQ   \n",
       "1         ABB India Ltd.  INDUSTRIAL MANUFACTURING        ABB     EQ   \n",
       "2               ACC Ltd.  CEMENT & CEMENT PRODUCTS        ACC     EQ   \n",
       "3   AIA Engineering Ltd.  INDUSTRIAL MANUFACTURING     AIAENG     EQ   \n",
       "4  APL Apollo Tubes Ltd.                    METALS  APLAPOLLO     EQ   \n",
       "\n",
       "      ISIN Code  \n",
       "0  INE470A01017  \n",
       "1  INE117A01022  \n",
       "2  INE012A01025  \n",
       "3  INE212H01026  \n",
       "4  INE702C01027  "
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "stocks_df = pd.read_csv('./Nifty500.csv')  ## https://www1.nseindia.com/products/content/equities/indices/nifty_500.htm\n",
    "stocks_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "8d8ed31f",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2021-12-19 21:54:14.352 NumExpr defaulting to 8 threads.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "{'zip': '560001',\n",
       " 'sector': 'Industrials',\n",
       " 'fullTimeEmployees': 1146,\n",
       " 'longBusinessSummary': '3M India Limited engages in the manufacture and trade of various products for health care, manufacturing, automotive, safety, electronics, energy, commercial solutions, transportation, and design and construction industries in India. The company operates through four segments: Safety and Industrial, Transportation and Electronics, Health Care, and Consumer. The Safety and Industrial segment offers vinyl, polyester, foil, and specialty industrial tapes and adhesives, such as scotch masking tapes, scotch filament and packaging tapes, functional and decorative graphics, abrasion-resistant films, masking tapes, and other specialty materials. This segment serves industrial, electrical, and safety markets. The Health Care segment provides medical and surgical supplies; medical devices; skin and wound care, as well as infection prevention products and solutions; drug delivery systems; dental and orthodontic products; and food safety products. The Transportation and Electronics segment offers personal protection products, brand and asset protection solutions, border control products, passive fire protection products for industries and commercial establishments, track and trace products, and cleaning and hygiene products for the hospitality industry. The Consumer segment provides home improvement, stationery and office supplies, home care, and consumer health care. This segment also includes retail auto care product lines, such as office supply, stationery, home improvement (do-it-yourself), home care, protective material, consumer retail personal safety, and consumer healthcare products. The company also exports its products. The company was incorporated in 1987 and is based in Bengaluru, India. 3M India Limited operates as a subsidiary of 3M Company.',\n",
       " 'city': 'Bengaluru',\n",
       " 'phone': '91 80 2223 1414',\n",
       " 'country': 'India',\n",
       " 'companyOfficers': [],\n",
       " 'website': 'https://www.3mindia.in',\n",
       " 'maxAge': 1,\n",
       " 'address1': 'WeWork Prestige Central',\n",
       " 'fax': '91 80 2223 1450',\n",
       " 'industry': 'Conglomerates',\n",
       " 'address2': '3rd floor 36 Infantry Road Tasker Town',\n",
       " 'ebitdaMargins': 0.0995,\n",
       " 'profitMargins': 0.07111,\n",
       " 'grossMargins': 0.36743,\n",
       " 'operatingCashflow': 2914648064,\n",
       " 'revenueGrowth': 0.218,\n",
       " 'operatingMargins': 0.08841,\n",
       " 'ebitda': 3136870912,\n",
       " 'targetLowPrice': None,\n",
       " 'recommendationKey': 'none',\n",
       " 'grossProfits': 9920188000,\n",
       " 'freeCashflow': 1849205376,\n",
       " 'targetMedianPrice': None,\n",
       " 'currentPrice': 24480,\n",
       " 'earningsGrowth': -0.144,\n",
       " 'currentRatio': 2.978,\n",
       " 'returnOnAssets': 0.06745,\n",
       " 'numberOfAnalystOpinions': None,\n",
       " 'targetMeanPrice': None,\n",
       " 'debtToEquity': 1.48,\n",
       " 'returnOnEquity': 0.11847,\n",
       " 'targetHighPrice': None,\n",
       " 'totalCash': 11867883520,\n",
       " 'totalDebt': 296408000,\n",
       " 'totalRevenue': 31526152192,\n",
       " 'totalCashPerShare': 1053.433,\n",
       " 'financialCurrency': 'INR',\n",
       " 'revenuePerShare': 2798.463,\n",
       " 'quickRatio': 2.234,\n",
       " 'recommendationMean': None,\n",
       " 'exchange': 'NSI',\n",
       " 'shortName': '3M INDIA LTD',\n",
       " 'longName': '3M India Limited',\n",
       " 'exchangeTimezoneName': 'Asia/Kolkata',\n",
       " 'exchangeTimezoneShortName': 'IST',\n",
       " 'isEsgPopulated': False,\n",
       " 'gmtOffSetMilliseconds': '19800000',\n",
       " 'quoteType': 'EQUITY',\n",
       " 'symbol': '3MINDIA.NS',\n",
       " 'messageBoardId': 'finmb_881351',\n",
       " 'market': 'in_market',\n",
       " 'annualHoldingsTurnover': None,\n",
       " 'enterpriseToRevenue': 8.401,\n",
       " 'beta3Year': None,\n",
       " 'enterpriseToEbitda': 84.431,\n",
       " '52WeekChange': 0.15501773,\n",
       " 'morningStarRiskRating': None,\n",
       " 'forwardEps': None,\n",
       " 'revenueQuarterlyGrowth': None,\n",
       " 'sharesOutstanding': 11265100,\n",
       " 'fundInceptionDate': None,\n",
       " 'annualReportExpenseRatio': None,\n",
       " 'totalAssets': None,\n",
       " 'bookValue': 1778.09,\n",
       " 'sharesShort': None,\n",
       " 'sharesPercentSharesOut': None,\n",
       " 'fundFamily': None,\n",
       " 'lastFiscalYearEnd': 1617148800,\n",
       " 'heldPercentInstitutions': 0.08179,\n",
       " 'netIncomeToCommon': 2241682944,\n",
       " 'trailingEps': 198.985,\n",
       " 'lastDividendValue': None,\n",
       " 'SandP52WeekChange': 0.2505386,\n",
       " 'priceToBook': 13.767582,\n",
       " 'heldPercentInsiders': 0.7648,\n",
       " 'nextFiscalYearEnd': 1680220800,\n",
       " 'yield': None,\n",
       " 'mostRecentQuarter': 1632960000,\n",
       " 'shortRatio': None,\n",
       " 'sharesShortPreviousMonthDate': None,\n",
       " 'floatShares': 2585639,\n",
       " 'beta': 0.423008,\n",
       " 'enterpriseValue': 264850063360,\n",
       " 'priceHint': 2,\n",
       " 'threeYearAverageReturn': None,\n",
       " 'lastSplitDate': None,\n",
       " 'lastSplitFactor': None,\n",
       " 'legalType': None,\n",
       " 'lastDividendDate': None,\n",
       " 'morningStarOverallRating': None,\n",
       " 'earningsQuarterlyGrowth': -0.144,\n",
       " 'priceToSalesTrailing12Months': 8.762472,\n",
       " 'dateShortInterest': None,\n",
       " 'pegRatio': None,\n",
       " 'ytdReturn': None,\n",
       " 'forwardPE': None,\n",
       " 'lastCapGain': None,\n",
       " 'shortPercentOfFloat': None,\n",
       " 'sharesShortPriorMonth': None,\n",
       " 'impliedSharesOutstanding': None,\n",
       " 'category': None,\n",
       " 'fiveYearAverageReturn': None,\n",
       " 'previousClose': 24926.6,\n",
       " 'regularMarketOpen': 25040,\n",
       " 'twoHundredDayAverage': 25533.867,\n",
       " 'trailingAnnualDividendYield': None,\n",
       " 'payoutRatio': 0,\n",
       " 'volume24Hr': None,\n",
       " 'regularMarketDayHigh': 25040,\n",
       " 'navPrice': None,\n",
       " 'averageDailyVolume10Day': 2593,\n",
       " 'regularMarketPreviousClose': 24926.6,\n",
       " 'fiftyDayAverage': 25775.902,\n",
       " 'trailingAnnualDividendRate': None,\n",
       " 'open': 25040,\n",
       " 'toCurrency': None,\n",
       " 'averageVolume10days': 2593,\n",
       " 'expireDate': None,\n",
       " 'algorithm': None,\n",
       " 'dividendRate': None,\n",
       " 'exDividendDate': None,\n",
       " 'circulatingSupply': None,\n",
       " 'startDate': None,\n",
       " 'regularMarketDayLow': 24461.55,\n",
       " 'currency': 'INR',\n",
       " 'trailingPE': 123.024345,\n",
       " 'regularMarketVolume': 4205,\n",
       " 'lastMarket': None,\n",
       " 'maxSupply': None,\n",
       " 'openInterest': None,\n",
       " 'marketCap': 276247019520,\n",
       " 'volumeAllCurrencies': None,\n",
       " 'strikePrice': None,\n",
       " 'averageVolume': 4434,\n",
       " 'dayLow': 24461.55,\n",
       " 'ask': 0,\n",
       " 'askSize': 0,\n",
       " 'volume': 4205,\n",
       " 'fiftyTwoWeekHigh': 31000,\n",
       " 'fromCurrency': None,\n",
       " 'fiveYearAvgDividendYield': None,\n",
       " 'fiftyTwoWeekLow': 18777,\n",
       " 'bid': 0,\n",
       " 'tradeable': False,\n",
       " 'dividendYield': None,\n",
       " 'bidSize': 0,\n",
       " 'dayHigh': 25040,\n",
       " 'regularMarketPrice': 24480,\n",
       " 'preMarketPrice': None,\n",
       " 'logo_url': 'https://logo.clearbit.com/3mindia.in'}"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "stock_info = yf.Ticker('3MINDIA.NS') ## without NS there is no info\n",
    "stock_info.info"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b1f961ee",
   "metadata": {},
   "outputs": [],
   "source": [
    "stocksSP500 = pd.read_csv('./SP500.csv') ## https://github.com/datasets/s-and-p-500-companies\n",
    "stocksSP500.head() "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f03dde27",
   "metadata": {},
   "outputs": [],
   "source": [
    "stock_info_SP500 = yf.Ticker('MMM')\n",
    "stock_info_SP500.info"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "215f5b6e",
   "metadata": {},
   "outputs": [],
   "source": [
    "def generate_stock_info(headings):\n",
    "    \"\"\" Goes over each heading to found out the entitites and link it with Nifty 500 companies data\n",
    "    and Extract the market data using yahoo finanec ticker function \n",
    "    \n",
    "    Return: data frame containing all the buzzing stocks and their stats\n",
    "    \"\"\"\n",
    "    Stock_info_dict = {\n",
    "        'Org': [],\n",
    "        'Symbol': [],\n",
    "        'currentPrice': [],\n",
    "        'dayHigh': [],\n",
    "        'dayLow': [],\n",
    "        'forwardPE': [],\n",
    "        'dividendYield': []\n",
    "    }\n",
    "    \n",
    "    stocks_df = pd.read_csv('./Nifty500.csv')\n",
    "    for title in headings:\n",
    "        doc = nlp(title.text)\n",
    "        for ent in doc.ents:\n",
    "            try:\n",
    "                if stocks_df['Company Name'].str.contains(ent.text).sum():\n",
    "                    symbol = stocks_df[stocks_df['Company Name'].str.contains(ent.text)]['Symbol'].values[0]\n",
    "                    org_name = stocks_df[stocks_df['Company Name'].str.contains(ent.text)]['Company Name'].values[0]\n",
    "                        #  sending yfinance the symbol for stock info\n",
    "                    stock_info = yf.Ticker(symbol+\".NS\").info\n",
    "                    print(symbol)\n",
    "                     \n",
    "                    stock_info_dict['Org'].append(org_name)\n",
    "                    stock_info_dict['Symbol'].append(symbol)\n",
    "                        \n",
    "                    stock_info_dict['currentPrice'].append(stock_info['currentPrice'])\n",
    "                    stock_info_dict['dayHigh'].append(stock_info['dayHigh'])\n",
    "                    stock_info_dict['dayLow'].append(stock_info['dayLow'])\n",
    "                    stock_info_dict['forwardPE'].append(stock_info['forwardPE'])\n",
    "                    stock_info_dict['dividendYield'].append(stock_info['dividendYield'])\n",
    "                else:\n",
    "                    pass\n",
    "            except:\n",
    "                pass\n",
    "\n",
    "    output_df = pd.DataFrame(Stock_info_dict)\n",
    "    return output_df\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "caf8e7c0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'https://www.cnbc.com/id/15839135/device/rss/rss.html?fbclid=IwAR2o0zeWtmgEwZob45_F6e02pkTVo9uBGL0VI1GQv8mPyScEFY-hn9t089Y'"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# add an input field to pass the RSS link\n",
    "user_input = st.text_input('Add your RSS link here', 'https://www.cnbc.com/id/15839135/device/rss/rss.html?fbclid=IwAR2o0zeWtmgEwZob45_F6e02pkTVo9uBGL0VI1GQv8mPyScEFY-hn9t089Y')\n",
    "user_input"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "c089c9a3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# get the financial headlines\n",
    "fin_headings = extract_text_from_rss(user_input)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "a8a15b90",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator(_root_container=0, _provided_cursor=None, _parent=None, _block_type=None, _form_data=None)"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "## output the financial info\n",
    "output_df = generate_stock_info(fin_headings)\n",
    "output_df.drop_duplicates(inplace = True)\n",
    "st.dataframe(output_df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "5629b5ff",
   "metadata": {},
   "outputs": [],
   "source": [
    "## Display the headlines\n",
    "with st.expander(\"Expand for financial stocks news!\"):\n",
    "    for heading in fin_headings:\n",
    "        st.markdown(\"* \" + heading.text)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
