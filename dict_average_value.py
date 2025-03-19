d = {'Krishna': [67, 68, 69], 'Arjun': [70, 98, 63], 'Malika': [52, 56, 60]}

print(d['Malika'])
sums = 0
for values in d['Malika']:
    sums += values
avg = sums/len(d['Malika'])
print(f'{avg:.2f}')