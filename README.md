# Demo

# Media Maven App

The **Media Maven App** is a user-friendly web application built using Python, Streamlit, HTML, and JavaScript. This app leverages the power of the TMDB (The Movie Database) API to provide movie recommendations similar to a particular movie.

## Installation

To run the Media Maven App locally, follow these steps:


1. **Install the required Python packages:**
    ```
    pip install -r requirements.txt
    ```
   
2. **Obtain a TMDB API Key:**
    - Sign up on the [TMDB website](https://www.themoviedb.org/) to get your API key.
    - Put your TMDB API key inside links in `details.html`, `index.html`, and `app.py` where `{your_api_key}` appears.

3. **Generate Similarity Data:**
    - Run the code segments in the `movies_recommendation.ipynb` notebook to generate a file named `similarity.pkl`.

4. **Run the App:**
    ```
    streamlit run app.py
    ```

Visit `http://localhost:8501` in your web browser to use the Media Maven App locally.

## Features

- **Search:** Enter the title of a movie you enjoyed, and the app will retrieve relevant information about that movie.

- **Recommendations:** Based on the selected movie, the app queries the TMDB API to find similar movies, taking into consideration various attributes such as genre, cast, and plot.

- **Details:** View detailed information about each recommended movie, including its title, release date, synopsis, cast, and more.

- **Watchlist:** Create a watchlist of movies you're interested in watching later. You can easily add and remove movies from your watchlist.

- **Responsive Design:** The app is designed to be responsive and user-friendly on both desktop and mobile devices.

## Technologies Used

- **Python:** The backend of the app is built using Python, including the logic for querying the TMDB API and generating recommendations.

- **Streamlit:** The user interface is created using Streamlit, a Python library for building interactive web applications.

- **HTML and JavaScript:** HTML and JavaScript are used to enhance the user interface and provide additional interactivity.

- **TMDB API:** The app utilizes the TMDB API to retrieve movie information and recommendations. The API provides data about movies, including details like cast, genres, and more.

## Contact

If you have any questions, suggestions, or issues, please feel free to contact me at selfmanish01@gmail.com.

---

Enjoy discovering new movies with the Media Maven App!

*Disclaimer: The Media Maven App is a project developed for educational and personal purposes and is not affiliated with TMDB or any movie production company.*
