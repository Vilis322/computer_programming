from re import findall


class WordIterator:
    """Represents an iterator that iterates over words in a given string separated by spaces.

    Words are extracted using a regular expression that considers only alphabetic characters.
    """
    def __init__(self, string: str):
        """Initializes the iterator with list of words on base of the given string and index of iterable word.

        Args:
            string (str): The given string to iterate.

        Notes:
            - `self.words` (list): A list of words extracted from the input string.
            - `self.index` (int): The current index in the word list, default is 0.
        """
        self.words: list = findall(r'\b[a-zA-Z]+\b', string)
        self.index: int = 0

    def __iter__(self) -> "WordIterator":
        """Returns the iterator.

        This method is called when an iterator is required for a container.

        Returns:
            WordIterator: The iterator object itself.
        """
        return self

    def __next__(self) -> str:
        """Returns the next word from the extracted list of words.

        Returns:
            str: The next word in the sequence.

        Raises:
            StopIteration: If there are no more words left to iterate.
        """
        if self.index >= len(self.words):
            raise StopIteration
        word = self.words[self.index]
        self.index += 1
        return word


if __name__ == "__main__":
    text = "Python is   awesome!"
    it = WordIterator(text)
    print(list(it))  # Output: ['Python', 'is', 'awesome']
