# import sys
# sys.stdin = open("input.txt", "r")

def solve():
    T = int(input().strip())
    for t in range(1, T + 1):
        d, m, q, y = map(int, input().split())   # 1일, 1달, 3달, 1년 요금
        plan = list(map(int, input().split()))   # 12개월 이용 계획 (일수)

        # dp[i] = i월부터 12월까지 최소 비용 (i: 1..12)
        # i=12에서 dp[i+3] = dp[15]까지 접근하므로 길이 16 필요 (0..15)
        dp = [0] * 16

        for i in range(12, 0, -1):
            days = plan[i - 1]
            if days == 0:
                dp[i] = dp[i + 1]
            else:
                cost_one_or_month = min(days * d, m) + dp[i + 1]
                cost_three_months = q + dp[i + 3]
                dp[i] = min(cost_one_or_month, cost_three_months)

        answer = min(dp[1], y)
        print(f"#{t} {answer}")

if __name__ == "__main__":
    solve()
