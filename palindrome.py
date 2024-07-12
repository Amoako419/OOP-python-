# def solution(inputString):
#     return inputString == inputString[::-1]
# print(solution('racecar'))


# letters = "abcdefghijklmnopqrstuvwxyz"

# print(letters[19:0:-1])

# inputArray = [3,6,-2,-5,7,3]
# # def solution(inputArray):
# #     inputArray.sort()
# #     print(inputArray())
   
   
# # solution([3,6,-2,-5,7,3])
# inputArray.sort()
# print(inputArray)




# # Bit length
# def answer(n):
#     return n.bit_length()

# answer(50)


def solution(n):
    s = str(n)
    half = len(s)//2
    first = s[0:half]
    last = s[half:-1]
    if sum(first) == sum(last):
        return True
    else:
        return False
    
solution(1230)