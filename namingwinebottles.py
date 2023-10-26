import random

def newname(size):
    name = ""
    for _ in range(5):
        name += chr(random.randint(65, 90))
    return name.lower()

if __name__ == "__main__":

    names = {
        0.75 : "standard",
        12 : "balthazar",
        15 : "nebuchadnezzar"
    }

    winenum = int(input())
    
    for _ in range(winenum):
        name = input()
        name = eval(name[:-1])
        
        if name not in names:
            names[name] = newname(name)

        print(names[name])