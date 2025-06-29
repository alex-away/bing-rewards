from keyword_gen import generate_keywords
from bing_search import run_bing_search


def main():
    print("Generating keywords...")
    generate_keywords()
    print("Running Bing search automation...")
    run_bing_search()


if __name__ == "__main__":
    main()
