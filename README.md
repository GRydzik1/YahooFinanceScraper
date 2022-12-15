# YahooFinanceScraper
This program scrapes stock data from Yahoo Finance. This can be used by researchers to archive stock data.
This documentation outlines the job of each of the individual files in getting the program to work.

Import Stocks:
Imports a list of stock ticker symbols from a cleaned csv file.

Update Data:
Uses get requests to pull stock data from Yahoo Finance for a single stock.

Main:
Scrapes stock data for every stock on the list in the CSV, then exports an updated CSV.
Unfortunately, I was not able to get multiprocessing to work on these requests well, so the program is a lot slower than I would like it to be. Currently, it would take a little over 4 and a half hours to get data on all of the 8,000 + included stocks. 
