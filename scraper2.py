from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

page = requests.get(url)

soup = bs(page.text,'html.parser')

star_table = soup.find_all('table')

temp_list= []

table_rows = star_table[7].find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

Star_names = []
Distance =[]
Mass = []
Radius =[]


for i in range(1,len(temp_list)):
    
    Star_names.append(temp_list[i][0])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][7])
    Radius.append(temp_list[i][8])

df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,)),columns=['Star_name','Distance','Mass','Radius'])
print(df2)

df2.to_csv('dwarf_stars.csv')
#                         Star_name Distance         Mass Radius
#0    SDSS J000013.54+255418.6 [de]     46.1           48   0.99
#1          2MASS J08283419-1309198
#2          2MASS J00040288-6410358      192           19   1.63
#3                        LHS 102BC
#4          2MASS J00242463-0158201     37.7           79   1.09
#..                             ...      ...          ...    ...
#346                 WISE 2348-1028     54.1
#347                 WISE 2357+1227     54.8
#348                 WISE 2359-7335     42.7
#349                WISEA 1101+5400      111
#350                         2M1510      120  40 + 39 + ?

#[351 rows x 4 columns]