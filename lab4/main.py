def get_total(item, size):
    n = len(item)

    total = [[0 for i in range(size + 1)] for j in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, size + 1):
            if item[i-1][1] > j:
                total[i][j] = total[i-1][j]
            else:
                total[i][j] = max(item[i-1][2] + total[i-1][j - item[i-1][1]], total[i-1][j])
    return total

def get_stuuf(item, size):
    total = get_total(item, size)
    n = len(item)
    res = total[n][size]
    bag = []
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == total[i-1][size]:
            continue
        else:
            bag.append(item[i-1])
            res -= item[i-1][2]
            size -= item[i-1][1]
    return bag

item = [['rifle', 3, 25], # rifle
        ['pistol', 2, 15], # pistol
        ['ammo', 2, 15], # ammo
        ['medkit', 2, 20], # medkit
        ['knife', 1, 15], # knife
        ['axe', 3, 20], # axe
        ['totem', 1, 25], # totem
        ['flask', 1, 15], # flask
        ['antidot', 1, 10], # antidot
        ['food', 2, 20], # food
        ['bow', 2, 20]] # bow
total_value = sum(i[2] for i in item)
sort_item = sorted(item, key = lambda x: x[2]/x[1], reverse=False)
size = 8
n = len(item)
bag = get_stuuf(sort_item, size)

survival_score =sum(j[2] for j in bag) - (total_value - sum(j[2] for j in bag)) + 5 + 15
stuf = [i[0] for i in bag] + ['inhaler']

print('Chances of survival (player has asthma):', survival_score)
print("Stuff in the bag", stuf)

print()
#for inventory with 7

size = 6
bag_7 = get_stuuf(item, size)

survival_score_7 = sum(j[2] for j in bag_7) - (total_value - sum(j[2] for j in bag_7)) + 5 + 15
stuf_7 = [i[0] for i in bag_7] + ['inhaler']

print('Chances of survival (player has asthma):', survival_score_7)
print("Stuff in the bag", stuf_7)
#for an inventory with 7 cells, the chances of survival will be -10
