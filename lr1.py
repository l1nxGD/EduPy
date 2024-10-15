import time

GREEN = '\u001b[42m'
YELLOW= '\u001b[43m'
RED = '\u001b[41m'
END = '\u001b[0m'

for i in range(8):
    if i < 4:
        print(f'{GREEN}{'    '*3}{YELLOW}{'    '*4}{END}')
    else:
        print(f'{GREEN}{'    '*3}{RED}{'    '*4}{END}')
'''
#'''
RED = '\u001b[41m'
END = '\u001b[0m'
#9*5   1 2 3 4 5 6 7 8 9
print('1 1 + 1 1 1 + 1 1')#1
print('1 + + + 1 + + + 1')#2
print('+ + + + + + + + +')#3
print('1 + + + 1 + + + 1')#4
print('1 1 + 1 1 1 + 1 1')#5
print()

for i in range(5):
    if i < 2:
        print(f'{'   '* abs(2 - i)}{RED}{'#  '* (i * 2 + 1)}{END}{'   '*(3 - i*2)}{RED}{'#  ' * (i*2+1)}{END}{'   '*abs(2 - i)}')
    elif(i == 2):
        print(f'{RED}{'#  ' * ((i+1)**2)}{END}')
    else:
        print(f'{'   ' * (i - 2)}{RED}{'#  ' * abs(i*2 - 9)}{END}{'   ' * abs(5 - i*2)}{RED}{'#  ' * (9 - i*2)}{END}{'   '*(i-2)}')
    time.sleep(0.5)
#0 1 2 -> 1 3 4 -> 1 3 7
#3 4 -> 3 1
#'''

plot_list = [[0 for j in range(10)] for i in range(10)]
res_ls = [i+1 for i in range(10)]
step = abs(res_ls[0] - res_ls[9])//4

for i in range(len(plot_list)):
    for j in range(len(plot_list[i])):
        if j == 0:
            plot_list[i][j] = step*(8-i) + step

for i in range(len(plot_list) - 1):
    for j in range(len(plot_list[i])):
        if abs((plot_list[i][0] - res_ls[9 - j])) < step:
            for k in range(9):
                if 8 -k == j:
                    plot_list[i][k+1] = 1

for i in range(len(plot_list)):
    plot_list[i][0] = str(plot_list[i][0]) + '   '
    for j in range(1, len(res_ls)):

        if plot_list[i][j] == 1:
            plot_list[i][j] = '#'
        if plot_list[i][j] == 0:
            plot_list[i][j] = "-"
#plot_list[9] = (0.0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

for i in plot_list:
    print(*i)
print('     1 2 3 4 5 6 7 8 9')

f = open('sequence.txt')
st = [float(i) for i in f]
res = list()
for i in st:
    if (i >= 0 and i <= 5) or (i <= -5 and i >= -10):
        res.append(i)
print(sorted(res, reverse=True))
