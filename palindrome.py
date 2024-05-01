# def solution(inputString):
#     return inputString == inputString[::-1]


# letters = "abcdefghijklmnopqrstuvwxyz"

# print(letters[-1::-1])

inputArray = [3,6,-2,-5,7,3]
# def solution(inputArray):
#     inputArray.sort()
#     print(inputArray())
   
   
# solution([3,6,-2,-5,7,3])
inputArray.sort()
print(inputArray)




# Bit length
def answer(n):
    return n.bit_length()

answer(50)