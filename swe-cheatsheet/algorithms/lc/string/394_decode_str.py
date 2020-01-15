class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_num = 0
        cur_str = ''
        for c in s:
            if c == '[':
                stack.append([cur_num, cur_str])
                cur_num = 0
                cur_str = ''
            elif c == ']':
                num, prev_str = stack.pop()
                cur_str = prev_str + num * cur_str
            elif c.isdigit():
                cur_num = cur_num * 10 + int(c)
            else:
                cur_str += c

        return cur_str


print(Solution().decodeString(s='2[a3[b]]2[c]'))
