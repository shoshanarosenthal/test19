import csv
import pandas as pd 
from enum import Enum
import statistics
import os
   
class Actions (Enum):
    EXIT = 0
    MOST_EXPENSIVE=1
    AVERAGE_PRICE = 2
    COUNT_IDEAL=3
    SORT_BY_COLOR = 4
    MEDIAN_CARAT_PREMIUM = 5
    AVERAGE_CARAT_PER_CUT = 6
    AVERAGE_PRICE_PER_COLOR = 7

df= pd.read_csv('diamonds.csv') 

def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def menu():
    for act in Actions: print(f"{act.value} - {act.name}") 
    return input ("your selection: ")

def most_expensive():
        price = list(df['price'])
        print(f"the most expensive diamond costs: {max(price)}")

def avarage_price():
     price = list(df['price'])
     print(f"the avarage  price of diamonds is: {statistics.mean(price)}")

def count_ideal():
    cuts = list(df['cut'])
    count = 0
    for c in cuts:
        if c == "Ideal":
             count+=1
    print(f"there are {(count)} ideal diamonds")

def sort_by_color():
    colors=set()
    for ind, row in df.iterrows():
         colors.add(row['color']) 
    for ind,color in enumerate(colors ):
                print(f"{ind} - {color}")
        
    color_list = list(colors)
    selected = color_list[int( input("select one from the list"))]
    
    counter =0
    for index, row in df.iterrows():
        if row['color'] == selected:
            counter +=1
    print(f"there is {counter} from {selected}")

def median():
    df['cut'] = df['cut'].astype(str)
    df['carat'] = pd.to_numeric(df['carat'])

    premium_diamonds = df[df['cut'] == 'Premium']
    median_carat = premium_diamonds['carat'].median()
    print(f'The median carat of diamonds with cut "Premium" is: {median_carat}')



def average_carat():
       average_carat_by_cut = df.groupby('cut')['carat'].mean()

       for cut_type, avg_carat in average_carat_by_cut.items():
          print(f'The average carat for {cut_type} cut is: {avg_carat}')

def average_price_color():
    df['color'] = df['color'].astype(str)
    average_price_per_color = df.groupby('color')['price'].mean()

    print('Average price for each color:')
    for color, avg_price in average_price_per_color.items():
            print(f'Color {color}: {avg_price} nis')

    




if __name__=="__main__":
    while True:
        # clear_screen()
        user_selection =Actions(int( menu()))
        if user_selection == Actions.EXIT:exit()
        elif user_selection == Actions.MOST_EXPENSIVE:most_expensive()
        elif user_selection == Actions.AVERAGE_PRICE:avarage_price()
        elif user_selection == Actions.COUNT_IDEAL: count_ideal()
        elif user_selection == Actions.SORT_BY_COLOR: sort_by_color()
        elif user_selection == Actions.MEDIAN_CARAT_PREMIUM:median()
        elif user_selection == Actions.AVERAGE_CARAT_PER_CUT:average_carat()
        elif user_selection == Actions.AVERAGE_PRICE_PER_COLOR: average_price_color()