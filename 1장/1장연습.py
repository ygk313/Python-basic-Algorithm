# 내가 짠 이진법 코드
def bin_to_decimal(num):
    numstr = str(num)
    length = len(numstr)
    sum = 0
    for i in range(length):
        sum += int(numstr[length-i-1])*2**i

    print(sum)
# 책에 나오는 이진법 코드
def convert_to_decimal(number, base):
    multiplier, result = 1,0
    while number>0:
        result += number%10*multiplier
        multiplier *= base
        number = number//10
    return result

def test_convert_to_decimal():
    number, base = 1001, 2
    assert(conver_to_decimal(number, base)==9)
    print("테스트 통과")
def oct_to_decimal(num):
    numstr = str(num)
    length = len(numstr)
    sum = 0
    for i in range(length):
        sum += int(numstr[length-i-1])*8**i

    print(sum)

def convert_from_decimal_larger_bases(number, base):
    strings = "0123456789ABCDEF"
    result = ""
    while number>0:
        digit = number % base
        result = strings[digit]+strings
        number = number//base
    return result

if __name__=="__main__":
    bin_to_decimal(101)
    oct_to_decimal(107)
    hex_to_decimal(172)