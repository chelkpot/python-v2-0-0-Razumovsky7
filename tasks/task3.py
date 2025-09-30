# tasks/task3.py

def solve():
# Ниже пишите решение задачи
    a, b = map(int, input().split())
    n = (a + b) - 1
    garry = n - a
    larry = n - b
    print(garry, larry)


# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()