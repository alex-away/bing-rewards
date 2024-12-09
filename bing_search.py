import time
import subprocess
import keyword_gen
# import os

# Function to read keywords from a file.
def read_keywords(file_path):
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except Exception as e:
        print(f"Error reading keywords: {e}")
        return []

# Function to search Bing for a keyword using Microsoft Edge.
def search_bing(keyword):
    # Path to Microsoft Edge executable.
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    
    # Construct the Bing search URL.
    bing_url = f"https://www.bing.com/search?q={keyword}"
    
    try:
        print(f"Searching for: {keyword}...")
        subprocess.run([edge_path, bing_url])  # Open URL in Edge.
        print(f"Opened Bing search for '{keyword}'.")
    except FileNotFoundError:
        print("Error: Microsoft Edge executable not found. Please check the path.")
    except Exception as e:
        print(f"An error occurred while trying to open the browser: {e}")

# Main function to run the script.
def main():
    keywords = read_keywords('keywords.txt')
    
    if not keywords:
        print("No keywords found. Exiting.")
        return
    
    for keyword in keywords:
        search_bing(keyword)  # Search for the current keyword.
        
        # Countdown timer
        for remaining in range(30, 0, -1):
            print(f"Next search in {remaining} seconds...", end='\r')
            time.sleep(1)
            # if remaining == 27:
            #     os.system("taskkill /im msedge.exe /f")
        
        print(" " * 30, end='\r')  # Clear the line

if __name__ == "__main__":
    main()
