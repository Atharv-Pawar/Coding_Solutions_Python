def vowel_count(str):
    s = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for i in str:
        if i in s:
            count += 1
    return count


if __name__ == "__main__":
    print(vowel_count("avacoddoo"))