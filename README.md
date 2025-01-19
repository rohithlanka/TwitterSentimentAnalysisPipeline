# Twitter Sentiment Analysis Pipeline

This project simulates real-time sentiment analysis of tweets using AWS services. It involves generating synthetic Twitter data, processing it with AWS Lambda and Comprehend for sentiment analysis, storing it in DynamoDB, and visualizing insights with Python and visualization libraries.

## Project Overview

### Data Generation
- **Python Script**: Simulates Twitter data with `Faker` and a sample dataset (`Twitter_Data.csv`). Each record includes attributes like tweet text, username, age range, gender, and region.
- **Kinesis Stream**: Data is streamed in real-time to an AWS Kinesis data stream (`SocialMediaDataStream`).

### Data Processing
- **AWS Lambda**: Triggered by data arrival in the Kinesis stream, this function:
  - Decodes and parses the data.
  - Performs sentiment analysis on tweets using AWS Comprehend.
  - Stores enriched data (including sentiment scores) in a DynamoDB table (`tweetsrealtimetable`).

### Data Visualization
- **Visualization Script**: Fetches data from DynamoDB and generates insights:
  - Sentiment distribution bar plots.
  - Gender distribution pie charts.
  - Top 10 regions analysis.
  - Age vs. Sentiment trends.
  - Heatmaps for regions vs. sentiments.

## Technologies Used
- **Data Generation**: Python, Faker.
- **Data Streaming**: AWS Kinesis.
- **Data Processing**: AWS Lambda, AWS Comprehend, DynamoDB.
- **Data Visualization**: Python, Matplotlib, Seaborn, Pandas.

## Setup and Usage

### Prerequisites
1. **AWS Account**: Ensure access to AWS services (Kinesis, Lambda, Comprehend, DynamoDB).
2. **Python**: Install Python 3.x with required libraries (`boto3`, `Faker`, `matplotlib`, `seaborn`, `pandas`).
3. **Data**: Have the `Twitter_Data.csv` file available in the working directory.

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/rohithlanka/twitter-sentiment-analysis.git
   cd twitter-sentiment-analysis
   ```
2. **Configure AWS Credentials**:
   Set up AWS credentials in `~/.aws/credentials` or use environment variables.
   
3. **Data Streaming**:
   - Run the `DataGenerator.py` script to generate and stream data to Kinesis:
     ```bash
     python DataGenerator.py
     ```

4. **Lambda Function Deployment**:
   - Package and deploy the Lambda function for processing Kinesis data.
   - Ensure it is correctly configured to use `tweetsrealtimetable` DynamoDB table and AWS Comprehend.

5. **Data Visualization**:
   - Fetch and visualize data from DynamoDB using `Dashboard.py`:
     ```bash
     python Dashboard.py
     ```

## Visualizations
- **Sentiment Analysis**: Understand the overall sentiment distribution of tweets.
- **Demographics**: Analyze tweet trends by gender, region, and age.
- **Heatmaps**: Identify sentiment patterns across top regions.

## Future Enhancements
- Integrate real Twitter data via APIs.
- Automate the deployment of resources using AWS CloudFormation or Terraform.
- Expand visualization dashboards with tools like Tableau or Power BI.
