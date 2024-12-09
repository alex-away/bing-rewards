import requests

# Replace 'YOUR_API_KEY' with your actual API key
api_url = 'https://api.api-ninjas.com/v1/randomword'
headers = {'X-Api-Key': 'YOUR_API_KEY'}

words = []  # List to store fetched words

print("Starting to fetch random words...")

for i in range(30):  # Fetch 30 words
    print(f"Fetching word {i + 1}...")
    response = requests.get(api_url, headers=headers)
    
    if response.status_code == requests.codes.ok:
        word_list = response.json().get('word')  # Get the list of words
        if isinstance(word_list, list) and len(word_list) > 0:  # Ensure we have a non-empty list
            word = word_list[0]  # Access the first word in the list
            words.append(word)  # Store word in the list
            print(f"Fetched word: {word}")
        else:
            print(f"Unexpected response format: {response.json()}")
    else:
        print("Error:", response.status_code, response.text)

# Save words to a text file without an extra newline at the end
with open("keywords.txt", "w") as file:
    if words:  # Check if there are any words to write
        file.write("\n".join(words))  # Join words with newline and write

print("Words saved to keywords.txt")