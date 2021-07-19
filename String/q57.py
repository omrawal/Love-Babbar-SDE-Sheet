#  all permutations of a string


class Solution:
    def rec(self, sinput, soutput, answer):
        # print(sinput,soutput)
        if(sinput == ''):
            answer.append(soutput)
            return
        for i in range(len(sinput)):
            self.rec(sinput[0:i]+sinput[i+1:], soutput+sinput[i], answer)

    def find_permutation(self, S):
        # Code here
        # s_list=list(S)
        answer = []
        self.rec(S, '', answer)
        # print(ans)
        return sorted(answer)
