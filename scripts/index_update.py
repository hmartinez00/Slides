import os

curso='python311'
clase='Intro'

file_start=os.path.join(curso, clase + '.html')
file_end=os.path.join('../reveal.js', 'index.html')

f = open(file_start, 'r', encoding='utf-8')
string=f.read()
f.close()

f = open(file_end, 'w', encoding='utf-8')
f.write(string)
f.close()

print(file_start)