#  Movie Recommendation System (Content-Based)

This project is a simple movie recommender system built using Python and Streamlit. It suggests movies similar to the one you select based on content (like genres, keywords, cast, etc.).

##  Features

* Select a movie from dropdown
* Get top 5 similar movie recommendations
* Displays movie posters using TMDB API
* Fast and lightweight UI using Streamlit

##  Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn (for similarity)
* Streamlit (for UI)
* TMDB API (for posters)

## 📂Project Structure

```
├── app.py                 # Main Streamlit app
├── movies.pkl            # Movie data
├── similarity.pkl        # Similarity matrix
├── requirements.txt      # Dependencies
```

##  How It Works

* Movie dataset is preprocessed
* Important features are combined into a single tag
* Tags are vectorized using CountVectorizer
* Cosine similarity is calculated between movies
* Top similar movies are recommended

##  Run Locally

1. Clone the repo

```
git clone <your-repo-link>
cd movie-recommender
```

2. Install dependencies

```
pip install -r requirements.txt
```

3. Run the app

```
streamlit run app.py
```

##  API Setup

* Get API key from TMDB
* Replace it in your code:

```
api_key = "YOUR_API_KEY"
```

##  Common Issues

* **Images not loading** → Check API key or internet connection
* **Connection timeout error** → Retry or add timeout in requests
* **poster_path error** → Handle missing values in API response

##  Future Improvements

* Add search instead of dropdown
* Improve UI/UX
* Add collaborative filtering
* Deploy on cloud (Streamlit Cloud / Render)

##  Note

This is a beginner-friendly project to understand recommendation systems and working with APIs.

---

Made while learning and experimenting 🚀
