import base64
import boto3
import json
import os
from datetime import datetime
from decimal import Decimal

comprehend = boto3.client('comprehend')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('tweetsrealtimetable') 

def lambda_handler(event, context):
    for record in event['Records']:
        encoded_data = record['kinesis']['data']
        decoded_data = base64.b64decode(encoded_data).decode('utf-8')
        payload = json.loads(decoded_data)
        
        tweet_text = payload['text']
        username = payload['username']
        age_range = payload['age_range']
        gender = payload['gender']
        region = payload['region']
        
        #label = payload['label']
        
        sentiment_response = comprehend.detect_sentiment(
            Text=tweet_text,
            LanguageCode='en'
        )
        
        sentiment = sentiment_response['Sentiment']
        sentiment_score = {
            key: Decimal(str(value)) for key, value in sentiment_response['SentimentScore'].items()
        }
        
        item = {
            'id': payload['id'],
            'tmstmp' : payload['timestamp'],
            'username': username,
            'tweet': tweet_text,
            'age_range': age_range,
            'gender': gender,
            'region': region,
            'detected_sentiment': sentiment,
            'sentiment_score': sentiment_score

        }
        
        table.put_item(Item=item)
        
        print(f"Processed tweet by {username}: {sentiment}")
        
    return {
        'statusCode': 200,
        'body': json.dumps('Processing completed successfully.')
    }