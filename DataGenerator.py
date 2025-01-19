import boto3
import pandas as pd
import json
import time
from faker import Faker
import random
import uuid
from datetime import datetime, timedelta

fake = Faker()
kinesis = boto3.client('kinesis', region_name='us-east-1')

# Load your dataset
df = pd.read_csv('Twitter_Data.csv')  # Ensure Twitter_data.csv is in the working directory

# Define the age ranges and genders
age_ranges = ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']
genders = ['Male', 'Female', 'Non-binary']

# Define the timeframe for random timestamps
start_time = datetime(2023, 1, 1)  # Example start date
end_time = datetime(2023, 12, 31)  # Example end date

# Function to generate a random timestamp within the timeframe
def get_random_timestamp(start, end):
    delta = end - start
    random_seconds = random.randint(0, int(delta.total_seconds()))
    return (start + timedelta(seconds=random_seconds)).isoformat()

# Function to send tweets to Kinesis stream
def send_tweets_to_kinesis():
    print("starting to send")
    for index, row in df.iterrows():
        print(f"index: {index}")
        tweet_data = {
            'id': str(uuid.uuid4()),  # Generate a unique ID for each tweet
            'text': row['clean_text'],
            'username': fake.user_name(),
            'age_range': random.choice(age_ranges),
            'gender': random.choice(genders),
            'region': fake.country(),
            'timestamp': get_random_timestamp(start_time, end_time)  # Generate random timestamp
        }
        # Send data to Kinesis stream
        kinesis.put_record(
            StreamName='SocialMediaDataStream',
            Data=json.dumps(tweet_data),
            PartitionKey=tweet_data['timestamp']
        )
        print(f"Sent: {tweet_data}")
        time.sleep(1.0)

if __name__ == "__main__":
    send_tweets_to_kinesis()