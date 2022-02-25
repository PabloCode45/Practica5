def funcionFibonacci (num) :
    if num == 0 or num==1 :
        return num
    else :
        return funcionFibonacci(num-1) + funcionFibonacci(num-2)