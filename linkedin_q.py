inp = [0,1,3,50,75]

out = []

for i in range(len(inp)):
    out.extend([str(i) for i in range(inp[i],inp[i-1]) if i not in inp])

print(out)
