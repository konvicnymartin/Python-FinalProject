# Stock Overviews - Documentation
## What does the project do?
Our project aims to extract names of the publicly traded companies that frequently appear in the headlines of top business-oriented websites by employing the Named Entity Recognition. They are linked with available financial pieces of information (i.e., sector, current stock price, dividend yield, etc.) from Yahoo using the [S&P 500 companies list](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies). The company names are extracted from RSS feeds.

The main output of the project is a table with the information of companies appearing in the headlines of the business-oriented websites. This table is accessible through the open-source app framework streamlit. 

## Why is the project useful?
This tool may point out potential investment opportunities for investors based on the appearances of companies' names in relevant news. If we decide to develop the news-based approach to investments further, this will be one of the essential features in trading algorithms.

## How can users get started with the project?
The main code for the application is in the [appka.py](appka.py) file. We describe most of the used code in detail in the [jupyter notebook Project](Project.ipynb). The user runs the application through his/her desktop terminal using the following command. It should open up an app in your web browser.

    'streamlit run appka.py'

To run it properly, it is crucial to install all relevant packages, especially streamlit, using:

    'pip install <package_name>'

Secondly, if we try to run it in our local system, we will have to download the pre-trained core language model from the spaCy library to extract companies in a headline first using the following command:

    'python -m spacy download en_core_web_sm'

    
The application usually runs for approximately 10 minutes (depending on the computer's computational power). When the procedure is finished, the table with the companies' names and their respective pieces of information will pop up, together with the simple bar chart. In addition to the information contained in the table, the potential users can see discussed companies grouped by sector in the following bar chart.

The application scrapes RSS feeds of [CNBC](https://www.cnbc.com/id/15839135/device/rss/rss.html?fbclid=IwAR2o0zeWtmgEwZob45_F6e02pkTVo9uBGL0VI1GQv8mPyScEFY-hn9t089Y), [Yahoo Finance](https://finance.yahoo.com/news/rssindex), and [WSJ](https://feeds.a.dj.com/rss/RSSMarketsMain.xml?fbclid=IwAR17gY8vV2SdoTLP_35v7zGYmPireg5xIX_y1VEgPYRoXVd5jVouoKRlXAc) to extract names of the publicly traded companies that frequently appear in the headlines. Additionally, a user can add an RSS feed by copying the respective RSS feed link into the app text area in the web browser. The RSS feed of [Seeking Alpha](https://seekingalpha.com/feed.xml) is the default input. The RSS feeds monitor websites for new content. Therefore, the table contains only companies from recent headlines. Although the number of items in an RSS feed is theoretically unlimited, some news websites provide a certain number of posts (per day) in it.

The final table is downloadable as a CSV file. Also, the respective headlines which were used could be found in the end of the page of the application, simply by clicking on the 'Expand for financial stocks news!' button.
 
## Where can users get help with the project?
In case of any issues, the creators of the code (application) are available for help. The contact information is provided below in the next section.

## Who does maintain and contribute to the project?
Maintenance of the project is conducted by the authors of the project who are happy to answer whatever questions you may have. 

The authors are open to discuss any possible improvements. Potential contributors are more than welcomed.

Contact information:
 - 66805807@fsv.cuni.cz (Martin Konvičný),
 - 19759295@fsv.cuni.cz (Lukáš Beran)