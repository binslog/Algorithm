

# 간단한 소인수분해

# T = int(input())
# for test_case in range(1, T+1):
#     # 숫자 입력
#     N = int(input())
#     # 나눠질 리스트
#     divide_list = [2, 3, 5, 7, 11]
#     counts = [0] * 5
#     for i in range(5):
#         while N % divide_list[i] == 0:
#             counts[i] += 1
#             N //= divide_list[i]
#     print(f'#{test_case}', end=' ')
#     print(*counts)

#------------------------------------------------------------


# 파리 퇴치

# T = int(input())
# for test_case in range(1, T+1):
#     N, M = map(int, input().split())
#     matrix = [list(map(int, input().split())) for _ in range(N)]
#     max_kill = -1
#     # 2차원 배열 반복
#     for x in range(N-M+1):
#         for y in range(N-M+1):
#             tmp = 0
#             for i in range(M):
#                 tmp += sum(matrix[x+i][y:y+M])
#             if max_kill < tmp:
#                 max_kill = tmp
#     print(f'#{test_case} {max_kill}')


#-------------------------------------------------------------

# 스도쿠검증
# 7 3 6 4 2 9 5 8 1
# 5 8 9 1 6 7 3 2 4
# 2 1 4 5 8 3 6 9 7
# 8 4 7 9 3 6 1 5 2
# 1 5 3 8 4 2 9 7 6
# 9 6 2 7 5 1 8 4 3
# 4 2 1 3 9 8 7 6 5
# 3 9 5 6 7 4 2 1 8
# 6 7 8 2 1 5 4 3 9

# def check_row():
#     # 한 줄이 [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     # 첫번째 : set 함수 사용
#     # for i in range(9):
#     #     if len(set(matrix[i])) != 9:
#     #         return False
#
#     # 두번째 : count 배열 사용
#     # matrix[i][j] 의 숫자의 count 배열에 ++
#     check = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#     for i in range(9):
#         count = [0]*10
#         for j in range(9):
#             count[matrix[i][j]] += 1
#         if count != check:
#             return False
#     return True
#
#
# def check_col():
#     for i in range(9):
#         tmp = []
#         for j in range(9):
#             tmp.append(matrix[j][i])
#         if len(set(tmp)) != 9:
#             return False
#     return True
#
#
# def check_block():
#     for x in range(0, 9, 3):
#         for y in range(0, 9, 3):
#             tmp = []
#             for i in range(x, x+3):
#                 for j in range(y, y+3):
#                     tmp.append(matrix[i][j])
#             if len(set(tmp)) != 9:
#                 return False
#     return True
#
#
# T = int(input())
# for test_case in range(1, T+1):
#     matrix = [list(map(int, input().split())) for _ in range(9)]
#
#     # 가로 검증
#     if check_row() is False:
#         print(f'#{test_case} 0')
#         continue
#
#     # 세로 검증
#     if check_col() is False:
#         print(f'#{test_case} 0')
#         continue
#
#     # 박스 검증
#     if check_block() is False:
#         print(f'#{test_case} 0')
#         continue
#
#     # 모두 괜찮으면 print1
#     print(f'#{test_case} 1')


# 스도쿠 검증 2
# T = int(input())
# for test_case in range(1, T+1):
#     matrix = [list(map(int, input().split())) for _ in range(9)]
#     answer = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#     flag = 0
#     for i in range(9):
#         count_row = [0] * 10
#         count_col = [0] * 10
#         count_block = [0] * 10
#         for j in range(9):
#             count_row[matrix[i][j]] += 1
#             count_col[matrix[j][i]] += 1
#             count_block[matrix[(i//3)*3+j//3][(i%3)*3+j%3]] += 1
#         if count_row != answer or count_col != answer or count_block != answer:
#             flag = 0
#             break
#         flag = 1
#     print(f'#{test_case} {flag}')

#----------------------------------------------------------------
# 삼성시의 버스 노선
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lines = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    cs = [int(input()) for _ in range(P)]
    count = [0] * P
    for p in range(P):
        for i in range(N):
            if lines[i][0] <= cs[p] <= lines[i][1]:
                count[p] += 1
    print(f'#{test_case}', *count)

# 삼성시의 버스 노선 2
# T = int(input())
# for test_case in range(1, T+1):
#     N = int(input())
#     lines = [list(map(int, input().split())) for _ in range(N)]
#     count = [0] * 5001
#     for line in lines:
#         for i in range(line[0], line[1]+1):
#             count += 1
#     P = int(input())
#     print(f'#{test_case}', end=' ')
#     for _ in range(P):
#         c = int(input())
#         print(count[c], end=' ')
#     print()

#-------------------------------------------------------------------
# 쇠막대기 자르기

# T = int(input())
# for test_case in range(1, T+1):
#     tc = input()
#     stack = []
#     count = 0
#     for i in range(len(tc)):
#         if tc[i] == '(':
#             stack.append('(')
#         else:
#             # 레이저 일 때
#             if tc[i-1] == '(':
#                 stack.pop()
#                 count += len(stack)
#             # 아닐 때
#             else:
#                 stack.pop()
#                 count += 1
#     print(f'#{test_case} {count}')


# 쇠막대기 자르기 2
# T = int(input())
# for test_case in range(1, T+1):
#     tc = input()
#     stack = count = 0
#     for i in range(len(tc)):
#         if tc[i] == '(':
#             stack += 1
#         else:
#             # 레이저라면
#             if tc[i-1] == '(':
#                 stack -= 1
#                 count += stack
#             else:
#                 stack -= 1
#                 count += 1
#     print(f'#{test_case} {count}')











