# I left a lot of commented out code in this file which originally calculated other styles of dough.
# I didn't find those functions necessary any more but left them in case I changed my mind.


def new_york_style(flour):
#    flour = float(input("How much flour (in grams)? "))
    sugar = flour * 0.02
    salt = flour * 0.015
    yeast = flour * 0.015
    oil = flour * 0.05
    water = flour * 0.67
    return sugar, salt, yeast, oil, water

#def neapolitan():
#    flour = float(input("How much flour (in grams)? "))
#    salt = flour * 0.02
#    yeast = flour * 0.015
#    water = flour * 0.65
#    print("Flour: " + format(flour, '.2f') + "g")
#    print("Salt: " + format(salt, '.2f') + "g")
#    print("Yeast: " + format(yeast, '.2f') + "g")
#    print("Water: " + format(water, '.2f') + "g")

#def sicilian():
#    flour = float(input("How much flour (in grams)? "))
#    salt = flour * 0.02
#    yeast = flour * 0.015
#    oil = flour * 0.03
#    water = flour * 0.70
#    print("Flour: " + format(flour, '.2f') + "g")
#    print("Salt: " + format(salt, '.2f') + "g")
#    print("Yeast: " + format(yeast, '.2f') + "g")
#    print("Oil: " + format(oil, '.2f') + "g")
#    print("Water: " + format(water, '.2f') + "g")

def convert(flour, sugar, salt, yeast, oil, water):
    w_oz = (flour + salt + yeast + oil + water) / 28.34952
    return format(w_oz, '.2f')

def by_weight():
    target = format(float(input("What is the desired amount of dough? (In ounces.): ")), '.2f')
    weight = 0
    f = 0
    while weight != target:
        sugar, salt, yeast, oil, water = new_york_style(f)
        f+=0.01
        weight = convert(f, sugar, salt, yeast, oil, water)
    print("Flour: " + format(f, '.2f') + "g")
    print("Salt: " + format(salt, '.2f') + "g")
    print("Yeast: " + format(yeast, '.2f') + "g")
    print("Oil: " + format(oil, '.2f') + "g")
    print("Water: " + format(water, '.2f') + "g")

by_weight()
