# Movies Recommendation System 🎬

A content-based movie recommendation system with an interactive **Streamlit web interface**. Built using the TMDB 5000 Movies dataset, this application analyzes movie data and provides personalized recommendations based on content similarity.

## 📁 Project Structure

```
movies_recommendation_system/
├── app.py                              # Streamlit web application
├── requirements.txt                    # Project dependencies
├── Notebooks/
│   ├── Movies_EDA.ipynb               # Exploratory Data Analysis
│   └── Movies_Recommendation_Model.ipynb  # Recommendation Model Implementation
├── Models/
│   ├── similarity.pkl                 # Pre-computed similarity matrix
│   └── movies.pkl                     # Processed movies dataframe
└── Data/
    ├── tmdb_5000_movies.csv          # Movies dataset (not included in repo)
    └── tmdb_5000_credits.csv         # Credits dataset (not included in repo)
```

## 📊 Dataset

The project uses the **TMDB 5000 Movies Dataset** which contains:
- **~4,800 movies** from The Movie Database (TMDb)
- **20 features** including budget, genres, keywords, cast, crew, overview, popularity, revenue, runtime, and more
- **JSON-formatted columns** for genres, keywords, cast, and crew

### Key Features:
- `budget`: Movie production budget
- `genres`: Movie genres (Action, Comedy, Drama, etc.)
- `keywords`: Plot keywords and themes
- `cast`: Top 3 cast members
- `crew`: Director information
- `overview`: Movie plot summary
- `revenue`: Box office revenue
- `vote_average` & `vote_count`: User ratings

## 🔍 Exploratory Data Analysis

The `Notebooks/Movies_EDA.ipynb` notebook includes comprehensive data analysis:

### Data Preprocessing
- Merged movies and credits datasets
- Parsed JSON columns (genres, keywords, cast, crew)
- Handled missing values
- Extracted director information from crew data
- Limited cast to top 3 actors per movie

### Visualizations
1. **Budget vs Revenue Analysis**: Scatter plot showing relationship between production budget and box office revenue
2. **Genre-wise Profit Analysis**: Bar chart displaying average profit margins across different genres
3. **Top Movies by Profit**: Visualization of highest-grossing movies
4. **Distribution Analysis**: Statistical analysis of movie features

### Key Insights
- Identified correlation between budget and revenue
- Analyzed genre profitability patterns
- Discovered top-performing movies and directors

## 🤖 Recommendation System

The `Notebooks/Movies_Recommendation_Model.ipynb` implements a **content-based filtering** approach:

### Methodology

1. **Feature Engineering**
   - Created a combined "tag" feature by concatenating:
     - Movie overview
     - Genres
     - Keywords
     - Cast (top 3 actors)
     - Crew (director)

2. **Text Processing**
   - Used `CountVectorizer` from scikit-learn
   - Parameters:
     - `max_features=10000`: Top 10,000 most frequent words
     - Stop words removal for better accuracy
     - Lowercase conversion for consistency

3. **Similarity Calculation**
   - Computed **cosine similarity** matrix between all movies
   - Measures content similarity based on movie features
   - Pre-computed matrix for fast real-time recommendations

4. **Recommendation Functions**
   - `recommend(movie, n=5)`: Get similar movies based on movie title
   - `recommend_by_tags(tags, n=5)`: Get movies matching specific features (genres, cast, director, keywords)

### Model Serialization
- Saved similarity matrix: `Models/similarity.pkl`
- Saved processed dataframe: `Models/movies.pkl`
- Enables quick loading without reprocessing

## 🌐 Web Application (Streamlit)

The `app.py` file provides an **interactive web interface** with the following features:

### Features
✅ **Multiple Recommendation Types:**
   - Search by **Movie Name**: Find similar movies to one you already love
   - Search by **Genres**: Discover movies by genre (Action, Comedy, Drama, etc.)
   - Search by **Director**: Find movies by your favorite directors
   - Search by **Cast**: Explore movies featuring specific actors
   - Search by **Keyword**: Find movies matching plot themes

✅ **Customizable Results**: Choose number of recommendations (1-50)

✅ **User-Friendly Interface**: 
   - Clean dropdown selection for recommendation type
   - Text input for search queries
   - Number slider for result count
   - Error handling for invalid inputs
   - Organized display of recommendations

