
def swapping():
     with open('file1.txt', 'r') as a:
        data_a = a.read()
     with open('file2.txt', 'r') as b:
        data_b = b.read()
     with open('file1.txt', 'w') as c:
        c.write(data_b)
     with open('file2.txt', 'w') as d:
        d.write(data_a)
        
swapping()
