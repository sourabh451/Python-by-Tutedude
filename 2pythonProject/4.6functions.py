#RECURSION
import sys
#print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)

n = 0
def python():
    global n
    n = n + 1
    print("Python",n)
    python()

python()