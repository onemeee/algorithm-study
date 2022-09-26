x, y, w, h = map(int, input().split())
dx = abs(w-x)
dy = abs(h-y)
if x < w and y < h:
    result = min(dx, dy, w-dx, h-dy)
elif x < w and y > h:
    result = dy
elif x > w and y < h:
    result = dx
else:
    result = dx + dy
print(result)