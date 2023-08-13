from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


bright_stars_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

page = requests.get(bright_stars_url)

soup = bs(page.text,'html.parser')

star_table = soup.find('table')

temp_list= []
table_rows = star_table.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)



Star_names = []
Distance =[]
Mass = []
Radius =[]

for i in range(1,len(temp_list)):
    Star_names.append(temp_list[i][1])
    Distance.append(temp_list[i][3])
    Mass.append(temp_list[i][5])
    Radius.append(temp_list[i][6])
    
df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius)),columns=['Star_name','Distance','Mass','Radius'])
print(df2)

df2.to_csv('bright_stars.csv')
#           Star_name         Distance   Mass         Radius
#0                Sun      0.000015813      1              1
#1             Sirius           0008.6    2.1           1.71
#2            Canopus             0310     15             71
#3     Alpha Centauri           0004.4    1.1            1.2
#4           Arcturus             0037    1.1             26
#..               ...              ...    ...            ...
#93           WOH G64         0163,000    <20  1,540 - 1,730
#94        TRAPPIST-1            039.6  0.089           0.12
#95  2MASS J0523-1403            040.3   0.07          0.086
#96    WISE 0855−0714            07.27  0.003              ?
#97            Icarus  014,400,000,000     33              ?

#[98 rows x 5 columns]