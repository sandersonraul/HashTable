n = int(input())
outputs = []
for i in range(n):
    size, inputs = map(int, input().split())

    table = [[] for _ in range(size)]

    keys = list(map(int, input().split()))

    for key in keys:
        address = key % size
        table[address].append(key)
    output = ""
    for j in range(size):
        output += f"{j} -> "
        for k in table[j]:
            output += f"{k} -> "
        output += "\\\n"
    outputs.append(output)
    
for i, output in enumerate(outputs):
    print(output)
    if i != len(outputs) - 1:
        print()