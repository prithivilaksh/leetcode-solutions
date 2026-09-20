# class StockPrice:

#     def __init__(self):
#         self.mp={}
#         self.l=[]
#         self.mx=[]
#         self.mi=[]

#     def update(self, timestamp: int, price: int) -> None:
#         self.mp[timestamp]=price
#         heappush(self.l,(-timestamp,price))
#         heappush(self.mx,(-price,timestamp))
#         heappush(self.mi,(price,timestamp))

#     def current(self) -> int:
#         while True:
#             ts,p=self.l[0]
#             ts=-ts
#             if self.mp[ts]==p: return p
#             heappop(self.l)


#     def maximum(self) -> int:
#         while True:
#             p,ts=self.mx[0]
#             p=-p
#             if self.mp[ts]==p: return p
#             heappop(self.mx)    

#     def minimum(self) -> int:
#         while True:
#             p,ts=self.mi[0]
#             if self.mp[ts]==p: return p
#             heappop(self.mi)        


# # Your StockPrice object will be instantiated and called as such:
# # obj = StockPrice()
# # obj.update(timestamp,price)
# # param_2 = obj.current()
# # param_3 = obj.maximum()
# # param_4 = obj.minimum()


class StockPrice:

    def __init__(self):
        self.mp={}
        self.mx=[]
        self.mi=[]
        self.curr_ts=0

    def update(self, timestamp: int, price: int) -> None:
        self.mp[timestamp]=price
        self.curr_ts=max(self.curr_ts,timestamp)
        heappush(self.mx,(-price,timestamp))
        heappush(self.mi,(price,timestamp))

    def current(self) -> int:
        return self.mp[self.curr_ts]

    def maximum(self) -> int:
        while True:
            p,ts=self.mx[0]
            if self.mp[ts]==-p: return -p
            heappop(self.mx)    

    def minimum(self) -> int:
        while True:
            p,ts=self.mi[0]
            if self.mp[ts]==p: return p
            heappop(self.mi)        


# # Your StockPrice object will be instantiated and called as such:
# # obj = StockPrice()
# # obj.update(timestamp,price)
# # param_2 = obj.current()
# # param_3 = obj.maximum()
# # param_4 = obj.minimum()


# from sortedcontainers import SortedDict,SortedList
# class StockPrice:

#     def __init__(self):
#         self.time_to_prices = SortedDict()
#         self.prices = SortedList()

#     def update(self, timestamp: int, price: int) -> None:
#         if timestamp in self.time_to_prices:
#             prev_price = self.time_to_prices[timestamp]
#             self.prices.remove(prev_price)

#         self.prices.add(price)
#         self.time_to_prices[timestamp] = price

#     def current(self) -> int:
#         return self.time_to_prices.peekitem(-1)[1]

#     def maximum(self) -> int: return self.prices[-1]

#     def minimum(self) -> int: return self.prices[0]