### UI Components
- **Title Header**: "Movie Recommendation System"
- **Dropdown Menu**: Select recommendation type
- **Text Input**: Enter movie name or feature
- **Number Input**: Specify number of recommendations
- **Recommend Button**: Trigger the recommendation engine
- **Results Display**: Numbered list of recommended movies

## 🛠️ Technologies Used

- **Python 3.11+**
- **Streamlit**: Interactive web application framework
- **pandas**: Data manipulation and analysis
- **matplotlib**: Data visualization
- **scikit-learn**: Machine learning (CountVectorizer, cosine_similarity)
- **pickle**: Model serialization
- **tqdm**: Progress bars for data processing

## 🚀 Getting Started

### Prerequisites

- Python 3.11 or higher
- pip package manager

### Installation

1. **Clone the repository:**
```bash
git clone <repository-url>
cd movies_recommendation_system
```

2. **Create and activate virtual environment:**

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install required dependencies:**
```bash
pip install -r requirements.txt
```

4. **Download the dataset:**
   - Download TMDB 5000 Movies dataset
   - Place `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv` in the `Data/` folder

5. **Build the model (if Models folder is empty):**
   - Open and run `Notebooks/Movies_EDA.ipynb` for data exploration
   - Open and run `Notebooks/Movies_Recommendation_Model.ipynb` to generate the model files
   - This will create `similarity.pkl` and `movies.pkl` in the `Models/` folder

6. **Launch the Streamlit app:**
```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

### Usage

#### **Option 1: Search by Movie Name**
```
1. Select "Movie Name" from dropdown
2. Enter: "Avatar"
3. Click "Recommend"
Output: Similar movies like 'Aliens', 'Alien³', 'Guardians of the Galaxy', etc.
```

#### **Option 2: Search by Genre**
```
1. Select "Genres" from dropdown
2. Enter: "action thriller"
3. Set number of recommendations: 10
4. Click "Recommend"
Output: Top 10 action thriller movies
```

#### **Option 3: Search by Director**
```
1. Select "Director" from dropdown
2. Enter: "Christopher Nolan"
3. Click "Recommend"
Output: Movies directed by Christopher Nolan
```

#### **Option 4: Search by Cast**
```
1. Select "Cast" from dropdown
2. Enter: "Tom Hanks"
3. Click "Recommend"
Output: Movies featuring Tom Hanks
```

#### **Option 5: Search by Keyword**
```
1. Select "Keyword" from dropdown
2. Enter: "space adventure"
3. Click "Recommend"
Output: Movies with space adventure themes
```

## 📦 Dependencies

```
pandas          # Data manipulation
matplotlib      # Data visualization
scikit-learn    # Machine learning algorithms
streamlit       # Web application framework
tqdm            # Progress bars
```



## 🎯 Key Features

✅ **Content-based filtering** for personalized recommendations  
✅ **Interactive Streamlit web interface** with multiple search options  
✅ **Comprehensive EDA** with multiple visualizations  
✅ **Robust data preprocessing** (JSON parsing, missing value handling)  
✅ **Fast recommendation generation** using pre-computed similarity  
✅ **Tag-based search functionality** (genres, cast, director, keywords)  
✅ **Error handling** for invalid inputs  
✅ **Customizable result count** (1-50 recommendations)  
✅ **User-friendly design** with clean UI/UX  

## 📝 Future Enhancements

- [ ] Add **movie posters** and **ratings** to recommendations
- [ ] Implement **collaborative filtering** for hybrid approach
- [ ] Include **user reviews** and **sentiment analysis**
- [ ] Add **movie trailers** integration (YouTube API)
- [ ] Deploy to **Heroku/Streamlit Cloud** for public access
- [ ] Implement **user authentication** and **watchlist** features
- [ ] Add **filtering options** (year, rating, duration)
- [ ] Include **trending movies** section with real-time updates
- [ ] Implement **A/B testing** for recommendation quality
- [ ] Add **export functionality** (CSV/PDF download)



## ⚠️ Important Notes

1. **Dataset**: The `Data/` folder is not included in the repository due to file size. Download the TMDB 5000 dataset separately.
2. **Virtual Environment**: The `venv/` folder is excluded from version control. Create your own virtual environment locally.
3. **Model Files**: The `Models/` folder should contain pre-built model files. If missing, run the notebooks to generate them.

---
