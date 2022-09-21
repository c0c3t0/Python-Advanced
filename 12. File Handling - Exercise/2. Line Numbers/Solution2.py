

with open("text.txt", "r") as file, open("output.txt", "w") as result:
    line_number = 1
    for line in file:
        if not line:
            break

        letters_count = 0
        punctuation_marks_count = 0
        for el in line:
            if el.isalpha():
                letters_count += 1
            elif not el.isspace() and not el.isalnum():
                punctuation_marks_count += 1
        result.write(f"Line {line_number}: {line.strip()} ({letters_count})({punctuation_marks_count})")
        result.write("\n")
        line_number += 1
