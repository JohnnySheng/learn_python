def build_profile(first, last, **user_info):
    profile = {}
    profile["fistname"] = first
    profile["lastname"] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('Johnny', 'Sheng', age=30, city='shanghai')
print(user_profile)