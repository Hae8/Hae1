N = int(input()) # 5

#     *     # i = 1, " " : 4, "*" : 1
#    ***    # i = 2, " " : 3, "*" : 3
#   *****   # i = 3, " " : 2, "*" : 5
#  *******  # i = 4, " " : 1, "*" : 7
# ********* # i = 5, " " : 0, "*" : 9
#  *******  # i = 6, " " : 1, "*" : 7
#   *****   # i = 7, " " : 2, "*" : 5
#    ***    # i = 8, " " : 3, "*" : 3
#     *     # i = 9, " " : 4, "*" : 1

for i in range(1, 2 * N):
    space = abs(i-N)
    star = 2 * (N - space) - 1
    print(" " * space + "*" * star)