def clamp_title(book_title):
    lst = book_title.split()
    s = []
    for w in lst:
        if w[0] != '(':
            s.append(w)
    return " ".join(s)


def refactorDataFile():
    catalog = []

    with open("library_orig.txt", encoding='utf-8') as f_in:
        lines = [row.strip() for row in f_in]
        for i in range(0, len(lines), 2):
            title = lines[i]
            author = lines[i + 1]
            title = clamp_title(title)
            catalog.append((author, title))

    f_out = open("library.txt", "w", encoding='utf-8')
    for book in catalog:
        author = book[0]
        title = book[1]
        # print("Author: " + author, file=f_out, end="\n")
        # print("Title:  " + title,  file=f_out, end="\n")
        print(author + "=" + title, file=f_out, end="\n")
    f_out.close()

    f_out_sorted = open("library_sorted.txt", "w", encoding='utf-8')
    catalog.sort()
    for book in catalog:
        author = book[0]
        title = book[1]
        # print("Author: " + author, file=f_out_sorted, end="\n")
        # print("Title:  " + title,  file=f_out_sorted, end="\n")
        print(author + "=" + title, file=f_out_sorted, end="\n")
    f_out_sorted.close()


if __name__ == "__main__":
    refactorDataFile()

    print("XXX")
