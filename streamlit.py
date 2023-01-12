import streamlit as st
import pandas as pd
import seaborn as sns

st.title ('Movies')

movies = sns.load_dataset("movies")

option = st.selectbox('What do you want?', ('Saw', 'TexasChainSaw', 'WrongTurn'))

with st.expander('MOVIES'):
    st.table(movies[movies.type == option])
    
col1, col2, col3 = st.columns(3)

with col1:
    st.image('saw.jpeg', caption = 'Saw')
with col2:
    st.image('texaschainsaw.jpeg', caption = 'TexasChainSaw')
with col3:
    st.image('wrongturn.jpeg', caption = 'WrongTurn')

#new_text = st.text_input('Movie title')
#test1 = st.text('This is some text.')
#test1.body = new_text
#st.write('The current movie title is', text1.body)

