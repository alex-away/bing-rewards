# Bing Rewards Automation

## Overview
This project automates Bing searches to help earn Bing Rewards points by generating random keywords and automatically searching them using Microsoft Edge.

## Features
- Generates 30 random keywords using an API
- Automatically opens Bing searches for each keyword
- Provides a 30-second delay between searches
- Uses Microsoft Edge browser for searching

## Prerequisites
- Python 3.x
- Microsoft Edge browser
- Internet connection
- API Ninjas API key for random word generation

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/bing-rewards.git
cd bing-rewards
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Replace the API key in `keyword_gen.py`:
   - Sign up at [API Ninjas](https://api-ninjas.com/api/randomword)
   - Replace `'YOUR_API_KEY'` with your actual API key

## Usage

1. Generate Keywords:
```bash
python keyword_gen.py
```
This script will:
- Fetch 30 random words from API Ninjas
- Save the words to `keywords.txt`

2. Run Bing Searches:
```bash
python bing_search.py
```
This script will:
- Read keywords from `keywords.txt`
- Open each keyword in a Bing search using Microsoft Edge
- Wait 30 seconds between searches

## Configuration
- Modify the Edge executable path in `bing_search.py` if needed
- Adjust the number of keywords in `keyword_gen.py`
- Customize search interval in `bing_search.py`

## Notes
- Ensure Microsoft Edge is installed
- The script is intended for educational purposes
- Comply with Bing Rewards program terms of service

## License
This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.

## Disclaimer
This script is provided as-is. Use at your own discretion and risk. The authors are not responsible for any consequences of using this automation tool.