class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

      if len(s)!=len(t):
        return False
      hash_map={}
      for i in range(len(s)):
        hash_map[s[i]]=hash_map.get(s[i],0)+1
      for j in t:
        if j not in hash_map:
            return False

        hash_map[j]-=1

        if hash_map[j]<0:
            return False
      return True              


        