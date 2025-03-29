import streamlit as st
import requests

def get_news(api_key, query):
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={api_key}'
    response = requests.get(url)
    return response.json()

def main():
    st.title('News Fetcher App')

    api_key = f'57e04e84451a466f93ce585df3066235'

    query = st.text_input('Enter the type of news you want (e.g., technology, sports)')

    if st.button('Get News'):
        if api_key and query:
            news_data = get_news(api_key, query)
            if news_data.get('status') == 'ok':
                articles = news_data.get('articles')
                for article in articles:
                    st.subheader(article['title'])
                    st.write(article['description'])
                    st.write(f"Source: {article['source']['name']}")
                    st.write(f"Published At: {article['publishedAt']}")
                    st.write(f"[Read more]({article['url']})")
                    st.write("---")
            else:
                st.error("Failed to fetch news articles. Please check your API key and query.")
        else:
            st.error("Please provide both an API key and a query.")

if __name__ == "__main__":
    main()