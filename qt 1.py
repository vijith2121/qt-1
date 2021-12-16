def repair_order(arr):
    data = sorted(arr, key=lambda i: (i['profit']), reverse=True)
    f2, f1, f3, = data[0], data[1], data[3]
    final_data = [f2['id'], f1['id'], f3['id']]
    return ",".join(final_data)


arr = [
    {'id': 'f1', 'deadline': 2, 'profit': 60},
    {'id': 'f2', 'deadline': 1, 'profit': 100},
    {'id': 'f3', 'deadline': 3, 'profit': 20},
    {'id': 'f4', 'deadline': 2, 'profit': 40},
    {'id': 'f5', 'deadline': 1, 'profit': 20}
]

print(repair_order(arr))
