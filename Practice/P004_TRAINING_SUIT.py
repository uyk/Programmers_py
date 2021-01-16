"""
---------------------------------------------------
프로그래머스 문제풀이 004
코딩테스트연습 > 연습문제 > 체육복
---------------------------------------------------
점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다. 다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다. 학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다. 예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다. 체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.

전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.
"""
TRAINING_SUIT_N = 5
TRAINING_SUIT_LOST = [2, 4]
TRAINING_SUIT_RESERVE = [1, 3, 5]
def runSolution() :
  return solution(TRAINING_SUIT_N,TRAINING_SUIT_LOST,TRAINING_SUIT_RESERVE)

def solution(n, lost, reserve):
  arr = []
  arrAll = []
  final = []
  for i in lost :
    tempList = []
    if i-1 in reserve :
      tempList.append(i-1)
      arrAll.append(i-1)
    if i+1 in reserve :
      tempList.append(i+1)
      arrAll.append(i+1)
    if len(tempList) != 0 :
      arr.append(tempList)
  print(arr)
  print(arrAll)
  #arr2 = [(2, [1, 3]), (4, [3, 5])]
  #test = (2, [1, 3])
  #print(test[1])
  for i in arr :
    for j in i :
      if j not in arrAll :
        final.append(j)
        continue     

  print(arr)    

  answer = 0
  return answer