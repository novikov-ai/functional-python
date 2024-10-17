from pymonad.tools import curry
from pymonad.maybe import Maybe, Just, Nothing
from pymonad.list import ListMonad

@curry(2)
def add(x, y):
    return x + y

def add10(x):
        return x.map(lambda x: add(10, x))

print(add10(Just(5))) # Just 15
print(add10(ListMonad(10,20,30))) # [20, 30, 40]