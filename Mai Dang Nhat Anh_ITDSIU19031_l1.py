import threading
import time
def checkPrimeValue(n):
    if n < 2:
        return False
    else:
        for p in range (2, (n//2)+1):
            if n%p == 0:
                return False
        return True
def PrintPrimeValue(a):
    for i in range (0, len(a)):
        time.sleep(1)
        if(checkPrimeValue(a[i])==True):
            print(str(a[i])+" is prime number")
        else: print (str(a[i])+" is not prime number")
def CheckSymetricNumber(n):
    temp = n
    new_num = 0
    if n < 9:
        return False
    else:
        while temp!= 0:
            late_num = temp % 10
            new_num = new_num*10 + late_num
            temp //= 10
        if new_num == n:
            return True
        else: return False
def PrintSymetricNummber(a):
    for i in range (0, len(a)):
        time.sleep(1)
        if(CheckSymetricNumber(a[i])==True):
            print(str(a[i])+" is symetric number")
        else: print (str(a[i])+" is not symetric number")
a1 = [2,3,4,5,6]
a2 = [1221,2112,13,45,5445,45654]
def SingleThread():
    t = time.time()
    PrintSymetricNummber(a2)
    PrintPrimeValue(a1)  
    print("time: ", time.time() - t)
def MultiThread():
    t = time.time()
    thread1 = threading.Thread(target = PrintPrimeValue, args = (a1,))
    thread2 = threading.Thread(target = PrintSymetricNummber, args = (a2,))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("time: ", time.time() - t)
def main():
    SingleThread()
    print("------------------------------------------")
    MultiThread()
if __name__ == "__main__" :
    main()