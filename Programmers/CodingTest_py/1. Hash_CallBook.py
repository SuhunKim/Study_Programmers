# def solution(phone_book):
#     answer = True
#     phone_book.sort()
#     for i in range(len(phone_book)):
#         if phone_book[i+1].str.contains(phone_book[i].str):
#             return False

# def solution(phone_book):
#     hash = {}
#     for i in phone_book:
#       hash[i] = 1
    
#     for i in phone_book:
#        arr=""
#        for j in i:
#           arr+= j

#           if arr in hash and arr!=j:
#              return False
        
#     return True

def solution(phone_book):
    phone_book.sort()

#   for i,j in phone_book:
#        for j in phone_book:
    for i,j in zip(phone_book, phone_book[1:]):
        if j.startswith(i) and i!=j:
                return False    
    
    return True

#solution(["119", "97674223", "1195524421"])
solution(["123","456","789"])