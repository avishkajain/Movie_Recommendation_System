import  streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    import requests

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=f4532bba4057aee40619725e9e963d16&language=en-US"
    data = requests.get(url).json()

    if data.get("poster_path"):
        return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]
    else:
        return "https://via.placeholder.com/500x750?text=No+Image"



def recommend(movie):
    movie_index = movies_list[movies_list["title"] == movie].index[0]# movie ka index fetch karo#masking this is
    distances = similarity[movie_index]  # uss movie ka vector
    movis= sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    # taki lists ka index barkaraar rahe so enumerate 0 th nhi 1 st index top 5 aur ascending false
    recommended_movies=[]
    recommended_movies_poster=[]
    for i in movis:
        movie_id=movies_list.iloc[i[0]].movie_id
        recommended_movies.append(movies_list.iloc[i[0]].title)
        #fetch posture


        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster
similarity=pickle.load(open("similarity.pkl","rb"))
movies_dict=pickle.load(open("movies.pkl","rb"))
movies_list=pd.DataFrame(movies_dict)
#movies_list=movies_list["title"].values#directly variable mein assign nhi kar sakte list banta
st.title("AVISHKA'S MOVIE RECOMMENDATION SYSTEM")
selected_movie_name=st.selectbox(
"Select Movie"
,movies_list["title"].values
)
if st.button(" Recommend"):
    names,postures=recommend(selected_movie_name)
    col1,col2,col3,col4,col5= st.columns(5)

    with  col1:
        st.text(names[0])
        st.image(postures[0])

    with  col2:
        st.text(names[1])
        st.image(postures[1])
    with  col3:
        st.text(names[2])
        st.image(postures[2])

    with  col4:
        st.text(names[3])
        st.image(postures[3])
    with  col5:
        st.text(names[4])
        st.image(postures[4])