string_1 = 'mein gut'
string_2 = 'Mein Gut'
if string_1 == string_2:
    print(True)
else:
    print(False)
if string_1.lower() == string_2.lower():
    print(True)
else:
    print(False)

strings = ['mein', 'Hause','Home']
if 'zu' in strings:
    print("zu is in the list")
elif 'mein' in strings:
    print("mein is in the list")
else:
    print("zu is not in the list")

