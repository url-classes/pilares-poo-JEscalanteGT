from animal import Animal
from cat import Cat
from dog import Dog

cat1 = Cat('Gardfield', 2, True)
cat2 = Cat('Misho', 1, False)
cat3 = Cat('Kitty', 4, True)
cat4 = Cat('Señor bigotes', 2, True)
dog1 = Dog('Bruno', 2, 'Jorge')
dog2 = Dog('Lazy', 3, 'Fulana')
dog3 = Dog('Pinky', 3, 'Julio')

animals: list[Animal] = [
    cat2,
    dog1,
    dog3,
    cat1,
    cat3,
    dog2,
    cat4
]

for animal in animals:
    animal.make_sound()


