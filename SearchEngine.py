data1 = open("doc1.txt", "r").read().split()
data2 = open("doc2.txt", "r").read().split()
data3 = open("doc3.txt", "r").read().split()
data4 = open("doc4.txt", "r").read().split()

hash_map = {
        "doc1": data1,
        "doc2": data2,
        "doc3": data3,
        "doc4": data4
     }
word = input("Search: ")
# doc_name = ""
# line = 0
count = 0
start_at = 0
for doc, value in hash_map.items():
    for i in value:
        # print(d[key][value.index(i)])
        if hash_map[doc][value.index(i)] == word:
            doc_name = doc
            line = value.index(i, start_at)
            count += 1
            print("Word", word, "Found in ", doc_name, "in line ", line)
            start_at = value.index(i) + 1
    start_at = 0
# print(d[key][0] == word)
print("NUmber of occurences of this word ", count)