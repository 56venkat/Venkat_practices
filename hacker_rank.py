l = [['Harsh', 20], ['Beria', 20], ['Varun', 19], ['Kakunami', 19], ['Vikas', 21]]
res = sorted(l, key=lambda x:x[1])
lowest_value = res[0][1]
i = 0
while i<len(res) and res[i][1] == lowest_value:
    i += 1
second_low = res[i][1]
res = [i[0] for i in res if i[1] == second_low]
res.sort()
print(res)