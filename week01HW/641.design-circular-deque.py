#
# @lc app=leetcode id=641 lang=python3
#
# [641] Design Circular Deque
#

# @lc code=start
class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.max_len = k
        self.cur_len = 0
        self.front, self.last = 0, 0
        self.queue = [0]*k
        
    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.max_len == self.cur_len:
            return False
        self.front = self.front - 1
        self.queue[self.front] = value
        self.cur_len += 1
        return True
        
    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.max_len == self.cur_len:
            return False
        self.queue[self.last] = value
        self.last = self.last + 1
        self.cur_len += 1
        return True
        
    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.cur_len == 0:
            return False
        self.front = self.front + 1
        self.cur_len -= 1
        return True
        
    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.cur_len == 0:
            return False
        self.last = self.last - 1
        self.cur_len -= 1
        return True
        
    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.cur_len == 0:
            return -1
        return self.queue[self.front]
        
    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.cur_len == 0:
            return -1
        return self.queue[self.last-1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.cur_len == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.cur_len == self.max_len
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
# @lc code=end

