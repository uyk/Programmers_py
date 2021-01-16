"""
프로그래머스 문제풀이 002
코딩테스트연습 > 연습문제 > 같은 숫자는 싫어
"""
NO_SAME_CHAR = [1, 1, 3, 3, 0, 1, 1]
def runSolution() :
  return solution(NO_SAME_CHAR)

def solution(arr):
    answer = []
    for index,item in enumerate(arr) :
      print(index,item)
      if index == 0:
        answer.append(item)
      else :
        if answer[len(answer)-1] != item :
        #if answer[-1] != item :  
          answer.append(item)
    return answer
