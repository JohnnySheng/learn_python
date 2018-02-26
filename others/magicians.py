def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    index = 0;
    for magician in magicians:
        magicians.remove(magician)
        magician = "the great " + magician.title()
        # print(magician)
        magicians.insert(index,magician)
        index = index + 1
    return magicians;

magicians = ['alice', 'david', 'carolina']
new_magicians = make_great(magicians[:])
show_magicians(magicians)
show_magicians(new_magicians)
