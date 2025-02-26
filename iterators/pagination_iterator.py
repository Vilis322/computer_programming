class Paginator:
    """Represents an iterator that paginates a dataset.

    The iterator returning a structured object containing: the current page number,
    the maximum number of pages and the actual data for that page.
    """
    def __init__(self, data: list, page_max: int):
        """Initializes the iterator with a list of data and a maximum page size.

        Args:
            data (list): The dataset to be paginated.
            page_max (int): The maximum number of items per page.
        """
        self.data: list = data
        self.page_max: int = page_max
        self.page: int = 1
        self.total_pages = (len(self.data) + self.page_max - 1) // self.page_max

    def __iter__(self) -> "Paginator":
        """Returns the iterator.

        This method is called when an iterator is required for a container.

        Returns:
            Paginator: The iterator object itself.
        """
        return self

    def __next__(self) -> dict:
        """Returns the next page of data.

        This method fetches the next subset of data based on the current page and updates the page counter.

        Returns:
            dict: A dictionary containing the current page number, number of pages, and the corresponding data.

        Raises:
            StopIteration: When there are no more pages left.
        """
        if self.page > self.total_pages:
            raise StopIteration

        start = (self.page - 1) * self.page_max
        end = self.page * self.page_max
        page_data = self.data[start:end]
        pager = {'page': self.page,
                 'max_page': self.page_max,
                 'data': page_data
                 }
        self.page += 1
        return pager


if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    pager = Paginator(data, 3)

    for page in pager:
        print(page)
