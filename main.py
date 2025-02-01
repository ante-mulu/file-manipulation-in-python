# file=open("my_file.txt")
# content=file.read()
# print(content)
with open("my_file.txt",mode="a") as file:
    file.write("\nAppending the text")
file.close()