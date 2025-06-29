import requests

def generate_keywords(count=30, api_key='YOUR_API_KEY', output_file="keywords.txt"):
    api_url = 'https://api.api-ninjas.com/v1/randomword'
    headers = {'X-Api-Key': api_key}
    words = []
    print("Starting to fetch random words...")
    for i in range(count):
        print(f"Fetching word {i + 1}...")
        response = requests.get(api_url, headers=headers)
        if response.status_code == requests.codes.ok:
            word_list = response.json().get('word')
            if isinstance(word_list, list) and len(word_list) > 0:
                word = word_list[0]
                words.append(word)
                print(f"Fetched word: {word}")
            else:
                print(f"Unexpected response format: {response.json()}")
        else:
            print("Error:", response.status_code, response.text)
    with open(output_file, "w") as file:
        if words:
            file.write("\n".join(words))
    print(f"Words saved to {output_file}")

if __name__ == "__main__":
    generate_keywords()