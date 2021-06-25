import urllib.request

fhandle = urllib.request.urlopen('http://localhost:9000/romeo.txt')
for line in fhandle:
    print(line.decode().strip())