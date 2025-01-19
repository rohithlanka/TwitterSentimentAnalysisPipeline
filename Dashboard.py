import boto3
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from collections import Counter

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
TABLE_NAME = 'tweetsrealtimetable'

def fetch_data():
    table = dynamodb.Table(TABLE_NAME)
    response = table.scan()
    return response['Items']

def visualize_sentiment_distribution(data):
    sentiments = [item['detected_sentiment'] for item in data]
    sentiment_counts = Counter(sentiments)
    
    plt.figure(figsize=(8, 5))
    sns.barplot(x=list(sentiment_counts.keys()), y=list(sentiment_counts.values()), palette='viridis')
    plt.title('Sentiment Distribution')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.show()

def visualize_gender_distribution(data):
    genders = [item['gender'] for item in data]
    gender_counts = Counter(genders)
    
    plt.figure(figsize=(7, 7))
    plt.pie(gender_counts.values(), labels=gender_counts.keys(), autopct='%1.1f%%', startangle=140, colors=['skyblue', 'lightgreen', 'salmon'])
    plt.title('Tweet Gender Analysis')
    plt.show()

def visualize_top_regions(data):
    regions = [item['region'] for item in data]
    region_counts = Counter(regions).most_common(10)  # Top 10 regions
    
    plt.figure(figsize=(7, 7))
    labels, sizes = zip(*region_counts)
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
    plt.title('Top 10 Tweet Regions')
    plt.show()

def visualize_age_vs_sentiment(data):
    df = pd.DataFrame(data)
    plt.figure(figsize=(8, 6))
    sns.countplot(x='age_range', hue='detected_sentiment', data=df, order=['18-25', '26-35', '36-45', '46-60'], palette='coolwarm')
    plt.title('Age Range vs Sentiment')
    plt.xlabel('Age Range')
    plt.ylabel('Count')
    plt.legend(title='Sentiment')
    plt.show()

def visualize_sentiment_vs_gender(data):
    df = pd.DataFrame(data)
    plt.figure(figsize=(8, 6))
    sns.countplot(x='gender', hue='detected_sentiment', data=df, palette='viridis')
    plt.title('Sentiment vs Gender')
    plt.xlabel('Gender')
    plt.ylabel('Count')
    plt.legend(title='Sentiment')
    plt.show()

def visualize_top_region_sentiment_heatmap(data):
    df = pd.DataFrame(data)
    top_regions = df['region'].value_counts().nlargest(10).index
    filtered_df = df[df['region'].isin(top_regions)]
    pivot_table = pd.crosstab(filtered_df['region'], filtered_df['detected_sentiment'])
    
    plt.figure(figsize=(10, 6))
    sns.heatmap(pivot_table, annot=True, cmap='YlGnBu')
    plt.title('Top 10 Regions vs Sentiment')
    plt.xlabel('Sentiment')
    plt.ylabel('Region')
    plt.show()

if __name__ == "__main__":
    data = fetch_data()
    visualize_sentiment_distribution(data)
    visualize_gender_distribution(data)
    visualize_top_regions(data)
    visualize_age_vs_sentiment(data)
    visualize_sentiment_vs_gender(data)
    visualize_top_region_sentiment_heatmap(data)
