def chopString(str: str):
    char_index = 0
    char = []
    temp = ""

    for index, value in enumerate(str):
        temp += value

        if index != 0 and index % 250 == 0 or index == len(str) - 1:
            char.append(temp)
            temp = ""

    for string in char:

        if string == char[-1]:
            break
        if string[-1] != " ":
            for index, value in enumerate(string[::-1]):
                if value == " ":
                    char[char_index + 1] = string[len(string) - index :] + char[char_index + 1]
                    char[char_index] = string[:len(string) - index]
                    break

        char_index += 1

    return char


