# tasks/task2.py

def solve():
# Ниже пишите решение задачи
    X, Y, Z = map(int, input().split())
    K = 3  
    R = K + 2  
    F = R + 7  
    total_cost = (X * K) + (Y * R) + (Z * F)
   

   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()