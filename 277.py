# class Solution:
#     def findCelebrity(self, n: int) -> int:

#         # problem:
#         #     1) celebrities labeled from 0 to n-1
#         #     2) x is a celebrity if everone knows x but x does not know anyone
#         #     3) knows(i,j) returns true if person i knows person j
#         #     4) return the celebrity if exists else -1
#         #     5) 2 <= n <= 100
#         #     6) solve it in O(3*n)
        
#         # idea:
#         #     1) if knows(i,j) is true, i cannot be a celebrity and j is a candidate
#         #     2) if knows(i,j) is false, j cannot be a celebrity and i is a candidate
#         #     2) if j is a celebrity then knows(i,j) = True and knows(j,i) = False for all i except j
#         #     3) initially everyone will be a "candidate"
#         #     4) as we iterate remove the "candidates" and add it to "not celebrity"
        
#         celeb_cand=set(range(n))
#         not_celeb=set()

#         while len(celeb_cand)>1:
#             i,j=celeb_cand.pop(),celeb_cand.pop()
#             if knows(i,j): celeb_cand.add(j);not_celeb.add(i)
#             else: celeb_cand.add(i);not_celeb.add(j)
        
#         final_cand=celeb_cand.pop()
#         return final_cand if all(knows(i,final_cand) and not knows(final_cand,i) for i in range(n) if i!=final_cand) else -1


# class Solution:
#     def findCelebrity(self, n: int) -> int:

#         # problem:
#         #     1) celebrities labeled from 0 to n-1
#         #     2) x is a celebrity if everone knows x but x does not know anyone
#         #     3) knows(i,j) returns true if person i knows person j
#         #     4) return the celebrity if exists else -1
#         #     5) 2 <= n <= 100
#         #     6) solve it in O(3*n)
        
#         # idea:
#         #     1) if knows(i,j) is true, i cannot be a celebrity and j is a candidate
#         #     2) if knows(i,j) is false, j cannot be a celebrity and i is a candidate
#         #     2) if j is a celebrity then knows(i,j) = True and knows(j,i) = False for all i except j
#         #     3) initially everyone will be a "candidate"
#         #     4) as we iterate remove the "candidates" and add it to "not celebrity"
        
#         celeb_cand=set(range(n))

#         while len(celeb_cand)>1:
#             i,j=celeb_cand.pop(),celeb_cand.pop()
#             if knows(i,j): celeb_cand.add(j)
#             else: celeb_cand.add(i)
        
#         final_cand=celeb_cand.pop()
#         return final_cand if all(knows(i,final_cand) and not knows(final_cand,i) for i in range(n) if i!=final_cand) else -1


class Solution:
    def findCelebrity(self, n: int) -> int:

        # problem:
        #     1) celebrities labeled from 0 to n-1
        #     2) x is a celebrity if everone knows x but x does not know anyone
        #     3) knows(i,j) returns true if person i knows person j
        #     4) return the celebrity if exists else -1
        #     5) 2 <= n <= 100
        #     6) solve it in O(3*n)
        
        # idea:
        #     1) if knows(i,j) is true, i cannot be a celebrity and j is a candidate
        #     2) if knows(i,j) is false, j cannot be a celebrity and i is a candidate
        #     2) if j is a celebrity then knows(i,j) = True and knows(j,i) = False for all i except j
        #     3) initially everyone will be a "candidate"
        #     4) as we iterate remove the "candidates" and add it to "not celebrity"
        
        final_cand=0
        for i in range(1,n):
            if knows(final_cand,i): 
                final_cand=i

        return final_cand if all(knows(i,final_cand) and not knows(final_cand,i) for i in range(n) if i!=final_cand) else -1