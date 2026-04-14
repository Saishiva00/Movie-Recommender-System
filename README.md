# Movie Recommender System 🎬

I built this project to get hands-on with how recommendation engines actually work under the hood — not just calling some library and calling it a day, but understanding the math and NLP behind why two movies are considered "similar."

The result is a web app where you pick any movie from the TMDB dataset and instantly get 5 recommendations based on what that movie is actually about — its cast, genre, crew, keywords, and plot.

---

## What it does

- Takes a movie title as input
- Computes similarity against 4,800+ movies using NLP-based feature vectors
- Returns the top 5 most similar movies
- Runs as an interactive web app via Streamlit

No user ratings needed. No login. Just pick a movie and see what comes up.

---

## How it works

The core idea is content-based filtering. Each movie gets converted into a "tag" — a single block of text made up of its genres, top cast members, director, plot keywords, and overview. These tags are then vectorized using scikit-learn's `CountVectorizer` and compared using cosine similarity.

At inference time, the app just looks up which movies scored highest on that similarity matrix for the selected title.

```
TMDB CSVs (movies + credits)
        ↓
Merge on title, select relevant columns
        ↓
Parse JSON columns (genres, cast, crew, keywords)
        ↓
Build unified tags per movie
        ↓
Stem words using NLTK PorterStemmer
        ↓
CountVectorizer → sparse matrix (5000 features)
        ↓
Cosine Similarity matrix (4806 × 4806)
        ↓
Serialize → movies_dict.pkl + similarity.pkl
        ↓
Streamlit app loads artifacts → serves recommendations
```

---

## Tech Stack

- **Python** — core language
- **pandas / numpy** — data processing
- **scikit-learn** — CountVectorizer, cosine similarity
- **NLTK** — PorterStemmer for text normalization
- **Streamlit** — web UI
- **pickle / gdown** — artifact serialization and loading
- **Dataset** — [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) from Kaggle

---

## Project Structure

```
Movie-Recommender-System/
├── Movie_Recommender_system.ipynb   # full ML pipeline — EDA, feature eng, model building
├── app.py                           # Streamlit app
├── movies_dict.pkl                  # serialized movie data (titles, tags, IDs)
├── requirements.txt                 # dependencies
└── .devcontainer/                   # Codespaces config
```

The `similarity.pkl` file (~175MB) is too large for GitHub so it lives on Google Drive and gets pulled at runtime via `gdown`.

---

## Running it locally

**1. Clone the repo**
```bash
git clone https://github.com/Saishiva00/Movie-Recommender-System.git
cd Movie-Recommender-System
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Get the dataset**

Download both files from Kaggle and place them in the root folder:
- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

[TMDB 5000 Dataset on Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

**4. Run the notebook**

Open `Movie_Recommender_system.ipynb` and run all cells. This generates `movies_dict.pkl` and `similarity.pkl`.

**5. Launch the app**
```bash
streamlit run app.py
```

The app opens at `http://localhost:8501`

---

## Screenshots

*Coming soon — will add once deployed.*

---

## What I'd improve next

- Pull movie posters from the TMDB API to make results more visual
- Pin dependency versions in `requirements.txt` for stability
- Add `@st.cache_data` so the similarity matrix doesn't reload on every interaction
- Host `similarity.pkl` on Hugging Face Hub instead of Google Drive (more reliable)
- Write unit tests for the `recommend()` function
- Deploy to Streamlit Cloud with a public link

---

## Dataset

TMDB 5000 Movie Dataset — https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

---

Built by [Saishiva](https://github.com/Saishiva00)
