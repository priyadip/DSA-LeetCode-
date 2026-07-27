class Solution:
    def decodeString(self, s: str) -> str:
        self.i = 0 
        def dfs():
            ans = ''
            num = 0 
            while self.i <len(s):
                ch = s[self.i]
                if ch.isdigit():
                    num = num*10 + int(ch)
                elif ch == '[':
                    self.i += 1
                    ans += dfs()*num
                    num = 0
                elif ch == ']':
                    return ans
                else:
                    ans += ch
                self.i += 1
            return ans
        return dfs()


























        # stack, curr, num = [], '', 0

        # for ch in s:
        #     if ch.isdigit():
        #         num = num*10 + int(ch)
        #     elif ch == '[':
        #         stack.append((curr, num))
        #         curr, num = '', 0
        #     elif ch == ']':
        #         prev, repeat = stack.pop()
        #         curr = prev + curr*repeat
        #     else:
        #         curr += ch
        # return curr
        