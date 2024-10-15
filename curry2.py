from pymonad.tools import curry

# 3.1
@curry(2)
def tag(tag:str, value:str) -> str:
    return f"<{tag}>{value}</{tag}>"

bold = tag("b")
italic = tag("i")

print(bold("value"), italic("data")) # <b>value</b> <i>data</i>

# 3.2
@curry(3)
def tagV2(tag:str, value:str, data:dict) -> str:
    attrs = ' '.join([f'{key}="{value}"' for key, value in data.items()])
    return f"<{tag} {attrs}>{value}</{tag}>"

dicts = {"class":"list-group","style":"none"}

print(tagV2("li", "item 23", dicts)) # <li class="list-group" style="none">item 23</li>