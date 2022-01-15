import numpy as np
import pandas as pd
from pandas import DataFrame, Series

s1 = Series(dtype=object)
df1 = DataFrame()


def create_raw_data():
    global s1, df1
    daten1 = np.arange(7)
    np.random.shuffle(daten1)
    daten2 = np.random.rand(30).reshape(5, 6)
    s1 = Series(data=daten1,
                name='DatenS1',
                index=['Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa', 'So'])
    df1 = DataFrame(daten2,
                    index=['R1', 'R2', 'R3', 'R4', 'R5'],
                    columns=['C1', 'C2', 'C3', 'C4', 'C5', 'C6'])
    # print(s1)
    # print(df1)


def print_data():
    global s1, df1
    print(s1, '\n\n', df1)
    print("="*80)
    # Ausgabe der Zeile mit index 'R3'
    print(df1.loc['R3'])
    print("="*80)
    # Ausgabe der Zeilen mit index 'R3' und 'R5'
    print(df1.loc[['R3', 'R5']])
    print("="*80)
    # Ausgabe ab Zeile 'R4', Iteration mit Schrittweite -1
    print(df1.loc['R4'::-1])
    print("="*80)
    print(df1.loc['R1'::2])
    print("="*80)
    print('Output single element R3/C3:',
          df1.loc['R3', 'C3'])
    print("="*80)
    print('Output all rows, columns C1..C3: \n',
          df1.loc[:, 'C1':'C3'])
    print("="*80)
    print('Output every second line, columns C2, C4: \n',
          df1.loc[::2,['C2', 'C4']])


def sort_data():
    global s1, df1
    print('='*80)
    print('Sorted DataFrame by column C4: \n')
    sort1 = df1.sort_values(by='C4',
                            ascending=False)
    print(sort1)
    print('='*80)
    print('Sorted DataFrame by column C4 with ignore_index: \n')
    sort2 = df1.sort_values(by='C4',
                            ascending=False,
                            ignore_index=True)
    print(sort2)


def skalare_vergleich():
    global s1, df1
    print('='*80)
    print('Data > 3: \n')
    print(s1 > 3)
    print(s1[s1 > 3])
    print('='*80)
    print('Data > 0.5: \n')
    print(df1 > 0.5)
    print(df1[df1 > 0.5])


def werte_zuweisen():
    global s1, df1
    s2 = s1.copy()
    print('='*80)
    s2['Mo']=13
    print(s2)
    print('='*80)
    print("Set all odd values to 99: \n")
    s2[s2%2 != 0] = 99
    print(s2)
    print('='*80)
    df2 = df1.copy()
    print("Set all values in column C1 to 88: \n")
    df2.loc[:,'C1'] = 88
    print(df2)
    print('='*80)
    print("Set all values < 0.5 to 13: \n")
    df2[df2 < 0.5] = 13
    print(df2)


def fehlende_werte():
    global s1, df1
    s2 = s1.copy()
    df2 = df1.copy()
    s2[['Di','Sa']]=np.nan
    df2[df2 > 0.5]=np.nan
    print("="*80)
    print("Number of missing elements (NaN): \n")
    print(df2)
    print(df2.isnull().sum())
    print("="*80)
    print("Not defined data in Series and DataFrame obejcts are NaN=Not a Number: \n")
    print(s2)
    print(df2)
    print("="*80)
    s2[s2.isnull()]=42
    print(s2)
    print("="*80)
    print(df2.fillna(42))
    print(df2.fillna({'C1':100, 'C6':200}))
    print(df2.fillna(method='ffill'))
    print("="*80)
    print("Drop missing elements: \n")
    s2 = s1.copy()
    s2[['Di','Sa']]=np.nan
    print(s2.dropna())
    df3=DataFrame({'Temp1':[10.0, 10.5, np.nan, 10.9],
                   'Temp2':[18.3, 17.9, 18.1, 10.9],
                   'Temp3':[np.nan, 33.0, 32.0, 10.9]})
    print(df3)
    print(df3.dropna(how='all'))
    print(df3.dropna(axis=1))


def doppelte_werte():
    df3 = DataFrame({'Temp1': [10.0, 10.0, 10.5, np.nan, 10.9, 10.0],
                     'Temp2': [18.3, 18.3, 18.3, 18.3, 10.9, 18.3],
                     'Temp3': [np.nan, np.nan, 33.0, 32.0, 10.9, np.nan]})
    print("=" * 80)
    print('Duplicated rows in a DataFrame object: \n')
    print('Original DataFrame object')
    print(df3)
    print('Find duplicates: \n')
    print(df3.duplicated())
    print('Find duplicates based on column Temp2: \n')
    print(df3.duplicated('Temp2'))
    print('Drop duplicates: \n')
    print(df3.drop_duplicates())
    print('Drop duplicates based on column Temp2: \n')
    print(df3.drop_duplicates(['Temp2']))
    # print(df3.drop_duplicates(['Temp2','Temp3']))


def daten_verbinden():
    global s1, df1
    s2 = s1.copy()
    df2 = df1.copy()
    df4 = DataFrame({'C7':[3, 4, 5], 'C8':[8, 9, 10]})
    df5 = DataFrame({'C1':[3, 4, 5], 'C2':[8, 9, 10]})
    print('='*80)
    print('Concatination of Series objects: \n')
    s3=pd.concat([s1, s2])
    print(s3)
    print('Concatination of DataFrame objects: \n')
    df3=pd.concat([df1, df2, df4, df5])
    print(df3)
    df3=pd.concat([df1, df2], ignore_index=True)
    print('\nignore_index=True leads to re-indexing of the DataFrame object\n')
    print(df3)
    print('Concatination of DataFrame objects (add columns): \n')
    df4.index=['R1','R2','R3']
    df3=pd.concat([df1, df4], axis=1)
    print(df3)
    print('Concatination of DataFrame and Series objects: \n')
    s2.index=['R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7']
    df3=pd.concat([df2, s2], axis=1)
    print(df3)
    # Alternative
    # DataFrame.join()
    # df2.append([df1, s1])


def daten_loeschen():
    global s1, df1
    print('='*80)
    print('Delete data in DataFrame objects \n')
    print(df1)
    print(df1.drop('R1'))
    print(df1.drop('C1', axis=1))


def daten_gruppieren():
    global s1, df1
    


def plot_data():
    global s1, df1
    df1.plot()


if __name__ == '__main__':
    create_raw_data()
    print_data()
    sort_data()
    skalare_vergleich()
    werte_zuweisen()
    fehlende_werte()
    doppelte_werte()
    daten_verbinden()
    daten_loeschen()
    daten_gruppieren()
    # plot_data()
