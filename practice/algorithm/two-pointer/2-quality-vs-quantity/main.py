def solve():
    n = int(input())
    nums = list(map(int, input().split(' ')))
    nums.sort()
    
    redCnt = 1
    red = nums[-1]
    blueCnt = 1
    blue = nums[0]
    while redCnt + blueCnt < n:
        if red <= blue:
            redCnt+=1
            red+=nums[-redCnt]
        elif blueCnt <= redCnt:
            blue+=nums[blueCnt]
            blueCnt+=1
        
        if red > blue and redCnt < blueCnt:
            print("YES")
            return
             
    print("NO")

tests = int(input())
for _ in range(tests):
	solve()