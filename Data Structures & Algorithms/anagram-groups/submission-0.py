class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Ek dictionary banayi jisme hum anagrams ko group karenge
        res = {} 
        
        for s in strs:
            # 1. Word ko sort kiya (e.g., "eat" -> "aet")
            # sorted(s) humein list deta hai ['a', 'e', 't'], isliye "".join() se wapas string banaya
            sorted_s = "".join(sorted(s))
            
            # 2. Check kiya ki kya ye sorted version pehle se dictionary mein hai?
            if sorted_s in res:
                # Agar hai, toh usi group mein asli word (s) daal do
                res[sorted_s].append(s)
            else:
                # Agar nahi hai, toh ek naya group (list) shuru karo
                res[sorted_s] = [s]
                
        # 3. Humein sirf groups chahiye, toh dictionary ki values return kar di
        return list(res.values())