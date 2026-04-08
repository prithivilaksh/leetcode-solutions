# class Twitter:

#     def __init__(self):
#         self.follows=defaultdict(set)
#         self.posts=defaultdict(deque)
#         self.time=0

#     def postTweet(self, userId: int, tweetId: int) -> None:
#         postq=self.posts[userId]
#         self.time+=1
#         postq.append((self.time,tweetId))
#         if len(postq)>10: postq.popleft()
        

#     def getNewsFeed(self, userId: int) -> List[int]:
        
#         self.follows[userId].add(userId)
#         h=[]
#         for person in self.follows[userId]:
#             for time,tweetId in reversed(self.posts[person]):
#                 if len(h)==10 and time<h[0][0]: break
#                 heappush(h,(time,tweetId))
#                 if len(h)>10: heappop(h)  
        
#         return [tweetId for _,tweetId in sorted(h,reverse=True)]
        

#     def follow(self, followerId: int, followeeId: int) -> None:
#         self.follows[followerId].add(followeeId)

#     def unfollow(self, followerId: int, followeeId: int) -> None:
#         self.follows[followerId].discard(followeeId)



# # Your Twitter object will be instantiated and called as such:
# # obj = Twitter()
# # obj.postTweet(userId,tweetId)
# # param_2 = obj.getNewsFeed(userId)
# # obj.follow(followerId,followeeId)
# # obj.unfollow(followerId,followeeId)

# class Twitter:

#     def __init__(self):
#         self.follows=defaultdict(set)
#         self.posts=defaultdict(list)
#         self.time=0

#     def postTweet(self, userId: int, tweetId: int) -> None:
#         postlist=self.posts[userId]
#         self.time+=1
#         postlist.append((self.time,tweetId))        

#     def getNewsFeed(self, userId: int) -> List[int]:
        
#         self.follows[userId].add(userId)
#         h,res=[],[]
#         for person in self.follows[userId]:
#             postlist=self.posts[person]
#             if not postlist: continue
#             ind=len(postlist)-1
#             time,postId=postlist[ind]
#             heappush(h,(-time,postId,ind,person))
        
#         while h:
#             time,postId,ind,person=heappop(h)
#             res.append(postId)
#             if len(res)==10: return res
#             if ind>0: 
#                 postlist=self.posts[person]
#                 ind-=1
#                 time,postId=postlist[ind]
#                 heappush(h,(-time,postId,ind,person))

#         return res        

#     def follow(self, followerId: int, followeeId: int) -> None:
#         self.follows[followerId].add(followeeId)

#     def unfollow(self, followerId: int, followeeId: int) -> None:
#         self.follows[followerId].discard(followeeId)



# # Your Twitter object will be instantiated and called as such:
# # obj = Twitter()
# # obj.postTweet(userId,tweetId)
# # param_2 = obj.getNewsFeed(userId)
# # obj.follow(followerId,followeeId)
# # obj.unfollow(followerId,followeeId)


# class Twitter:

#     def __init__(self):
#         self.follows=defaultdict(set)
#         self.posts=defaultdict(list)
#         self.time=0

#     def postTweet(self, userId: int, tweetId: int) -> None:
#         postlist=self.posts[userId]
#         self.time+=1
#         postlist.append((self.time,tweetId))        

#     def getNewsFeed(self, userId: int) -> List[int]:
        
#         self.follows[userId].add(userId)
#         h,res=[],[]
#         for person in self.follows[userId]:
#             postlist=self.posts[person]
#             if not postlist: continue
#             ind=len(postlist)-1
#             time,postId=postlist[ind]
#             heappush(h,(time,postId,ind,person))
#             if len(h)>10: heappop(h)

#         h=[(-a,b,c,d) for a,b,c,d in h]
#         heapify(h)
#         while h:
#             time,postId,ind,person=heappop(h)
#             res.append(postId)
#             if len(res)==10: return res
#             if ind>0: 
#                 postlist=self.posts[person]
#                 ind-=1
#                 time,postId=postlist[ind]
#                 heappush(h,(-time,postId,ind,person))

#         return res        

#     def follow(self, followerId: int, followeeId: int) -> None:
#         self.follows[followerId].add(followeeId)

#     def unfollow(self, followerId: int, followeeId: int) -> None:
#         self.follows[followerId].discard(followeeId)



# # Your Twitter object will be instantiated and called as such:
# # obj = Twitter()
# # obj.postTweet(userId,tweetId)
# # param_2 = obj.getNewsFeed(userId)
# # obj.follow(followerId,followeeId)
# # obj.unfollow(followerId,followeeId)


# class Twitter:

#     def __init__(self):
#         self.follows=defaultdict(set)
#         self.posts=defaultdict(list)
#         self.time=0

#     def postTweet(self, userId: int, tweetId: int) -> None:
#         postlist=self.posts[userId]
#         self.time+=1
#         postlist.append((self.time,tweetId))        
#         if len(postlist)>10: postlist.pop(0)

#     def getNewsFeed(self, userId: int) -> List[int]:
        
#         self.follows[userId].add(userId)
#         h,res=[],[]
#         for person in self.follows[userId]:
#             postlist=self.posts[person]
#             if not postlist: continue
#             ind=len(postlist)-1
#             time,_=postlist[ind]
#             heappush(h,(time,ind,person))
#             if len(h)>10: heappop(h)

#         h=[(-a,b,c) for a,b,c in h]
#         heapify(h)
#         while h:
#             time,ind,person=heappop(h)
#             postlist=self.posts[person]
#             res.append(postlist[ind][1])
#             if len(res)==10: return res
#             if ind>0: 
#                 ind-=1
#                 time,_=postlist[ind]
#                 heappush(h,(-time,ind,person))

#         return res        

#     def follow(self, followerId: int, followeeId: int) -> None:
#         self.follows[followerId].add(followeeId)

#     def unfollow(self, followerId: int, followeeId: int) -> None:
#         self.follows[followerId].discard(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)



import heapq


class Twitter:

    def __init__(self):
        self.cnt = 0
        self.tweets = {}
        self.following = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((self.cnt, tweetId))
        self.cnt += 1
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].pop(0)

    def getNewsFeed(self, userId: int) -> list[int]:
        heap = []

        for uid in self.following.get(userId, set()) | {userId}:
            if uid in self.tweets and self.tweets[uid]:
                idx = len(self.tweets[uid]) - 1
                t, tid = self.tweets[uid][idx]
                heapq.heappush(heap, (-t, tid, uid, idx))

        res = []
        while heap and len(res) < 10:
            _, tid, uid, idx = heapq.heappop(heap)
            res.append(tid)
            if idx > 0:
                t, tid = self.tweets[uid][idx - 1]
                heapq.heappush(heap, (-t, tid, uid, idx - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)