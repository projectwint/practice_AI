#https://ctdlog.tistory.com/24
#2차원 리스트 입력 받기 정리 by. seowon1177

n, m = map(int, input().split())
#리스트의 크기를 입력받는다.
#n행, m열(행의 개수는 중요해보이지만, 파이썬에서는 입력할 때 개수가 중요하지 않아서 열의 개수는 크게 중요하지 않다.)

#1
mylist = [0 for _ in range(n)]
for i in range(n):
    mylist[i] = list(map(int, input().split()))
#1차원 리스트 mylist에 0으로 초기화
#for문으로 한 줄씩 받아서 i번째 인덱스를 입력받은 1차원 리스트로 할당
#(c.f파이썬에서 =은 대입 연산자가 아니라 할당 연산자)


#2
mylist = []
for i in range(n):
    mylist.append(list(map(int, input().split())))
#for문으로 한 줄씩 입력 받은 값을 mylist에 append한다. 


#3
mylist = [list(map(int, input().split())) for _ in range(n)]
#위에 나온 선언, 초기화, 입력, append를 한 줄로 축약

print(mylist)
