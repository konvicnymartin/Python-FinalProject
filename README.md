# Stock Overviews
## What the project does
Our project aims to extract names of the publicly traded companies that frequently appear in the headlines of top business-oriented websites. Consequently, we will link them with available financial pieces of information (i.e., current stock price, dividend yield, etc.) from Yahoo. We will get the company names from RSS feeds.

## Why the project is useful
This tool may point out potential investment opportunities for investors based on the appearances of companies' names in relevant news. If we decide to develop the news-based approach to investments further, this will be one of the essential features in trading algorithms.

## How users can get started with the project
The main output of the project is a table with the information of companies that appeared in the headlines of the business-oriented websites. This table is accessible through the streamlit application. To be able to use this application, one has to have installed streamlit package (Please, refer to the section 'additional information' if you do not have it istalled). 

The main code for the application is in the [appka.py](appka.py) file. The user runs the application through his/her desktop terminal using:

    'streamlit run appka.py'
    
code. The code is running approximately 10 minutes. When the procedure is finished, the table with the companies names and their respective informations will pop up, together with the simple bar chart. The bar chart gives the information of the number of companies in each sector. Together with information already contained in the table, the potential users can see which sectors are mostly discussed in the respective business-oriented websites.

The business-oriented websites included in the code are from CNBC, yahoo finance and WSJ. The user can add his/her own RSS feed by copying respective RSS feed adress into the area in the application. As an example, the RSS feed from Seeking Alpha is provided:

    https://seekingalpha.com/feed.xml

The final table can be downloaded as a CSV file. Also, the respective headlines which were used could be found in the end of the page of the application, simply by clicking on the 'Expand for financial stocks news!' button.
 
## Where users can get help with your project
In case of any issues, the creators of the code (application) are available for help. The contact information is provided in the 'additional information' section.

## Who maintains and contributes to the project
Maintenance of the project is conducted by the authors of the project who are happy to answer whatever questions you may have. 

The authors are open to discuss any possible improvements. Potential contributors are more than welcomed.

## Additional information
Code for downloading a streamlit package:

    'pip install streamlit'

Contact information:
 - 66805807@fsv.cuni.cz (Martin Konvičný),
 - 19759295@fsv.cuni.cz (Lukáš Beran)