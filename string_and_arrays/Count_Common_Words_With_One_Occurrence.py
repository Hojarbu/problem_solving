# https://leetcode.com/problems/count-common-words-with-one-occurrence/
"""
Count Common Words With One Occurrence
"""


def countWords(self, words1: List[str], words2: List[str]) -> int:
    a = Counter(words1)
    b = Counter(words2)
    a_list = []
    for k, v in a.items():
        if v == 1:
            a_list.append(k)

    for k, v in b.items():
        if v == 1:
            a_list.append(k)

    return len(a_list) - len(set(a_list))