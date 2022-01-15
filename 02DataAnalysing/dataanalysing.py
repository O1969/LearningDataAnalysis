import numpy as np
import pandas as pd
from pandas import DataFrame, Series


class DataAnalysing:
    def __init__(self, datafile):
        self.__datafile = datafile
        self.__raw_data = DataFrame()

    def import_data_from_file(self):
        self.__raw_data = pd.read_csv(self.__datafile,
                                      delimiter=';',
                                      usecols=['Wochentag', 'Umsatz', 'Warengruppe'])
        print(self.__raw_data.describe())

    def get_raw_data(self):
        return self.__raw_data

    def analysis_by_weekday(self):
        revenue_by_weekday = self.__raw_data.groupby(by='Wochentag')
        print(revenue_by_weekday.sum())
        print(revenue_by_weekday.describe())

    def analysis_by_product_group(self):
        revenue_by_product_group = self.__raw_data.groupby(by='Warengruppe')
        print(revenue_by_product_group.sum())
        print(revenue_by_product_group.describe())


if __name__ == '__main__':
    revenue = DataAnalysing('RevenueData.csv')
    revenue.import_data_from_file()
    print(revenue.get_raw_data())
    revenue.analysis_by_weekday()
    revenue.analysis_by_product_group()
