for tc in range(1, int(input())+1):
    day, month, thmon, year = map(int, input().split())
    swim = [0] + list(map(int, input().split()))
    day_month_fee = [0] * 13
    pay = []
    for i in range(1, 13):
        if swim[i] != 0:
            # 1일권으로 계산
            day_fee = swim[i] * day
            if day_fee < month:
                day_month_fee[i] = day_fee
            else:
                day_month_fee[i] = month
    for i in range(1, 13):
        pay.append(day_month_fee[i])
        if i%3 == 0:
            print(sum(pay[i-2:i+1]))
            if sum(pay[i-2:i+1]) > thmon:
                pay[i-2] = 0
                pay[i-1] = 0
                pay[i] = thmon
    print(pay)
    result = sum(pay)
    result = min(result, year)
    print(f'#{tc} {result}')