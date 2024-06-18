def solution(numbers):
  ret = [ ]  

  for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
      ret.append(numbers[i] + numbers[j])

  ret = sorted(set(ret))
  return ret  

print(solution([2,1,3,4,1]))