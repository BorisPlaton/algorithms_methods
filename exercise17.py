n = int(input())
nums = [int(i) for i in input().split()]
ans = [0, ]

for i in range(n+1):
    if i == 0:
        continue
    elif i == 1:
        ans.append(nums[i-1])
    else:
        ans.append(nums[i-1] + max(ans[i-1], ans[i-2]))

print(ans[-1])
