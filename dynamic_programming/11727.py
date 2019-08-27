n=int(input())
tile = []
for i in range(0, n + 1):
    if i == 0 or i == 1:
        tile.append(1)
    else:
        tile.append((tile[i - 1] + tile[i - 2] * 2) % 10007)
print(tile[n]%10007)

