file_name = 'txt_files/alice.txt'
try:
    with open(file_name) as file_object:
        contents = file_object.read()
except FileNotFoundError as e:
    print("The file is not found！")
else:
    words = contents.split()
    num_words = len(words)
    print(num_words)