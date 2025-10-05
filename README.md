# CCN Web Scraper Project

## Overview
This project is a web scraper built with Python, using `requests` to fetch web pages and `BeautifulSoup` to parse HTML content. It scrapes, describe what it scrapes, and saves the data to a CSV file or console.

## Requirements
- Python 3.8 or higher (check with `python3 --version`)
- Git (for cloning and managing the repository)
- Dependencies listed in `requirements.txt`:
  - beautifulsoup4==4.14.2
  - requests==2.32.5
  - Other dependencies (certifi, charset-normalizer, idna, soupsieve, urllib3)

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/webscraper.git
   cd webscraper

2. Best-practice: Set up a venv
    python3 -m venv venv
    source venv/bin/activate  # macOS/Linux
    # or
    venv\Scripts\activate  # Windows

3. Install Dependencies
    pip install -r requirements.txt    