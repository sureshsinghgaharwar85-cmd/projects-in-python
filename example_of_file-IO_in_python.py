with open("file.txt", "w") as f:
    for i in range(1, 11):
        # here only str can written so we use (str)
        # and + "/n" is written to add new line
        f.write(str(9 * i) + "\n")
