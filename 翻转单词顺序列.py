'''
牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。同事Cat对Fish写的内容颇感兴趣，有一天他向Fish借来翻看，但却读不懂它的意思。例如，“student. a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了，正确的句子应该是“I am a student.”。Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？
'''

# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        return " ".join(s.split(' ')[::-1])



# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        
        def reverse(res):
            p1 = 0
            p2 = len(res)-1
            while p1 < p2:
                res[p1], res[p2] = res[p2], res[p1]
                p1 += 1
                p2 -= 1
            return res
        
        s_reverse = reverse(list(s))
        start = 0
        end = 0
        while end < len(s):
            if s_reverse[start]==" ":
                start += 1
                end += 1
            elif s_reverse[end]==" ":
                s_reverse[start:end] = reverse(s_reverse[start:end])
                start = end + 1
                end = end + 1
            elif end==len(s)-1:
                s_reverse[start:end+1] = reverse(s_reverse[start:end+1])
                end = end + 1
            else:
                end += 1
        return "".join(s_reverse)
        