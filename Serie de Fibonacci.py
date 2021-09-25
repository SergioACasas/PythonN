print("----------------Serie de Fibonacci-----------------------")
fn1,fn2 = 0 , 1
while fn1 < 1598 :
    print(fn1,end=" ")
    fn = fn1 + fn2 
    fn1 = fn2
    fn2 = fn 
print("Fin")