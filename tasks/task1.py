# tasks/task1.py

def solve():
# Ниже пишите решение задачи
    var S, x, y: longint;
    begin
    readln(S);
    x:=S div 6;
    y:=4*x;
    writeln(x,' ', y,' ', x);
   

    
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()