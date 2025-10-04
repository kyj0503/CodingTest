import sys
input = sys.stdin.readline

text = input().rstrip()
pattern = input().rstrip()
t = len(text)
p = len(pattern)
cnt = i = 0

while i < t - p + 1:
    start_idx = i
    for letter in pattern:
        if letter != text[start_idx]:
            i += 1
            break
        else:
            start_idx += 1
    else:
        cnt += 1
        i += p

print(cnt)