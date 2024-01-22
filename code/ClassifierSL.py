import pickle
import pandas as pd
import numpy as np
import streamlit as st

st.title('Which direction should you go?')


with open('../pickles/RFClassifier.pkl', 'rb') as pickle_in:
    pipe = pickle.load(pickle_in)
    

price = st.text_input('How Much would like to spend (USD) on your first leg of your trip ')
arr = st.text_input('What portion of the day would you like to arrive 0: early morning - 5: late night')
dep = st.text_input('What portion of the day would you like to depart 0: early morning - 5: late night')

price = int(price) if price else 0
arr = int(arr) if arr else 0
dep = int(dep) if dep else 0

temp_list = []

for i in range(0, price, 10):
    temp_list.append(pipe.predict(pd.DataFrame({'arrival_time': [arr], 'departure_time': [dep], 'price': [i]})))
    

cardinal_direction = {'N':'North','NE': 'Northeast', 'E': 'East', 'SE': 'Southeast', 'S':'South', 'SW':'Southwest', 'W':'West', 'NW': 'Northwest'}

def input_func():
    
    direction, count = np.unique(np.array(temp_list), return_counts=True)
    wander_abr = sorted(zip(count, direction), reverse=True)[0][1]
    
    return wander_abr


button= st.button('Reveal to me the enchanted path I should traverse.')

if button:
    wander_abr = input_func()
    st.write(f"Wanderlust pulls you towards the {cardinal_direction[wander_abr]}")

    