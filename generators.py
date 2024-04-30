def all_variants(string):
    for sliced in range(1, len(string)+1):
        for num_char in range(len(string)):
            if num_char + sliced > len(string):
                break
            yield string[num_char:num_char + sliced]


a = all_variants("abc")
for i in a:
    print(i)
