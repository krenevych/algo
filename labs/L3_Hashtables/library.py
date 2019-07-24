def clamp_title(book_title):
    lst = book_title.split()
    s = []
    for w in lst:
        if w[0] != '(':
            s.append(w)
    return " ".join(s)


catalog = []
f_out = open("library_out.txt", "w", encoding='utf-8')
with open("library.txt", encoding='utf-8') as f_in:
    lines = [row.strip() for row in f_in]
    for i in range(0, len(lines), 2):
        title = lines[i]
        author = lines[i + 1]

        title = clamp_title(title)

        catalog.append((author, title))

        print("Author: " + author, file=f_out, end="\n")
        print("Title:  " + title,  file=f_out, end="\n")

f_out.close()

catalog.sort()


print("XXX")
