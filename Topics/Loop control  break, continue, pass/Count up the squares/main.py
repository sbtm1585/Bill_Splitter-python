sum = 0
squares = 0
while True:
    num = int(input())
    if num == 0:
        print(num)
        break
    squares += pow(num, 2)
    sum += num
    if sum == 0:
        print(squares)
        break