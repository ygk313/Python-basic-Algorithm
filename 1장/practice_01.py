import math
# ===============진법변환====================
def change_base(num, base):
    multiplier, result = 1, 0
    
    while num>0:
        remain = num%10
        num = num//10
        result += remain*multiplier
        multiplier = multiplier*base
    
    print("변환한 값", result)

def change_sixteen(num, base):
    strings = "0123456789ABCEDF"
    length = len(num)
    multiplier, result = 1, 0

    for i in range(length-1, -1, -1):
        if num[i] in strings:
            result += strings.index(num[i])*multiplier
        multiplier = multiplier*base

    print("변환한 값", result)

def run_base():
    num, base = input("변환할 숫자, 진수:").split(',')
    if base == "16":
        change_sixteen(num, int(base))
    else:
        change_base(int(num), int(base))
    
# =============================================

# ===========최대공약수와 최대공배수============
def gcd(num1, num2):
    a, b = num1, num2
    
    while b!=0:
        a, b = b, a%b
    
    print("최대공약수:",a)
    return a

def smallest(num1, num2):
    gc = gcd(num1, num2)
    result = 0
    result = (num1//gc)*(num2//gc)*gc
    print("최소공배수:", result)

# =============================================
# ==============피보나치 수열===================
def fib(num):
    a,b=0,1
    if num<2: print("피보나치 수열:", num)
    for i in range(num):
        result = b
        a,b = b, a+b
    print("피보나치 수열:", result)

# =============================================
# ================소수판별하기==================
def find_prime(num):
    flag =0
    if num<4: flag = 1
    else:
        for i in range(2, int(math.sqrt(num))+1):
            if (num%i==0):
                flag =0
                break
            else:
                flag = 1
    if (flag):
        print("소수입니다")
    else:
        print("소수가 아닙니다.")
# =============================================

if __name__=="__main__":
    run_base()
    # smallest(12,16)
    # fib(10)
    # find_prime(10)