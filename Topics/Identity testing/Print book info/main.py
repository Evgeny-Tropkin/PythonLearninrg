def print_book_info(title, author=None, year=None):
    #  Write your code here
    result = '"' + title + '"'

    if author is not None or year is not None:
        result += " was written"
    if author is not None:
        result += " by " + author
    if year is not None:
        result += " in " + year

    print(result)
