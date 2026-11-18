# Movie Recommender System

A content-based movie recommendation web application built using Python and Machine Learning. The system recommends movies similar to a user's selected movie based on movie metadata such as genres, keywords, cast, crew, and overview.

## Project Overview

With thousands of movies available across different platforms, finding movies that match a user's interests can be challenging.

This project addresses that problem using a **Content-Based Recommendation System**. It analyzes movie information, converts textual features into numerical vectors, and calculates similarity scores to identify movies with similar characteristics.

Users can search for a movie by its title and receive recommendations for similar movies through a simple web interface.

## Dataset

**Dataset:** TMDB 5000 Movie Dataset

**Source:** [TMDB 5000 Movie Dataset – Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

##  Methodology

The project follows a Content-Based Filtering approach.

### 1. Data Loading and Preprocessing

- Load the movie datasets using Pandas.
- Merge relevant movie information.
- Handle missing values.
- Extract useful features such as genres, keywords, cast, director, and overview.

### 2. Feature Engineering

Combine the selected movie attributes into a single textual feature called `tags`.

### 3. Text Preprocessing

- Remove unnecessary spaces and formatting.
- Apply stemming to normalize similar words.
- Prepare textual data for feature extraction.

### 4. Feature Extraction

Use **CountVectorizer** to convert movie tags into numerical vectors.

### 5. Similarity Calculation

Use **Cosine Similarity** to calculate how similar movies are based on their numerical representations.

### 6. Recommendation Generation

When a user searches for a movie, the system identifies its similarity scores with other movies and returns the top 5 similar movies.

##  Machine Learning Concepts Used

| Concept | Purpose |
|---|---|
| Content-Based Filtering | Recommends movies based on their features |
| Text Preprocessing | Cleans and prepares textual data |
| Stemming | Reduces words to their root forms |
| CountVectorizer | Converts text into numerical vectors |
| Cosine Similarity | Measures similarity between movie vectors |

##  Technology Stack

- **Programming Language:** Python
- **Web Framework:** Flask
- **Data Processing:** Pandas, NumPy
- **Machine Learning:** Scikit-learn
- **Text Processing:** NLTK
- **Frontend:** HTML, CSS
- **Version Control:** Git and GitHub

## Application Features

- Search movies using a search box.
- Search using simplified movie titles.
- Find movies without requiring exact title formatting.
- Receive five similar movie recommendations.
- Simple and user-friendly web interface.
- Content-based movie recommendation functionality.

##  Project Structure

```text
movie_recommender_system/
│
├── app.py
├── model.py
├── requirements.txt
├── README.md
│
├── data/
│   └── dataset_source.md
│
├── models/
│
├── screenshots/
│   ├── home.png
│   └── recommendations.png
│
└── .gitignore
```

## Results and Key Observations

- The system identifies similar movies using their textual metadata.
- Movies sharing similar genres, keywords, cast, crew, and descriptions can receive higher similarity scores.
- Content-Based Filtering does not require user ratings or historical user interactions.
- Recommendation quality depends on the quality and availability of movie metadata.

## Real-World Applications

Similar recommendation techniques are used in:

- Movie and entertainment discovery platforms.
- Music recommendation applications.
- E-commerce product recommendations.
- Personalized content discovery systems.

##  Limitations and Future Improvements

- Recommendation quality depends on available movie metadata.
- The system may not capture individual user preferences.
- It can struggle with movies having limited information.
- A hybrid recommendation approach could be explored in the future.
- User ratings and feedback could be incorporated to improve personalization.

## Author

**Rahul Pathak**

GitHub: [rahul-pathak-12-bot](https://github.com/rahul-pathak-12-bot)

---
