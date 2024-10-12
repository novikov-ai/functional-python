from pymonad.tools import curry

@curry(2)
def greeting(x:str, y:str):
    print(x+y)

hello = greeting("Hello, ")
hello("Alex")

@curry(4)
def greeting_full(word:str, comma:str, exclamation:str, name:str):
     print(word+comma+name+exclamation)

bye = greeting_full("Bye")
byeWithComma = bye(", ")
byeFull = byeWithComma("!")
byeFull("Mike")