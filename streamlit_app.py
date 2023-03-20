import streamlit
import pandas

streamlit.header('🍳 Indrayani Park Breakfast Menu')
streamlit.text('🍇 Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🌯 Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🍗 Hard-Boiled Free-Range Egg')


streamlit.header('🍌🥭I think Umesh like Strawberries 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(my_fruit_list)



