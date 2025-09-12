def count_vowels(word):
    """
    Count the number of letters, vowels, and calculate the percentage of vowels in the word.

    Args:
        word (str): The input word.

    Returns:
        dict: A dictionary containing the number of letters, vowels, and percentage of vowels.
    """
    results = {
        "letters": 0,
        "vowels": 0,
        "percentage": 0.0
    }
    vowels = set("aeiouAEIOU")
    for char in word:
        results["letters"] += 1
        if char in vowels:
            results["vowels"] += 1
    if results["letters"] > 0:
        results["percentage"] = (results["vowels"] / results["letters"]) * 100
        return results
def main():
    word = input("Enter a word: ")
    results = count_vowels(word)
    print(f"Word: {word}")
    print(f"Number of Letters: {results['letters']}")
    print(f"Number of Vowels: {results['vowels']}")
    print(f"Percentage of Vowels: {results['percentage']:.2f}%")

if __name__ == "__main__":
    main()