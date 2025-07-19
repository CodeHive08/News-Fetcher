markdown

# News Fetcher App


A simple Streamlit application that allows users to fetch news articles based on their interests. Users can input a news category (e.g., technology, sports, health) and receive relevant news articles from the NewsAPI.
you can see the preview of the website here:https://newsfetcherz.streamlit.app/

## Features


- User-friendly interface to input news preferences.

- Fetches and displays news articles from the NewsAPI.

- Displays article title, description, source, and publication date.

- Provides a link to read the full article.


## Technologies Used


- [Streamlit](https://streamlit.io/) - A Python library for creating web applications.

- [Requests](https://docs.python-requests.org/en/master/) - A simple HTTP library for Python to make API calls.

- [NewsAPI](https://newsapi.org/) - A service to get news articles from various sources.


## Prerequisites


- Python 3.6 or higher

- A NewsAPI key (you can get one by signing up at [NewsAPI](https://newsapi.org/))


## Installation


1. Clone the repository:

   ```

   git clone https://github.com/CodeHive08/news-fetcher-app.git

   cd news-fetcher-app
```
    Create a virtual environment (optional but recommended):

```
    bash

python -m venv venv

source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install the required packages:
```
bash

pip install -r requirements.txt
```

Run the Streamlit app:
```
bash

    streamlit run news_app.py
````
    Open your web browser and go to http://localhost:8501 to view the app.

Usage

    Enter your NewsAPI key in the input field.
    Specify the type of news you want (e.g., technology, sports).
    Click the "Get News" button to fetch and display the news articles.

License

This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgments

    Streamlit for providing an easy way to create web applications.
    NewsAPI for providing access to news articles from various sources.

