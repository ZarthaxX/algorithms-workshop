def solve():
    n = int(input())
    nums = list(map(int, input().split(' ')))

    aliceCnt = 0
    alice = 0
    bobCnt = 0
    bob = 0
    while aliceCnt + bobCnt < n:
       if alice < bob:
           alice += nums[aliceCnt]
           aliceCnt+=1
       elif bob < alice:
           bobCnt+=1
           bob += nums[-bobCnt]
       else:
           if aliceCnt + bobCnt == n - 1:
            alice += nums[aliceCnt]
            aliceCnt+=1
           else:
            alice += nums[aliceCnt]
            aliceCnt+=1
            bobCnt+=1
            bob += nums[-bobCnt]
              
              
    print(aliceCnt,bobCnt)
             
    

solve()