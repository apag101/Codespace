#source chatgpt query: https://chatgpt.com/g/g-cKXjWStaE-python/c/6771764a-f868-8011-b69f-92b5049f5050

import pandas as pd
import numpy as np
from faker import Faker

# Initialize Faker for generating mock data
fake = Faker()

# Generate mock product review data
def generate_mock_reviews(num_reviews=1000):
    reviews = []
    for _ in range(num_reviews):
        reviews.append({
            "review_id": fake.uuid4(),  # Unique review ID
            "review_text": fake.text(max_nb_chars=200),  # Random review text
            "rating": np.random.randint(1, 6),  # Ratings between 1 and 5
            "timestamp": fake.date_time_this_year()  # Random timestamp from this year
        })
    return pd.DataFrame(reviews)

# Generate 1000 mock reviews
mock_reviews = generate_mock_reviews(1000)

# Display a sample of the mock reviews
print(mock_reviews.head())


from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Download necessary NLTK data
nltk.download('vader_lexicon')

# Initialize VADER Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

# Function to analyze sentiment
def analyze_sentiment(text):
    sentiment = sia.polarity_scores(text)
    if sentiment['compound'] >= 0.05:
        return 'positive'
    elif sentiment['compound'] <= -0.05:
        return 'negative'
    else:
        return 'neutral'

# Apply sentiment analysis to the review_text
mock_reviews['sentiment'] = mock_reviews['review_text'].apply(analyze_sentiment)

# Display sentiment distribution
sentiment_distribution = mock_reviews['sentiment'].value_counts()

from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Download necessary NLTK data
nltk.download('vader_lexicon')

# Initialize VADER Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

# Function to analyze sentiment
def analyze_sentiment(text):
    sentiment = sia.polarity_scores(text)
    if sentiment['compound'] >= 0.05:
        return 'positive'
    elif sentiment['compound'] <= -0.05:
        return 'negative'
    else:
        return 'neutral'

# Apply sentiment analysis to the review_text
mock_reviews['sentiment'] = mock_reviews['review_text'].apply(analyze_sentiment)

# Display sentiment distribution
sentiment_distribution = mock_reviews['sentiment'].value_counts()

import matplotlib.pyplot as plt
from collections import Counter
import string
from nltk.corpus import stopwords
import nltk

# Download stopwords
nltk.download('stopwords')

# Define stopwords and punctuation
stop_words = set(stopwords.words('english'))
punctuation = set(string.punctuation)

# Function to preprocess text
def preprocess_text(text):
    # Convert to lowercase and tokenize
    words = text.lower().split()
    # Remove stopwords and punctuation
    words = [word for word in words if word not in stop_words and word not in punctuation]
    return words

# Extract keywords for positive and negative reviews
positive_reviews = mock_reviews[mock_reviews['sentiment'] == 'positive']['review_text']
negative_reviews = mock_reviews[mock_reviews['sentiment'] == 'negative']['review_text']

# Tokenize and preprocess reviews
positive_keywords = preprocess_text(" ".join(positive_reviews))
negative_keywords = preprocess_text(" ".join(negative_reviews))

# Count word frequencies
positive_word_counts = Counter(positive_keywords).most_common(10)
negative_word_counts = Counter(negative_keywords).most_common(10)

# Function to create bar charts for word frequencies
def plot_word_frequencies(word_counts, title):
    words, counts = zip(*word_counts)
    plt.figure(figsize=(10, 6))
    plt.bar(words, counts, color='skyblue' if 'Positive' in title else 'salmon')
    plt.title(title, fontsize=16)
    plt.xlabel('Words', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.xticks(rotation=45, fontsize=12)
    plt.show()

# Plot word frequencies for positive and negative reviews
plot_word_frequencies(positive_word_counts, 'Top Keywords in Positive Reviews')
plot_word_frequencies(negative_word_counts, 'Top Keywords in Negative Reviews')

# Visualize sentiment distribution
def plot_sentiment_distribution(distribution):
    distribution.plot(kind='bar', color=['gray', 'blue', 'red'], figsize=(8, 5))
    plt.title('Sentiment Distribution', fontsize=16)
    plt.xlabel('Sentiment', fontsize=14)
    plt.ylabel('Number of Reviews', fontsize=14)
    plt.xticks(rotation=0, fontsize=12)
    plt.show()

plot_sentiment_distribution(mock_reviews['sentiment'].value_counts())
