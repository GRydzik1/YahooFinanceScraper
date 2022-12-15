import Import_Stocks
import update_data
import cProfile
import pandas as pd
import csv

Import_Stocks.get_stock_list()
def get_stocks():
    i = 0
    while i < int(len(Import_Stocks.listofstocks)):
        update_data.get_stock_data(Import_Stocks.listofstocks[i])
        i += 1
if __name__ == "__main__":
    with cProfile.Profile() as pr:
        get_stocks()
        dict = {'name': Import_Stocks.listofstocks, 'value' : update_data.stock_data}
        df = pd.DataFrame(dict)
        df.to_csv("Updated_Stock_Data.csv")