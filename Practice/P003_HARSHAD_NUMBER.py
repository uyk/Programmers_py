"""
---------------------------------------------------
프로그래머스 문제풀이 003
코딩테스트연습 > 연습문제 > 하샤드 수
---------------------------------------------------
양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.
x는 1 이상, 10000 이하인 정수입니다.
"""
HARSHARD_NUMBER = 12
def runSolution() :
  return solution(HARSHARD_NUMBER)

def solution(x):  
  answer = False
  x_sum = 0
  for i in str(x) :
    print(i)
    x_sum += int(i)
  if x % x_sum == 0 :
    answer = True
  return answer
