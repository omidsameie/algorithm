'''
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
'''
class Solution:
    def split(self,string):
        return [char for char in string]
      
    def reverse(self, word):
        l , r = 0 , len(word)-1
        while l<r:
            word[l],word[r] = word[r],word[l]
            l,r = l+1,r-1
        return word
      
    def reverseWords(self, s) :
        s = self.split(s)
        j = 0
        aux = []
        s_2 = []
        while j<len(s):
            if s[j]!=' ':
                aux.append(s[j])
            else:
                aux= self.reverse(aux)
                aux = "".join(aux)
                aux += " "
                s_2.append(aux)
                aux = []
            j +=1

        aux= self.reverse(aux)
        aux = "".join(aux)
        s_2.append(aux)
        s = "".join(s_2)
        return s 
