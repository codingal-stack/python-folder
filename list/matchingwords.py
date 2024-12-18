def match(words):
    ctr = 0
    lst = []
    for i  in words:
        if len(i) > 1 and i[0] == i [-1]:
            ctr +=1
            lst.append(i)
    print(lst)
    return ctr






a = ['emile','tyosn','Soifon','Html','yesy']
count = match  (a)
print('no. of word with first and last letters are same',count)

