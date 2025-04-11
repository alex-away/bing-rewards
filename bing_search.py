import time
import keyword_gen
import random
import pyautogui
import subprocess
import os

# Function to read keywords from a file.
def read_keywords(file_path):
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except Exception as e:
        print(f"Error reading keywords: {e}")
        return []

# Function to simulate human typing with random delays.
def human_type(text):
    for char in text:
        pyautogui.write(char)
        # Random delay between keystrokes (50-200ms)
        time.sleep(random.uniform(0.05, 0.2))

# Function to open Edge and navigate to Bing
def open_edge_with_bing():
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    
    try:
        # Open Edge with Bing.com
        subprocess.Popen([edge_path, "https://www.bing.com"])
        
        # Wait for Edge to open and load Bing
        print("Opening Edge and navigating to Bing.com...")
        time.sleep(5)  # Adjust if needed for your system
        
        return True
    except Exception as e:
        print(f"Error opening Edge: {e}")
        return False

# Main function to run the script.
def main():
    keywords = read_keywords('keywords.txt')
    
    if not keywords:
        print("No keywords found. Exiting.")
        return
    
    print(f"Found {len(keywords)} keywords to search.")
    print("Setting up for Edge and Bing...")
    
    # Make sure PyAutoGUI has a failsafe
    pyautogui.FAILSAFE = True
    
    # Give user time to switch to the right window if needed
    print("Starting in 5 seconds. Please don't move mouse after this countdown...")
    for i in range(5, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    
    # Open Edge with Bing
    if not open_edge_with_bing():
        print("Failed to open Edge. Exiting.")
        return
    
    try:
        # Process all keywords
        for i, keyword in enumerate(keywords):
            # Wait a bit for page to stabilize
            time.sleep(2)
            
            # First keyword doesn't need a countdown
            if i > 0:
                # Countdown timer with some randomness in the delay (25-35 seconds)
                delay = random.randint(25, 35)
                for remaining in range(delay, 0, -1):
                    print(f"Next search in {remaining} seconds...", end='\r')
                    time.sleep(1)
                print(" " * 30, end='\r')  # Clear the line
            
            # Find and click on the search box - focus precisely on the top search box
            search_box_x = pyautogui.size()[0] // 2  # Center horizontally
            search_box_y = 140  # Fixed position near the top where search box usually is
            
            # Click to focus on search box
            print(f"Focusing on search bar...")
            pyautogui.click(search_box_x, search_box_y)
            time.sleep(1)
            
            # Clear any existing text in a more controlled way
            for _ in range(25):  # Ensure we clear any previous text, up to 25 characters
                pyautogui.press('backspace')
            
            # Add a small pause before typing
            time.sleep(0.5)
            
            # Type and search
            print(f"Searching for: {keyword}...")
            human_type(keyword)
            time.sleep(random.uniform(0.5, 1.0))
            pyautogui.press('enter')
            print(f"Searched for '{keyword}'")
            
            # Add a pause after search to ensure page loads and prevent accidental clicking on results
            time.sleep(2)
        
        print("All searches completed.")
        
        # Wait a moment before closing
        time.sleep(3)
        print("Closing browser...")
        pyautogui.hotkey('alt', 'f4')
        
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        print("Process completed.")

if __name__ == "__main__":
    main()
