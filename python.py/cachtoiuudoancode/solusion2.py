list_of_words=["apple", "banana", "cherry", "date", "elderberry"]
to_print=" "
for i in range(len(list_of_words)):
    to_print+=list_of_words[i]
    if i!=len(list_of_words)-1:
        to_print+="."
print(to_print)