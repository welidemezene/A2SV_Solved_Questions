class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = 0
        list1 = []
        for n in nums:
            if n % 2 == 0:
                ans+=n
        for n in queries:
            if nums[n[1]] % 2 == 0:
                if n[0]%2==0:
                    
                    ans += n[0]
                    nums[n[1]] += n[0]
                else:
                    ans -= nums[n[1]]
                    
                    nums[n[1]]+= n[0]   
            else:
                if n[0]%2==0:
                    
                    nums[n[1]]+= n[0]   
                    
                else:
                    
                    ans += n[0] + nums[n[1]]
                    nums[n[1]] += n[0]
            list1.append(ans)
        return list1    
                    


        