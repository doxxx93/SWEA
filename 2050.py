T = input()
a = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
b= " "
for i in range(len(T)):
    # ///////////////////////////////////////////////////////////////////////////////////
	b = T[i]
	print(a.index(b)+1, end =" ")