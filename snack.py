'''snack'''
def main():
    '''hungry'''
    money = int(input())
    cost_water = int(input())
    snack1 = int(input())
    snack2 = int(input())
    snack3 = int(input())
    ans = money - cost_water
    if ans%3 == 0:
        snack1 = snack1*10
        ans2 = ans - snack1
    elif ans%3 == 1:
        snack1 = snack1*15
        ans2 = ans - snack1
    elif ans%3 == 2:
        snack1 = snack1*20
        ans2 = ans - snack1
    if ans2%3 == 0:
        snack2 = snack2*12
        ans4 = ans2 - snack2
    elif ans2%3 == 1:
        snack2 = snack2*15
        ans4 = ans2 - snack2
    elif ans2%3 == 2:
        snack2 = snack2*18
        ans4 = ans2 - snack2
    if ans4%3 == 0:
        snack3 = snack3*5
        ans6 = ans4 - snack3
    elif ans4%3 == 1:
        snack3 = snack3*7
        ans6 = ans4 - snack3
    elif ans4%3 == 2:
        snack3 = snack3*9
        ans6 = ans4 - snack3
    if ans6 < 0:
        print('Now you have', money, 'left.'+'\n'+"You don't have enough money!")
    elif ans6 >= 0:
        print('Now you have', ans6, 'left.')
        print("Here's your order! ")
        print('Water:', cost_water, 'baht')
        print('Snack number 1:', snack1, 'baht')
        print('Snack number 2:', snack2, 'baht')
        print('Snack number 3:', snack3, 'baht')
main()
    