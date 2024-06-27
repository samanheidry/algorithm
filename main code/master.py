from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time
import pandas as pd
import tkinter as tk
from tkinter import ttk
import pandas as pd


leagues = {
    "ll2024": "https://www.varzesh3.com/football/league/2/%D9%84%D8%A7%D9%84%DB%8C%DA%AF%D8%A7-%D8%A7%D8%B3%D9%BE%D8%A7%D9%86%DB%8C%D8%A7",
    "ll2023": "https://www.varzesh3.com/football/league/2/%D9%84%D8%A7%D9%84%DB%8C%DA%AF%D8%A7-%D8%A7%D8%B3%D9%BE%D8%A7%D9%86%DB%8C%D8%A7/2022-2023",
    "ll2022": "https://www.varzesh3.com/football/league/2/%D9%84%D8%A7%D9%84%DB%8C%DA%AF%D8%A7-%D8%A7%D8%B3%D9%BE%D8%A7%D9%86%DB%8C%D8%A7/2021-2022",
    "ll2021": "https://www.varzesh3.com/football/league/2/%D9%84%D8%A7%D9%84%DB%8C%DA%AF%D8%A7-%D8%A7%D8%B3%D9%BE%D8%A7%D9%86%DB%8C%D8%A7/2020-2021",
    "ll2020": "https://www.varzesh3.com/football/league/2/%D9%84%D8%A7%D9%84%DB%8C%DA%AF%D8%A7-%D8%A7%D8%B3%D9%BE%D8%A7%D9%86%DB%8C%D8%A7/2019-2020",

    "bl2024": "https://www.varzesh3.com/football/league/1/%D8%A8%D9%88%D9%86%D8%AF%D8%B3%D9%84%DB%8C%DA%AF%D8%A7-%D8%A7%D9%93%D9%84%D9%85%D8%A7%D9%86",
    "bl2023": "https://www.varzesh3.com/football/league/1/%D8%A8%D9%88%D9%86%D8%AF%D8%B3%D9%84%DB%8C%DA%AF%D8%A7-%D8%A7%D9%93%D9%84%D9%85%D8%A7%D9%86/2022-2023",
    "bl2022": "https://www.varzesh3.com/football/league/1/%D8%A8%D9%88%D9%86%D8%AF%D8%B3%D9%84%DB%8C%DA%AF%D8%A7-%D8%A7%D9%93%D9%84%D9%85%D8%A7%D9%86/2021-2022",
    "bl2021": "https://www.varzesh3.com/football/league/1/%D8%A8%D9%88%D9%86%D8%AF%D8%B3%D9%84%DB%8C%DA%AF%D8%A7-%D8%A7%D9%93%D9%84%D9%85%D8%A7%D9%86/2020-2021",
    "bl2020": "https://www.varzesh3.com/football/league/1/%D8%A8%D9%88%D9%86%D8%AF%D8%B3%D9%84%DB%8C%DA%AF%D8%A7-%D8%A7%D9%93%D9%84%D9%85%D8%A7%D9%86/2019-2020",

    "pl2024": "https://www.varzesh3.com/football/league/3/%D9%84%DB%8C%DA%AF-%D8%A8%D8%B1%D8%AA%D8%B1-%D8%A7%D9%86%DA%AF%D9%84%DB%8C%D8%B3",
    "pl2023": "https://www.varzesh3.com/football/league/3/%D9%84%DB%8C%DA%AF-%D8%A8%D8%B1%D8%AA%D8%B1-%D8%A7%D9%86%DA%AF%D9%84%DB%8C%D8%B3/2022-2023",
    "pl2022": "https://www.varzesh3.com/football/league/3/%D9%84%DB%8C%DA%AF-%D8%A8%D8%B1%D8%AA%D8%B1-%D8%A7%D9%86%DA%AF%D9%84%DB%8C%D8%B3/2021-2022",
    "pl2021": "https://www.varzesh3.com/football/league/3/%D9%84%DB%8C%DA%AF-%D8%A8%D8%B1%D8%AA%D8%B1-%D8%A7%D9%86%DA%AF%D9%84%DB%8C%D8%B3/2020-2021",
    "pl2020": "https://www.varzesh3.com/football/league/3/%D9%84%DB%8C%DA%AF-%D8%A8%D8%B1%D8%AA%D8%B1-%D8%A7%D9%86%DA%AF%D9%84%DB%8C%D8%B3/2019-2020"
}

leag = {
    "ll": "",  
    "bl": "",  
    "pl": ""
}

league_name = input("Enter Your League Name (Laliga == ll , PrimerLeague = pl , Bundesliga = bl ) ")
if league_name not in leag:
    print("league name is incorrect")
    exit()

year = input("Enter Year(2024 , 2023 , 2022, 2021, 2020)")
if int (year) >=2025 or int (year)<=2018:
    print("Year is not supported")
    exit()

league_year=league_name+year
url_league = leagues[league_year]
xpath_table = '/html/body/section/main/div[2]/div[1]/div/section/div[3]/div/div[2]/div/div[1]/table/tbody'


options = wd.FirefoxOptions()
options.add_argument('--headless')
driver = wd.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
driver.get(url_league)

print("Receiving Data ...")
time.sleep(5)

try:
    table = driver.find_element(By.XPATH, xpath_table)
    rows = table.find_elements(By.TAG_NAME, "tr")
    data_list = []
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, "td")
        cols_text = [col.text for col in cols]
        data_list.append(cols_text)
except:print("Error in get data, please try again")
driver.quit()

df = pd.DataFrame(data_list, columns=['Rank', 'Team', 'Games', 'Wins', 'Draws', 'Losses', 'GoalDifference', 'GoalsScored', 'GoalsConceded', 'Points'])

df.to_csv('league_table.csv', index=False, encoding='utf-8-sig')

print("Data has been saved to league_table.csv")



df = pd.read_csv('league_table.csv')

def make_table():
    root = tk.Tk()
    root.title("Premier League Table")
    tree = ttk.Treeview(root, columns=('Rank', 'Team', 'Games', 'Wins', 'Draws', 'Losses', 'GoalDifference', 'GoalsScored', 'GoalsConceded', 'Points'), show='headings')
    tree.heading('Rank', text='Rank')
    tree.heading('Team', text='Team')
    tree.heading('Games', text='Games')
    tree.heading('Wins', text='Wins')
    tree.heading('Draws', text='Draws')
    tree.heading('Losses', text='Losses')
    tree.heading('GoalDifference', text='Goal Difference')
    tree.heading('GoalsScored', text='Goals Scored')
    tree.heading('GoalsConceded', text='Goals Conceded')
    tree.heading('Points', text='Points')
    tree.column('Rank', width=50, anchor='center')
    tree.column('Team', width=150, anchor='center')
    tree.column('Games', width=50, anchor='center')
    tree.column('Wins', width=50, anchor='center')
    tree.column('Draws', width=50, anchor='center')
    tree.column('Losses', width=50, anchor='center')
    tree.column('GoalDifference', width=100, anchor='center')
    tree.column('GoalsScored', width=100, anchor='center')
    tree.column('GoalsConceded', width=100, anchor='center')
    tree.column('Points', width=50, anchor='center')
    for index, row in df.iterrows():
        tree.insert('', 'end', values=(row['Rank'], row['Team'], row['Games'], row['Wins'], row['Draws'], row['Losses'], row['GoalDifference'], row['GoalsScored'], row['GoalsConceded'], row['Points']))
    tree.pack(expand=True, fill='both')
    root.mainloop()

make_table()

