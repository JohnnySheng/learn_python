from collections import OrderedDict
favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    if name in friends:
        print("Hi," + name.title() + ", I see your favorite language is " + language.title()+'.')
    else:
        print(name.title())

    
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")