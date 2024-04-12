number = input("몇 단까지 출력할까요?")

num_number = int(number)

opp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

for a in opp[0:num_number]:
    print("------[ %d 단 ]------" %a)
    for b in opp[0:20]:
        print(a * b)