"""Process a list of numbers and a list of words, then print the results."""

LONG_WORD_THRESHOLD = 5  # words longer than this are treated as "long"


def process_numbers(numbers):
    """Double the even numbers and triple the odd numbers.

    Args:
        numbers (list of int): The integers to process.

    Returns:
        list of int: A new list, in the same order as the input, where each
        even number is multiplied by 2 and each odd number by 3.
    """
    return [number * 2 if number % 2 == 0 else number * 3 for number in numbers]


def format_words(words):
    """Join words into one string, uppercasing long words and lowercasing short ones.

    A word is "long" if it has more than LONG_WORD_THRESHOLD characters.

    Args:
        words (list of str): The words to format.

    Returns:
        str: The formatted words separated by single spaces, with no
        trailing space.
    """
    # join() avoids the trailing space the old loop had to strip off
    return " ".join(
        word.upper() if len(word) > LONG_WORD_THRESHOLD else word.lower()
        for word in words
    )


def main():
    """Run both processing functions on sample data and print the results."""
    sample_numbers = [1, 2, 3, 4, 5, 6, 7]
    sample_words = ["apple", "banana", "kiwi", "grapefruit", "cherry"]

    processed_numbers = process_numbers(sample_numbers)
    formatted_words = format_words(sample_words)

    print("Processed Numbers:", processed_numbers)
    print("Processed Strings:", formatted_words)


if __name__ == "__main__":
    main()