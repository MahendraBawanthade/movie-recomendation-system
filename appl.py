import numpy as np
import pandas as pd
import pickle
import streamlit as st
from PIL import Image
import base64


def recommend(movie):
  movie_index=movies[movies['title']==movie].index[0]

  distances=similarity[movie_index]
  movie_list= sorted(list(enumerate(distances)), reverse=True,key=lambda x:x[1])[1:6]

  recommended_movies=[]
  for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
  return recommended_movies
movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

selected_movie_name= st.selectbox(
    'MOVIE NAME HERE?',
movies['title'].values)

if st.button('recommend'):
   recommendations= recommend(selected_movie_name)
   for i in recommendations:
       st.write(i)

import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('2772922.png')
st.title(':white[_SASTA NETFLIX_]')
st.snow()
