#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#"""
#QUESTION 1
#"""
def filter_string(s: str) -> str:
    # WRITE YOUR BRILLIANT CODE HERE
    news = s[0:2]
    for i in range(2, len(s)):
        # Do not append if the previous chars are the same
        if s[i] != s[i - 1] or s[i] != s[i - 2]:
            news += s[i]
    return news


def solution(S):
	Three_letters = S[0:2]
	for i in range(2, len(S)):
		if S[i] != S[i-1] or S[i] != S[i-2]:
			Three_letters += S[i]
	return Three_letters

if __name__ == '__main__':
    s = input()
    res = solution(s)
    print(res)
	

