"""
프로그래머스 문제풀이 001
코딩테스트연습 > 연습문제 > 서울에서 김서방 찾기
"""
FIND_KIM = ["Kim","Lee","James"]
def runSolution() :
  return solution(FIND_KIM)

def solution(seoul):
    indexOfKim = str(seoul.index("Kim"))
    answer = "김서방은 " + indexOfKim + "에 있다"
    return answer