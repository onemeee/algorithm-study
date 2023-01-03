members = []
for i in range(9):
    members.append(int(input()))

members.sort()
def findmember(num_list):
    for i in range(9):
        remo = members.pop(i)
        k = sum(members) - 100 
        if k in members:
            members.pop(members.index(k))
        else:
            members.append(remo)
            members.sort()
        if len(members) == 7 and sum(members) == 100:
            return(members)

for i in findmember(members):
    print(i)