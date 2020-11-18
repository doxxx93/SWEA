n = input()

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
a = list(n)
sum = 0

for i in range(len(a)):
    sum += int(a[i])
    
print(sum)