from functools import lru_cache
import time

@lru_cache(maxsize=None)
def square(n):
    time.sleep(3)
    return n*n

print(square(2))
print("done for 2")
print(square(3))
print("done for 3")
print(square(4))
print("done for 4")
print(square(5))
print("done for 5")
print(square(6))
print("done for 6")

print(square(2))
print("done for 2")
print(square(3))
print("done for 3")
print(square(4))
print("done for 4")
print(square(5))
print("done for 5")
print(square(6))
print("done for 6")

print(square(7))
print("done for 7")
print(square(8))
print("done for 8")

print(square(5))
print("done for 5")
print(square(6))
print("done for 6")