from pymonad.tools import curry
from pymonad.state import State

monster = {'health': 1000, 'loot': ['shield*', 'gold*']}

player = {'damage': 300, 'inventory': ['helmet', 'sword', 'armor']}

inventory_state = State.insert(player['inventory'])

@curry(2)
def fight(damage, inventory):
    def resolve_battle(health_remained):
        health_remained -= damage
        if health_remained <= 0:
            return inventory + monster['loot'], 0

        return inventory, health_remained

    return State(resolve_battle)

finale = inventory_state.then(fight(player['damage'])).then(fight(player['damage'])).then(fight(player['damage'])).then(fight(player['damage']))

result = finale.run(monster['health'])

print("Player inventory:", result[0]) # Player inventory: ['helmet', 'sword', 'armor', 'shield*', 'gold*']
print("Monster health:", result[1]) # Monster health: 0