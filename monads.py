from pymonad.maybe import Maybe, Just, Nothing

# Некий канатоходец ходит по канату с шестом, но на шест любят садиться птицы, а потом могут и улететь. 
# Канатоходец может держать равновесие, если разность кол-ва птиц на сторонах шеста не более 4. 
# Ну и канатоходец просто может упасть подскользнувшись на банановой кожуре. 
# Нужно смоделировать симуляцию последовательности событий с выдачей результата в виде «упал»/«не упал»

to_left = lambda num: (lambda l,r:
       Nothing   
       if abs((l+num) -r) > 4 
       else Just((l+num, r))       
)

to_right = lambda num: (lambda l,r:
    Nothing
    if abs((r+num)-l)>4
    else Just((l,r+num))
)

banana = lambda x: Nothing

def show(state:Maybe): 
    if state == Nothing:
        print("falled :(")
        return Nothing
    else:
        print("ok:", state.value)
        return Just(state.value)
        
begin = lambda: Just((0,0))

def simulate():
    state = begin().bind(lambda pos: to_left(3)(*pos)).bind(lambda pos: to_right(5)(*pos))
    show(state) # falled :(

simulate()