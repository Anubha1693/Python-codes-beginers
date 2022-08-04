with open("anuva.txt","w") as f: #read = r, write = w, read+write = r+,w+
    for i in range(10):
        f.write(str(i) + '\n')

with open("anuva.txt","r") as f: #read = r, write = w, read+write = r+,w+
    lines = f.read()
    print(lines.split('\n'))
    lines = lines.split('\n')[:-1]
    print(lines)