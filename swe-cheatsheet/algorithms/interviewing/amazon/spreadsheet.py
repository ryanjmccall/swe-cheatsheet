class Solution:
    def __init__(self):
        self.num_to_char = {
            i: c for i, c in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        }
    def convert_to_title(self, n: int) -> str:
        pass

        """
        A
        
        Z
        AA
        
        
        AZ
        BA
        
        
        BZ
        
        ZZ
        
        AAA
        
        26 + 26*26 + 26^3 + ... 
        
        """
        title = []
        power = 26
        while n:
            remain = (n - 1) % power
            title.append(self.num_to_char[remain])
            n = (n - 1) // power

        return ''.join(reversed(title))


def t():
   s = Solution()
   print(s.convert_to_title(1))
   print(s.convert_to_title(456976))
   print(s.convert_to_title(28))

t()
