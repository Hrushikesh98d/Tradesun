from flask import Flask, render_template
import boto3
import pytz
from datetime import datetime
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

def fetch_data_from_aws():
    session = boto3.Session(
        aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name=os.getenv("AWS_REGION")
    )
    s3 = session.client('s3')
    bucket_name = 'time0512'
    object_key = 'data.txt'
    try:
        obj = s3.get_object(Bucket=bucket_name, Key=object_key)
        data = obj['Body'].read().decode('utf-8').splitlines()
    except s3.exceptions.NoSuchKey:
        data = []
    return data

def validate_and_clean_data(data):
    valid_data = []
    for row in data:
        try:
            date = datetime.strptime(row, '%Y-%m-%d %H:%M:%S')
            valid_data.append(row)
        except ValueError:
            print(f"Invalid date format or missing value: {row}")
    return valid_data

@app.route('/')
def index():
    data = fetch_data_from_aws()
    if not data:
        data = ["No data available"]
    else:
        data = validate_and_clean_data(data)
    timezones = pytz.all_timezones
    return render_template('index.html', data=data, timezones=timezones)

if __name__ == '__main__':
    app.run(debug=True)
