T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for i in range(T):
    # ///////////////////////////////////////////////////////////////////////////////////
	numbers = list(map(int, input().split())) 
	odd_nums = [num for num in numbers if num % 2 == 1]
	print("#{} {}".format(i+1, sum(odd_nums)))