file_path = "fille.txt"
file = open(file_path, 'w')
file.write("1 :  Mohamed Ali  0615332211\n")
file.write("2 :  Nor Mohamed   0615778888\n")
file.write("3 :  Hassan Awaale  0615665544")
file.close()

file = open(file_path, 'r')
content = file.read()
file.close()

find_word = input("Enter the word to find: ")
replace_word = input("Enter the word to replace with: ")
new_content = content.replace(find_word, replace_word)

print("New Content:\n",  new_content)
