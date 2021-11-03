from typing import List

words: List[str] = ['hola','como']
w: str

for w in words:
        print(w,len(w))


words.append('estas')
for w in words:
    print(w,len(w))

r: range= range(5)

for i in r:
    print(i)