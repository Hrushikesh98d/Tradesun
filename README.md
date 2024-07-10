# Trade Sun

## Author
Hrushikesh Dandge

## Description
A web application that fetches data from an AWS S3 bucket and displays it, with the capability to convert times to different timezones.

## Setup and Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/yourrepository.git
    cd yourrepository
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Create the .env file and fill the keys
   
4. Run the application:
    ```bash
    python app.py
    ```

## Usage
- Open your browser and go to `http://127.0.0.1:5000/`.
- Select your timezone to see the converted times.

## AWS Setup
- S3 bucket: `time0512`
- File: `data.txt` with datetime entries (`YYYY-MM-DD HH:MM:SS`).

## Dependencies
- Flask
- Boto3
- Pytz
