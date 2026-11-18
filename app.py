
from flask import Flask, render_template, request
import pickle
import re

app = Flask(__name__)

# Load movie dataset
with open("movies.pkl", "rb") as file:
    movies = pickle.load(file)

# Load similarity matrix
with open("similarity.pkl", "rb") as file:
    similarity = pickle.load(file)

movies = movies.reset_index(drop=True)

# Get all movie titles
all_movies = sorted(
    movies["title"].dropna().astype(str).unique().tolist()
)


# Normalize movie names for flexible searching
def normalize_title(title):
    return re.sub(r"[^a-z0-9]", "", str(title).lower())


# Movie recommendation function
def recommend(movie_title):

    movie_index = movies[movies["title"] == movie_title].index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        enumerate(distances),
        key=lambda x: x[1],
        reverse=True
    )

    recommendations = []

    for index, score in movie_list:

        # Skip the selected movie
        if index == movie_index:
            continue

        recommendations.append(movies.iloc[index]["title"])

        if len(recommendations) == 5:
            break

    return recommendations


@app.route("/", methods=["GET", "POST"])
def home():

    search_query = ""
    search_results = []
    searched = False

    selected_movie = ""
    recommendations = []

    message = ""

    if request.method == "POST":

        action = request.form.get("action")

        # SEARCH MOVIES
        if action == "search":

            search_query = request.form.get("search", "").strip()
            searched = True

            if search_query:

                normalized_query = normalize_title(search_query)

                search_results = [
                    movie for movie in all_movies
                    if normalized_query in normalize_title(movie)
                ]

                if not search_results:
                    message = "No matching movies found."

            else:
                message = "Please enter a movie name."

        # RECOMMEND MOVIES
        elif action == "recommend":

            selected_movie = request.form.get("movie", "")

            if selected_movie in all_movies:

                recommendations = recommend(selected_movie)

            else:
                message = "Please select a valid movie."

    return render_template(
        "index.html",
        all_movies=all_movies,
        search_query=search_query,
        search_results=search_results,
        searched=searched,
        selected_movie=selected_movie,
        recommendations=recommendations,
        message=message
    )


if __name__ == "__main__":
    app.run(debug=True)
