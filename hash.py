n = int(input())
outputs = []
for i in range(n):
    m, c = map(int, input().split())

    table = [[] for _ in range(m)]

    keys = list(map(int, input().split()))

    for key in keys:
        address = key % m
        table[address].append(key)
    output = ""
    for j in range(m):
        output += f"{j} -> "
        for k in table[j]:
            output += f"{k} -> "
        output += "\\\n"
    outputs.append(output)
    
for i, output in enumerate(outputs):
    print(output)
    if i != len(outputs) - 1:
        print()