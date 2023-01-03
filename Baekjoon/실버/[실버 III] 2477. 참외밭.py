def rotate(list,n):
    return list[n:] + list[:n]

melon = int(input())
order_list = []
dis_list = []
check = []

for _ in range(6):
    order, dis = map(int, input().split())
    order_list.append(order)
    dis_list.append(dis)

for order in order_list:
    if order_list.count(order) == 1:
        check.append(order_list.index(order))
if 0 not in check or 5 not in check:
    order_list = rotate(order_list, check[1])
    dis_list = rotate(dis_list, check[1])

area = dis_list[0] * dis_list[-1] - (dis_list[2] * dis_list[3])

result = area * melon
print(result) 