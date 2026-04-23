class Solution:
    def encode(self, strs: list[str]) -> str:
        # Optimization: List comprehension + join use karo 
        # Yeh memory mein baar-baar nayi string banane se bachaata hai
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            # Length nikaali
            length = int(s[i:j])
            
            # Word extract kiya aur result mein daala
            # s[j+1 : j+1+length] se direct slicing
            res.append(s[j+1 : j+1+length])
            
            # Pointer ko agle segment ke start par move kiya
            i = j + 1 + length
            
        return res