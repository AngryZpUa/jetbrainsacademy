# put your python code here
input_list = input().split()
words_list = [x.lower() for x in input_list]
result = {}
for word in words_list:
    result[word] = words_list.count(word)
for key, value in result.items():
    print('{} {}'.format(key, value))
