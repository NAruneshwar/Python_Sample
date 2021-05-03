class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        all_scores = {}
        for item in items:
            if item[0] not in all_scores.keys():
                all_scores[item[0]]=[]
            if len(all_scores[item[0]])<5:
                all_scores[item[0]].append(item[1])
            elif min(all_scores[item[0]])<item[1]:
                all_scores[item[0]].remove(min(all_scores[item[0]]))
                all_scores[item[0]].append(item[1])
        final_score = []
        print(all_scores)
        for i,j in all_scores.items():
            final_score.append([i,(sum(j)//5)])
        final_score.sort()
            
        return final_score