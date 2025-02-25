from typing import Iterable, Iterator, Any


class SkippingIterator:
    """Represents an iterator class that iterates over a sequence but skips every n elements."""
    def __init__(self, sequence: Iterable, step: int):
        """Initializes the iterator with a sequence of iteration and a step size for iteration.

        Args:
            step (int): The step size of iteration.
            sequence (Iterable): The sequence of iterable elements to iterate by a step.
        """
        self.step: int = step
        self.sequence: Iterator = iter(sequence)

    def __iter__(self) -> "SkippingIterator":
        """Returns the iterator.

        This method is called when an iterator is required for a container.

        Returns:
            SkippingIterator: The iterator object itself.
        """
        return self

    def __next__(self) -> Any:
        """Returns the first element or the next element of the sequence by a specified step.

        Returns:
            Any: The first element or the next element of the sequence by a specified step.
        """
        current = next(self.sequence)

        for _ in range(self.step):
            try:
                next(self.sequence)
            except StopIteration:
                break

        return current


if __name__ == "__main__":
    seq = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    it = SkippingIterator(seq, 3)
    print(list(it)) # Output: [1, 4, 7]
    text = "abcdefghi"
    it = SkippingIterator(text, 3)
    print("".join(it))  # Output: "adg"""
    