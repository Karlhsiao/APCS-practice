triangle = [int(x) for x in input().split()]

triangle.sort()

a = triangle[0]
b = triangle[1]
c = triangle[2]

print(a, b, c)

if (a + b) <= c:
    print("No")

elif (a*a + b*b) < c*c:
    print("Obtuse")

elif (a*a + b*b) > c*c:
    print("Acute")

elif (a*a + b*b) == c*c:
    print("Right")