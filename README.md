# Bing Rewards Automation

## Overview
This project automates Bing searches to help earn Bing Rewards points by generating random keywords and automatically searching them using Microsoft Edge with human-like typing behavior.

## Features
- Generates 30 random keywords using an API
- Automatically opens Bing.com in Microsoft Edge
- Types each keyword letter by letter with realistic timing
- Provides random delays between searches (25-35 seconds)
- Controls the mouse and keyboard directly using PyAutoGUI
- Simulates human-like search behavior

## Prerequisites
- Python 3.x
- Microsoft Edge browser
- Internet connection
- API Ninjas API key for random word generation

## Installation

1. Clone the repository:
```bash
git clone https://github.com/alex-away/bing-rewards.git
cd bing-rewards
```

2. Install [uv](https://docs.astral.sh/uv/getting-started/installation/) (if not already installed):
```bash
pip install uv
```

3. Create and activate a virtual environment using uv:
```bash
uv venv
```

Follow the instructions provided by uv to activate the virtual environment for your platform.

4. Install required dependencies using uv:
```bash
uv pip install -r pyproject.toml
```

5. Replace the API key in `keyword_gen.py`:
   - Sign up at [API Ninjas](https://api-ninjas.com/api/randomword)
   - Replace `'YOUR_API_KEY'` with your actual API key

## Usage

Run the main script to generate keywords and perform Bing searches:
```bash
uv run main.py
```

The script will automatically:
1. Generate 30 random keywords using API Ninjas
2. Open Microsoft Edge browser to Bing.com
3. For each keyword:
   - Type the keyword letter by letter like a human
   - Press Enter to search
   - Wait a random period between searches (25-35 seconds)
4. Close the browser after all searches are complete

## Important Notes About PyAutoGUI
- **DO NOT move your mouse during script execution**
- PyAutoGUI has a safety feature: move your mouse to a corner of the screen to abort
- The script needs to be able to control your mouse and keyboard
- Close other applications before running to avoid interference

## Configuration
- Adjust typing speed in the `human_type` function in `bing_search.py`
- Modify wait times between searches in `bing_search.py`
- Customize the number of keywords in `keyword_gen.py`

## Notes
- Ensure Microsoft Edge is installed
- The script is intended for educational purposes
- Comply with Bing Rewards program terms of service
- Automated behavior that appears too robotic might trigger security measures

## License
This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.

## Disclaimer
This script is provided as-is. Use at your own discretion and risk. The authors are not responsible for any consequences of using this automation tool.