import streamlit as st
import pickle
import pandas as pd
import os

# Loading the similarity matrix
similarity = pickle.load(open("Models\similarity.pkl", "rb"))

# Loading the movies dataframe
movies = pickle.load(open("Models\movies.pkl", "rb"))

# Recommendation Functions
def recommend(movie, n=5):
    if movie not in movies['title'].values:
        return [f"There is no movie named '{movie}' in the dataset. Search for some other movie..."]

    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),
                       reverse=True, key=lambda x: x[1])
    recommended_movies = []
    for i in distances[1:n+1]:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


def recommend_by_tags(tags, n=5):
    # Converting input tags to lowercase for better matching
    input_tags = tags.lower()

    # Calculating similarity scores for all movies based on tags
    tag_scores = []
    for idx, movie_tags in enumerate(movies['tag']):
        if not movie_tags:
            score = 0
        else:
            movie_tags_lower = ' '.join(movie_tags).lower()
            input_words = set(input_tags.split())
            movie_words = set(movie_tags_lower.split())
            score = len(input_words.intersection(movie_words))
        tag_scores.append((idx, score))

    # Sorting by similarity score in descending order
    tag_scores = sorted(tag_scores, key=lambda x: x[1], reverse=True)

    recommended_movies = []
    count = 0
    for idx, score in tag_scores:
        if score > 0 and count < n:
            recommended_movies.append(movies.iloc[idx]['title'])
            count += 1
        if count == n:
            break

    if count == 0:
        return [f"No movies found matching this '{tags}' feature! Search for some other feature..."]

    return recommended_movies

# Streamlit UI
st.title("Movie Recommendation System")

# Selecting recommendation type
option = st.selectbox(
    "Choose Recommendation Type:",
    ["Movie Name", "Genres", "Director", "Cast", "Keyword"]
)

# Input fields
feature_input = st.text_input(f"Enter {option}:")
n_recommendations = st.number_input(
    "Enter number of recommendations:", min_value=1, max_value=50, value=5
)

# Recommendation button
if st.button("Recommend"):
    if option == "Movie Name":
        results = recommend(feature_input, n=n_recommendations)
    else:
        results = recommend_by_tags(feature_input, n=n_recommendations)

    # If results contain only one item and it starts with an error message
    if len(results) == 1 and ("no movie" in results[0].lower() or "no movies found" in results[0].lower()):
        st.error(results[0])  # Show only the message as error
    else:
        st.subheader("Recommended Movies:")
        for idx, movie in enumerate(results, start=1):
            st.write(f"{idx}. {movie}")

