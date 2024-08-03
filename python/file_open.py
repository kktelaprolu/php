import sys
import os
from os import system

file = open('python/123.txt','r')
content = file.read()
print(content)
file.close()

print("------------")

with open('python/123.txt','r') as file:
    content = file.read()
    print(content)


with open('python/example.txt','w') as file:
    file.write("How are you?")

system("cat ./python/example.txt")