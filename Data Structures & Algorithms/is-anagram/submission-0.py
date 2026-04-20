class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Step 1: Length check (Jo aapne sahi socha tha)
        if len(s) != len(t):
            return False
        
        # Step 2: Dictionaries initialize karna
        countS, countT = {}, {}
        
        # Step 3: 's' ke characters ginna
        for char in s:
            countS[char] = 1 + countS.get(char, 0)
            
        # Step 4: 't' ke characters ginna (Yeh miss ho gaya tha)
        for char in t:
            countT[char] = 1 + countT.get(char, 0)
            
        # Step 5: Dono ki ginti compare karna
        return countS == countT
        