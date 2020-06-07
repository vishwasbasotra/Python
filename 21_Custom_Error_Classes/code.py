class TooManyPagesReadError(ValueError):
    pass


class Book:
    def __init__(self,name: str,page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0
    def __repr__(self) -> str:
        return (
            '<Book {n!r}, pages read {p!r} out of {t!r}>'.format(n=self.name,p=self.pages_read,t=self.page_count)
            )
    def read (self, pages: int):
        if self.pages_read + pages > self.page_count:
            raise TooManyPagesReadError(
            'You tried to read {p} pages, but total pages are {t}'.format(p=self.pages_read+pages,t=self.page_count)
        )
        self.pages_read += pages
        print('You have read {p} out of {t}'.format(p=self.pages_read,t=self.page_count))

python = Book('Python',100)
try:
    python.read(50)
    python.read(100)
except TooManyPagesReadError as e:
    print(e)
finally:
    print('Reading is GOOD !!!')
