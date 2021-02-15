# 로또 조건 1. 같은 숫자가 나와서는 안된다. --> 같은 숫자가 있으면( count 함수 써서 숫자가 0인지로 확인)
# 없는 경우에만 append 하고 있는 경우에 해당하는 실행은 없으니까 if 하나만 쓴다.
# 또 다른 조건 2. 6개의 숫자를 골라야 한다. --> 6개 보다 많으면 그만

import random


def getNumber():
    return random.randrange(1, 46)


lotto = []
num = 0

print("로또 추첨을 시작합니다.\n")

while True:
    num = getNumber()

    if lotto.count(num) == 0:  # lotto 리스트 안에 같은 숫자가 있는지 확인 후
        # 없으면 그 개수가 0이면 리스트에 append 하기
        lotto.append(num)

    if len(lotto) >= 6:
        break

print("추첨된 로또 번호 ==>", end='')
lotto.sort()
for i in range(0, 6):
    print("%d " % lotto[i], end='')
