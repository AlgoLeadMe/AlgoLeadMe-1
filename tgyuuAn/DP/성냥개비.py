import sys

def input(): return sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    count = int(input())
    DP = [[str(int(1e17)), "0"] for _ in range(count+1)]
    DP[0][0] = "0"

    for now_idx in range(count):
        if now_idx + 2 <= count:
            if int(DP[now_idx + 2][0]) > int(DP[now_idx][0] + "1"):
                DP[now_idx + 2][0] = DP[now_idx][0] + "1"

            if int(DP[now_idx + 2][1]) < int(DP[now_idx][1] + "1"):
                DP[now_idx + 2][1] = DP[now_idx][1] + "1"

        if now_idx + 3 <= count:
            if int(DP[now_idx + 3][0]) > int(DP[now_idx][0] + "7"):
                DP[now_idx + 3][0] = DP[now_idx][0] + "7"

            if int(DP[now_idx + 3][1]) < int(DP[now_idx][1] + "7"):
                DP[now_idx + 3][1] = DP[now_idx][1] + "7"

        if now_idx + 4 <= count:
            if int(DP[now_idx + 4][0]) > int(DP[now_idx][0] + "4"):
                DP[now_idx + 4][0] = DP[now_idx][0] + "4"

            if int(DP[now_idx + 4][1]) < int(DP[now_idx][1] + "4"):
                DP[now_idx + 4][1] = DP[now_idx][1] + "4"

        if now_idx + 5 <= count:
            if int(DP[now_idx + 5][0]) > int(DP[now_idx][0] + "3"):
                DP[now_idx + 5][0] = DP[now_idx][0] + "3"

            if int(DP[now_idx + 5][1]) < int(DP[now_idx][1] + "3"):
                DP[now_idx + 5][1] = DP[now_idx][1] + "3"
                
            if int(DP[now_idx + 5][0]) > int(DP[now_idx][0] + "2"):
                DP[now_idx + 5][0] = DP[now_idx][0] + "2"

            if int(DP[now_idx + 5][1]) < int(DP[now_idx][1] + "2"):
                DP[now_idx + 5][1] = DP[now_idx][1] + "2"
                
            if int(DP[now_idx + 5][0]) > int(DP[now_idx][0] + "5"):
                DP[now_idx + 5][0] = DP[now_idx][0] + "5"

            if int(DP[now_idx + 5][1]) < int(DP[now_idx][1] + "5"):
                DP[now_idx + 5][1] = DP[now_idx][1] + "5"

        if now_idx + 6 <= count:
            if int(DP[now_idx + 6][0]) > int(DP[now_idx][0] + "6"):
                DP[now_idx + 6][0] = DP[now_idx][0] + "6"

            if int(DP[now_idx + 6][1]) < int(DP[now_idx][1] + "6"):
                DP[now_idx + 6][1] = DP[now_idx][1] + "6"
                
            if int(DP[now_idx + 6][0]) > int(DP[now_idx][0] + "9"):
                DP[now_idx + 6][0] = DP[now_idx][0] + "9"

            if int(DP[now_idx + 6][1]) < int(DP[now_idx][1] + "9"):
                DP[now_idx + 6][1] = DP[now_idx][1] + "9"

            if int(DP[now_idx][0]) != 0 and int(DP[now_idx + 6][0]) > int(DP[now_idx][0] + "0"):
                DP[now_idx + 6][0] = DP[now_idx][0] + "0"

            if int(DP[now_idx][0]) != 0 and int(DP[now_idx + 6][1]) < int(DP[now_idx][1] + "0"):
                DP[now_idx + 6][1] = DP[now_idx][1] + "0"

        if now_idx + 7 <= count:
            if int(DP[now_idx + 7][0]) > int(DP[now_idx][0] + "8"):
                DP[now_idx + 7][0] = DP[now_idx][0] + "8"

            if int(DP[now_idx + 7][1]) < int(DP[now_idx][1] + "8"):
                DP[now_idx + 7][1] = DP[now_idx][1] + "8"

    print(int(DP[-1][0]), int(DP[-1][1]))