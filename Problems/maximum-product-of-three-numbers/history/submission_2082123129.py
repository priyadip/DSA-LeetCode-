class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        fm = sm = tm = float('-inf')
        fmi = smi = float('inf')
        for x in nums:
            if x>= fm:
                tm = sm
                sm = fm
                fm = x
            elif x>=sm:
                tm = sm
                sm = x
            elif x > tm:
                tm = x

            if x <= fmi:
                smi = fmi
                fmi = x
            elif x < smi:
                smi = x
        return max(fmi*smi*fm, fm*sm*tm)
        #return fm*sm*tm if (fm*sm*tm) > (fmi*smi*fm) else fmi*smi*fm
            
                
        