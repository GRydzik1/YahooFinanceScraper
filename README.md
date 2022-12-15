# YahooFinanceScraper
Stock Data Scraper Info:

Import Stocks:
Imports a list of stock ticker symbols from a cleaned csv file.

Update Data:
Requests Stock Data from Yahoo Finance

Main:
Requests stock data for every stock on the list in the CSV, then exports an updated CSV.
Unfortunately, I was not able to get multiprocessing to work on these requests well, so the program is a lot slower than I would like it to be.
Currently, it would take a little over 4 and a half hours to get data on all of the 8,000 + included stocks. This made it unsuitable for any real time investing,
and I was not able to take my project as far as I would have liked.
