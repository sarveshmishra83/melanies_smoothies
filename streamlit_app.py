# Import python packages
import streamlit as st

#from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col



# Write directly to the app
st.title(":cup_with_straw: Example Streamlit App :cup_with_straw:")
#st.write(
#    """Replace this example with your own code!
#    **And if you're new to Streamlit,** check
#    out our easy-to-follow guides at
#    [docs.streamlit.io](https://docs.streamlit.io).
#    """

st.write(
    """Choose the fruits you want in your custom smoothie !
    """
)

title = st.text_input('Movie Title', 'Life of Brian')
st.write('The current movie title is', title)

name_on_order = st.text_input('Name on Smoothie')

st.write('The name on your smoothie will be:', name_on_order)

#Replace this example with your own code
#import streamlit as st
#option = st.selectbox(
#   "What is your favourite food?",
#    ("Banana", "StrawBerries", "Peaches"))
#st.write("Your favourite food is:", option)

cnx = st.connection("snowflake")
session =cnx.session()
#session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)
ingredients_list =st.multiselect(
'choose upto 5 ingredients:', my_dataframe
    ,max_selections = 5
    
)

# Lesson 2 -Cleaning Up Empty Brackets
#st.write(ingredients_list)
#st.text(ingredients_list)

# Lesson 2 -Cleaning Up Empty Brackets
ingredients_string = ''
if ingredients_list:
   # st.write(ingredients_list)
   # st.text(ingredients_list)
   # ingredients_string = ''

    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ' '
    st.write(ingredients_string)

 # Lesson 3 code   
#my_insert_stmt = """ insert into smoothies.public.orders(ingredients)
#            values ('""" + ingredients_string + """')"""

####Lesson 4 Code - enhanced.
my_insert_stmt = """ insert into smoothies.public.orders(ingredients, name_on_order)
            values ('""" + ingredients_string + """',  '""" +name_on_order+ """')"""



time_to_insert = st.button('Submit Order')
#st.write(my_insert_stmt)

#if ingredients_string:
if time_to_insert:
        session.sql(my_insert_stmt).collect()
        #st.success('Your Smoothie is ordered!', icon="✅")
        st.success('Your Smoothie is ordered, ' + name_on_order + '!', icon="✅")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#st.text(fruityvice_response.json())
fd_df = st.dataframe(data=fruityvice_response.json(),use_container_widh=True)

