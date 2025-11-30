# 1
# class Driver:
#     def __init__(self, n, t):
#         self.n = n
#         self.t = list(map(int, t))
#         self.s = sum(self.t)
#
#     def __lt__(self, o):
#         return self.s < o.s
#
#
# n, m = map(int, input().split())
# d = []
# for _ in range(n):
#     name = input().strip()
#     times = input().split()
#     d.append(Driver(name, times))
# d.sort()
# print(d[0].n)


# 2
# import math
#
#
# class Point:
#     def __init__(self, a, b):
#         self.x = a
#         self.y = b
#
#     def dist(self, p):
#         dx = self.x - p.x
#         dy = self.y - p.y
#         return math.sqrt(dx * dx + dy * dy)
#
#
# x1, y1, x2, y2 = map(int, input().split())
# p1 = Point(x1, y1)
# p2 = Point(x2, y2)
# print(f"{p1.dist(p2):.10f}")


# 3
# import math
#
#
# class Point:
#     def __init__(self, a, b):
#         self.x = a
#         self.y = b
#
#     def d(self, p):
#         return math.hypot(self.x - p.x, self.y - p.y)
#
#
# class Circle:
#     def __init__(self, c, r):
#         self.c = c
#         self.r = r
#
#     def cross(self, o):
#         dist = self.c.d(o.c)
#         return dist <= self.r + o.r and dist >= abs(self.r - o.r)
#
#
# x1, y1, r1 = map(int, input().split())
# x2, y2, r2 = map(int, input().split())
# c1 = Circle(Point(x1, y1), r1)
# c2 = Circle(Point(x2, y2), r2)
# print("YES" if c1.cross(c2) else "NO")

# 4
# import math
#
# n = int(input())
# p = []
# for _ in range(n):
#     x, y = map(int, input().split())
#     p.append((x, y))
#
# s = set()
# for i in range(n):
#     for j in range(i+1, n):
#         dx = p[i][0] - p[j][0]
#         dy = p[i][1] - p[j][1]
#         s.add(math.sqrt(dx*dx + dy*dy))
#
# res = sorted(s)
# print(len(res))
# for x in res:
#     print(f"{x:.12f}")

# 5
# x1, y1, x2, y2, x3, y3 = map(int, input().split())
# s = abs((x2-x1)*(y3-y1) - (x3-x1)*(y2-y1)) / 2
# print(int(s) if s == int(s) else s)


# 6
# p = [tuple(map(int, input().split())) for _ in range(4)]
#
# def area(a, b, c):
#     return abs((b[0]-a[0])*(c[1]-a[1]) - (c[0]-a[0])*(b[1]-a[1])) / 2
#
# a, b, c, t = p
# total = area(a, b, c)
# s1 = area(t, a, b)
# s2 = area(t, b, c)
# s3 = area(t, c, a)
#
# print("In" if abs(s1+s2+s3 - total) < 0.000001 else "Out")

# 7
# import math
#
#
# class Point:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def dist(self, p):
#         return math.hypot(self.a - p.a, self.b - p.b)
#
#
# class Circle:
#     def __init__(self, c, r):
#         self.c = c
#         self.r = r
#
#     def has(self, p):
#         return self.c.dist(p) <= self.r
#
#
# class Operator:
#     def __init__(self, n):
#         self.n = n
#         self.s = []
#
#     def add(self, c):
#         self.s.append(c)
#
#     def cnt(self, p):
#         return sum(1 for t in self.s if t.has(p))
#
#
# n = int(input())
# ops = {}
# ord = []
#
# for _ in range(n):
#     name = input().strip()
#     x, y, r = map(int, input().split())
#     if name not in ops:
#         ops[name] = Operator(name)
#         ord.append(name)
#     center = Point(x, y)
#     tower = Circle(center, r)
#     ops[name].add(tower)
#
# xa, ya = map(int, input().split())
# user = Point(xa, ya)
#
# res = []
# for name in ord:
#     c = ops[name].cnt(user)
#     res.append(f"{name} {c}")
#
# print(len(res))
# for r in res:
#     print(r)

# 8
# class Res:
#     def __init__(self, c, f, l, a):
#         self.c = c
#         self.f = f
#         self.l = l
#         self.a = a
#         self.v = self.get_v()
#
#     def get_v(self):
#         v = []
#         for x in self.a:
#             if x != 'x':
#                 v.append(float(x))
#         v.sort(reverse=True)
#         return v
#
#     def has_v(self):
#         return len(self.v) > 0
#
#     def best(self):
#         return self.v[0] if self.v else 0
#
#     def __lt__(self, o):
#         if not self.v: return True
#         if not o.v: return False
#         m = min(len(self.v), len(o.v))
#         for i in range(m):
#             if self.v[i] != o.v[i]:
#                 return self.v[i] < o.v[i]
#         return len(self.v) < len(o.v)
#
#
# class Tbl:
#     def __init__(self):
#         self.a = []
#
#     def add(self, r):
#         self.a.append(r)
#
#     def top(self, k):
#         v = [x for x in self.a if x.v]
#         v.sort(reverse=True)
#         return v[:k]
#
#     def out(self, t):
#         if not t:
#             return "No results."
#         r = []
#         for i, x in enumerate(t, 1):
#             r.append(f"{i}) {x.c} {x.f} {x.l} {x.best():.2f}")
#         return "\n".join(r)
#
#
# n = int(input())
# t = Tbl()
#
# for _ in range(n):
#     d = input().split()
#     cnt, fn, ln = d[0], d[1], d[2]
#     jumps = d[3:9]
#     t.add(Res(cnt, fn, ln, jumps))
#
# top = t.top(3)
# print(t.out(top))