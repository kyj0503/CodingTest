T = int(input())

def find_cheapest(month, acc):
    global answer

    if acc >= answer: 
        return

    if month > 11:
        if answer > acc: 
            answer = acc
        return 

    find_cheapest(month+1, acc + plans[month]*prices[0])

    find_cheapest(month+1, acc + prices[1])

    find_cheapest(month+3, acc + prices[2])

for tc in range(1, T+1):
    prices = list(map(int, input().split()))
    plans = list(map(int, input().split()))
    answer = prices[3]
    find_cheapest(0, 0)

    print('#{} {}'.format(tc, answer))