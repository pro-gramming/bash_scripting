import re


pattern = re.compile(r'\w+@\w+\.com')

with open('detail.txt', 'r') as f:
    
    contents = f.read()
    matches = pattern.finditer(contents)

    for match in matches:
        print(match)
