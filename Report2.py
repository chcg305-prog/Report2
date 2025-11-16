# 1.     반사성 검사
def is_reflective (matrix) :
    for i in range(5):
        if matrix[i][i] != 1 :
            return False
    return True

# 2.    대칭성 검사
def is_symmetric(matrix):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] != matrix[j][i] :
                return False
    return True

# 3.    추이성 검사
def is_transitive (matrix):
    for k in range(5):
        for i in range(5):
            for j in range(5):
                if ((matrix[i][k] == 1 and matrix[k][j] == 1) and matrix[i][j] != 1) :
                    return False
    return True     
       
# 4.    동치류 판단
def is_equal_type(matrix):
    if is_reflective(matrix) and is_symmetric(matrix) and is_transitive(matrix) :
                print("동치입니다, 이어서 동치류를 원소별로 출력합니다! ")
                for i in range(5):
                    print(f"[{i+1}] ", end=" -> ")
                    current_class = set()
                    for j in range(5):
                        if matrix[i][j] == 1:
                            current_class.add(j)
                    for element in sorted(current_class):
                        print(f"{element+1}", end=" ")
                    print()
                return True
    else :
        print("\n 해당 관계는 동치 관계가 아닙니다,.")
        return False
    


# 5.    폐포 생성

# 5.1 반사 폐포

def reflective_closure(matrix):
    if is_reflective(matrix) == False:
        print("\n=== 반사 폐포 전 ===")
        for row in matrix:
            print(*row)

        for i in range(5) :
            matrix[i][i] = 1
        
        print("\n=== 반사 폐포 후 ===")
        for row in matrix:
            print(*row)

        print("동치 판별을 이어서 진행합니다.")
        is_equal_type(matrix)
        return True
    else :
        print("이미 반사성을 가집니다.")
        return True
    
# 5.2 대칭 폐포

def symmetric_closure(matrix):
    if (is_symmetric(matrix) == False) :
        print("\n=== 대칭 폐포 전 ===")
        for row in matrix:
            print(*row)

        for i in range(5):
            for j in range(5):
                if (matrix[i][j] == 1):
                    matrix[j][i] = 1
        print("\n=== 대칭 폐포 후 ===")
        for row in matrix:
            print(*row)
        print("동치 판별을 이어서 진행합니다.")
        is_equal_type(matrix)
        return True
    
    
    else:
        print("이미 대칭성을 가집니다.")
        return True 
            
# 5.3 추이 폐포
       
def transitive_closure(matrix):
    if (is_transitive(matrix) == False) :
        print("\n=== 추이 폐포 전 ===")
        for row in matrix:
            print(*row)
       
        for k in range(5):
            for i in range(5):
                for j in range(5):
                    if (matrix[i][k] == 1 and matrix[k][j] == 1):
                        matrix[i][j] = 1
        print("\n=== 추이 폐포 후 ===")
        for row in matrix:
            print(*row)

        print("동치 판별을 이어서 진행합니다.")
        is_equal_type(matrix)

        return True
    else :
        print("이미 추이성을 가집니다.")
        return True
             


    print("해당 관계는 동치가 아닙니다.")  
    return False









matrix = []

print ( "5X5 정방행렬을 입력하세요. 각 행은 5개의 숫자로 공백 하나를 간격으로 이루어집니다.")

for i in range(5) :
    while True:
        row_input = input(f"{i+1}번째 행 입력 : ")

        try :
            row = list(map(int, row_input.split()))
        except ValueError :
            print(" 숫자만 가능합니다. ")
            continue

        
        if len(row) != 5:
            print("5개의 값을 입력하서야 합니다. 길이에 문제가 있습니다.")
            continue

        matrix.append(row)
        break

print("\n === 입력된 관계 행렬 ===")
for row in matrix:
    print(*row)

if not is_equal_type(matrix):
    reflective_closure(matrix)
    symmetric_closure(matrix)
    transitive_closure(matrix)
    print("\n 폐포 적용 후 동치 관계 재 체크")
    is_equal_type(matrix)
