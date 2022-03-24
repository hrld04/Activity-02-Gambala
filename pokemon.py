import random

modifier = {
    "tar": 1,
    "weat": 1,
    "badge": 1,
    "crit": 1,
    "random": random.uniform(0.85,1),
    "stab": 1.5,
    "type": 1,
}

mod = 1
for x in modifier:
    mod * modifier[x]


level = 90
power = 110
a = 205
d = 188

damage = ((((((2 * level)/5) + 2)* power * (a/5))/50) + 2) * float(mod)

print(damage)




