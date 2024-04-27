|   layout  |   title | date | author  | tag |
|  ----  | ----  | ---- | ---- | ---- |
|  post | LinkedList |  2020-12-01 | Shawn_Song  | leetcode
-------

# 链表

## Recap
* 141 Linked List Cycle
这道题使用快慢指针，根据快指针是否“套圈”慢指针来判断是否形成环。  

## Content
* 160 Intersectionof Two Linked Lists(Recap 141)
## 链表反转
* 206.Reverse Linked List
* 92.Reverse Linked List II
* 25.Reverse Nodes in k-Group

## 链表排序
* 148 Sort List
* 21 Merge Two Sorted Lists
* [23. 合并K个升序链表](#23-合并K个升序链表hard)

* [237. 删除链表中的节点](#237-删除链表中的节点easy)
* 83 Remove Duplicates from Sorted List(Recap 26、80)
* [82. 删除排序链表中的重复元素II](#82删除排序链表中的重复元素IImedium)
* 19 Remove Nth Node From End of List
* 24 Swap Nodes in Pairs
* 445 Add Two  Numbers II
* 234 Palindrome Linked List(Recap 125、680 in 对撞双指针)
* 725 Split Linked List in Parts
* 328 Odd Even Linked List
* 138.Copy List with Random Pointer
* [2. 两数相加](#2-两数相加medium)

## 160. Intersection of Two Linked Lists(Easy)

[https://leetcode-cn.com/problems/intersection-of-two-linked-lists/](https://leetcode-cn.com/problems/intersection-of-two-linked-lists/)


### Description
编写一个程序，找到两个单链表相交的起始节点。

### Solution(Two Pointers)
```python
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB: return None
        
        def length(head: ListNode):
            n = 0
            while head:
                head = head.next
                n += 1
            return n
        # 计算两个链表长度
        len1, len2 = length(headA), length(headB)
        # 将第一个链表永远保持为长链表
        if len1 < len2:
            headA, headB = headB, headA
        # 让第一个链表先走多出第二个链表的长度
        for _ in range(abs(len1 - len2)):
            headA = headA.next
        # 两个指针同时遍历相同长度的链表，相等则找到相交点
        while headA != headB:
            headA, headB = headA.next, headB.next
        return headA
```

**思路**：首先想到用双指针分别遍历两个链表，指针元素相同时则找到相交点。但只有两个链遍遍历时长度相同才能把保证。所以：
1. 计算两个链表长度，并算出长链表比短链表多的长度n。
2. 让长链表的头指针先行n步，和短链表处在同一起点。
3. 开始用双指针遍历两个链表。
4. 指针元素相同时，找到相交点，返回当前元素。


## 206. Reverse Linked List(Easy)

[https://leetcode-cn.com/problems/reverse-linked-list/](https://leetcode-cn.com/problems/reverse-linked-list/)

### Description
反转一个单链表。

### Solution One(循环迭代)
```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return
        pre = None
        cur = head
        while cur:
            # 下一个反转节点
            ori_next = cur.next
            # 将当前节点的next指针指向前一个节点
            cur.next = pre
            # 然后将“前一节点”移动到当前节点
            pre = cur
            # 当前节点进行移动
            cur = ori_next
        return pre
```

**思路**：从头开始遍历对每个节点进行反转操作，该操作主要分为三步：  
1. 将当前节点的next指针指向前一个节点。
2. 将“前一个节点”变成当前节点。
3. 当前节点向后移动。

### Solution Two(递归)
```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        nextNode = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return nextNode
```
**思路**：递归的方法稍微有一点难理解，也是从头开始递归到尾部，达到尾部就是终止条件，即head.next == None。然后从尾部开始一个个反转节点，计算之前累计的递归函数，主要有两步：
1. 将当前节点下一个节点的next指针指向自己。
2. 将当前指针的next指针指向空，这样上一层递归函数可以返回值，并且执行反转操作。


## 92.Reverse Linked List II(Medium)

[https://leetcode-cn.com/problems/reverse-linked-list-ii/](https://leetcode-cn.com/problems/reverse-linked-list-ii/)

### Solution
```python
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        pre, cur = dummy, head
        for _ in range(1, left):
            pre = cur
            cur = cur.next

        first, last = pre, cur
        for _ in range(left, right + 1):
            ori_next = cur.next
            cur.next = pre
            pre = cur
            cur = ori_next
            
        first.next = pre
        last.next = cur
        return dummy.next
```
思路：首先找到反转起点left，在进行链表反转。


## 25.Reverse Nodes in k-Group(Hard)

[https://leetcode-cn.com/problems/reverse-nodes-in-k-group/](https://leetcode-cn.com/problems/reverse-nodes-in-k-group/)

### Solution
```python
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        left, right = dummy, head
        cnt = 0
        while right:
            cnt += 1
            right = right.next
            if cnt % k == 0:
                # reverse 函数中的left是需要反转链表头节点的前一个节点
                # right是需要反转链表尾节点的后一个节点
                left = self.reverse(left, right)
        return dummy.next

    def reverse(self, left, right):
        pre, cur = left, left.next
        first, last = pre, cur
        while cur != right:
            ori_next = cur.next
            cur.next = pre
            pre = cur
            cur = ori_next
        first.next = pre
        last.next = right
        return last
```

## 148 Sort List(Medium)

[https://leetcode-cn.com/problems/sort-list/](https://leetcode-cn.com/problems/sort-list/)

### Description
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

### Solution
```python
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        slower = head
        faster = head.next
        while faster and faster.next:
            slower = slower.next
            faster = faster.next.next
        mid = slower.next
        slower.next = None
        left = self.sortList(head)
        right = self.sortList(mid)
            
        return self.mergeList(left, right)
    
    def mergeList(self, left, right):
        dummy = ListNode(0)
        p = dummy
        while left and right:
            if left.val < right.val:
                p.next = left
                left = left.next
            else:
                p.next = right
                right = right.next
            p = p.next
        p.next = left if left else right
        return dummy.next
```
思路：归并排序的思想。

## 21. Merge Two Sorted Lists(Easy)

[https://leetcode-cn.com/problems/merge-two-sorted-lists/](https://leetcode-cn.com/problems/merge-two-sorted-lists/)

### Description
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

### Solution(双指针遍历)
```python
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1

        p = ListNode()
        head = p
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
                p = p.next
            else:
                p.next = l2
                l2 = l2.next
                p = p.next
        p.next = l1 if l1 else l2
        return head.next
```

**思路**：创建一个新的头指针，然后遍历两个链表，依次把小的元素所在的链表接入创建的指针。边界情况一个是其中一个链表为空，另一个情况是两个链表长度不一，一个链表会优先遍历完，直接把另一个链表接到最后即可。

## 23. 合并K个升序链表(Hard)

[https://leetcode-cn.com/problems/merge-k-sorted-lists/](https://leetcode-cn.com/problems/merge-k-sorted-lists/)

### Description
给你一个链表数组，每个链表都已经按升序排列。
请你将所有链表合并到一个升序链表中，返回合并后的链表。

### Solution
```python
class Solution:
    def mergeKLists(self , lists ):
        # write code here
        n = len(lists)
        if n == 0: return None
        if n == 1: return lists[0]
        mid = n // 2
        left = lists[:mid]
        right = lists[mid:]
        left_linked = self.mergeKLists(left)
        right_linked = self.mergeKLists(right)

        return self.mergeTwoLists(left_linked, right_linked)
        
    def mergeTwoLists(self, p1, p2):
        if not p1: return p2
        if not p2: return p1
        p = ListNode(0)
        dummy = p
        while p1 and p2:
            if p1.val < p2.val:
                p.next = p1
                p1 = p1.next
                p = p.next
            else:
                p.next = p2
                p2 = p2.next
                p = p.next
        p.next = p1 if p1 else p2
        return dummy.next
```
思路：归并排序思路，将k个链表向下分治为合并两个链表合并排序的子问题，再向上合并。


## 237. 删除链表中的节点(Easy)

[https://leetcode-cn.com/problems/delete-node-in-a-linked-list/](https://leetcode-cn.com/problems/delete-node-in-a-linked-list/)

### Solution
```python
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val, node.next = node.next.val, node.next.next
```

## 83. Remove Duplicates from Sorted List(Easy)

[https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/)

### Description
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

### Solution(快慢指针)
```python
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return
        slower, faster = head, head
        while faster:
            while faster and slower.val == faster.val:
                faster = faster.next
            slower.next = faster
            slower = faster
            
        return head
```

**思路**：和第26题唯一不一样的地方就是数据结构从列表换成了链表，但是解题思路是一样的，设计一个快指针和慢指针。快指针遇到和慢指针指向元素值一样则跳过，大于慢指针则更新慢指针，快指针继续向前搜索。  


## 82.删除排序链表中的重复元素II(Medium)

[https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/)

### Description
存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除链表中所有存在数字重复情况的节点，只保留原始链表中 没有重复出现 的数字。
返回同样按升序排列的结果链表。

### Solution
```python
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return
        dummy = ListNode()
        dummy.next = head
        a = dummy
        b = head
        while b and b.next:
            if a.next.val == b.next.val:
                while b and b.next and a.next.val == b.next.val:
                    b = b.next
                a.next = b.next
                b = b.next
            else:
                a = a.next
                b = b.next
        return dummy.next
```
思路：比较`.next.val`





## 24. Swap Nodes in Pairs(Medium)

[https://leetcode-cn.com/problems/swap-nodes-in-pairs/](https://leetcode-cn.com/problems/swap-nodes-in-pairs/)

### Description
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

### Solution(Use dummy node)
```python
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode()
        dummy.next = head
        p = dummy
        while head and head.next:
            first = head
            second = head.next
            p.next = second
            first.next = second.next
            second.next = first
            p = first
            head = p.next
        return dummy.next
```
**思路**：两两交换，注意核心是设置哨兵节点当作第二个节点的头节点。

## 445.Add Two Numbers II(Medium)

[https://leetcode-cn.com/problems/add-two-numbers-ii/](https://leetcode-cn.com/problems/add-two-numbers-ii/)

### Description
给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
你可以假设除了数字 0 之外，这两个数字都不会以零开头。
要求：
如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。

### Solution(Naive)
```python
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        first, second = '', ''
        while l1:
            first += str(l1.val)
            l1 = l1.next
        while l2:
            second += str(l2.val)
            l2 = l2.next
        sum_num = int(first) + int(second)
        dummy = ListNode()
        p = dummy
        for num in str(sum_num):
            p.next = ListNode(int(num))
            p = p.next
        return dummy.next
```
**思路**：第一直觉就是把两个链表转化成整数相加后再转回链表。


## 234. Palindrome Linked List(Easy)

[https://leetcode-cn.com/problems/palindrome-linked-list/](https://leetcode-cn.com/problems/palindrome-linked-list/)

### Description
请判断一个链表是否为回文链表。

### Solution(栈，两次遍历)
```python
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head: return True
        stack = []
        p = head
        while p:
            stack.append(p.val)
            p = p.next
        while head:
            if head.val == stack[-1]:
                head = head.next
                stack.pop()
            else:
                return False

        return True
```

**思路**：利用列表栈的使用性质，第一次遍历将链表中的所有元素入栈，第二次遍历的同时执行出栈操作进行两两比较。第二次遍历的过程可以看成是125、680题中的双指针从头尾进行遍历。

## 725. Split Linked List in Parts(Medium)

[https://leetcode-cn.com/problems/split-linked-list-in-parts/](https://leetcode-cn.com/problems/split-linked-list-in-parts/)

### Description
给定一个头结点为 root 的链表, 编写一个函数以将链表分隔为 k 个连续的部分。
每部分的长度应该尽可能的相等: 任意两部分的长度差距不能超过 1，也就是说可能有些部分为 null。
这k个部分应该按照在链表中出现的顺序进行输出，并且排在前面的部分的长度应该大于或等于后面的长度。
返回一个符合上述规则的链表的列表。
举例： 1->2->3->4, k = 5 // 5 结果 [ [1], [2], [3], [4], null]

### Solution
```python
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        res = []
        head = root
        length = 0
        # 计算链表总长度
        while head:
            head = head.next
            length += 1
        # 计算商数和余数
        quotient = length // k
        remainder = length % k
        i = 0
        p1 = root
        # 开始将分开的parts一个个加入列表
        while k:
            # 如果有余数, 前余数个链表长度=商数+1，否则=商数
            if i < remainder:
                sublength = quotient + 1
            else:
                sublength = quotient
            # 切分当前链表
            if sublength:
                p2 = p1
                while sublength - 1:
                    p1 = p1.next
                    sublength -= 1
                temp = p1.next
                p1.next = None
                p1 = temp
                res.append(p2)
            else:
                res.append(None)
            k -= 1
            i += 1
        return res
```
**思路**：主要核心思路是求出整除的商，和余数。商代表每一份的链表长度，余数代表前几份链表的长度需要加一。

## 328. Odd Even Linked List(Medium)

[https://leetcode-cn.com/problems/odd-even-linked-list/](https://leetcode-cn.com/problems/odd-even-linked-list/)

### Description
给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。
请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。

### Solution(双指针同向遍历)
```python
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next: 
            return head
        odd, even = head, head.next
        firstEven = head.next
        while odd.next and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = firstEven
        return head
```

**思路**：设置两个指针，一个去把奇数位串起来，一个去把偶数位串起来。然后把第一位偶数节点放到最后一位奇数节点后。

## 138.Copy List with Random Pointer(Medium)

[https://leetcode-cn.com/problems/copy-list-with-random-pointer/](https://leetcode-cn.com/problems/copy-list-with-random-pointer/)

### Solution
```python
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return head
        dic = {}
        cur = head
        # 建立老链表和新链表的节点 map
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next
        p = head
        # 复制索引
        while p:
            dic[p].next = dic.get(p.next)
            dic[p].random = dic.get(p.random)
            p = p.next
        return dic[head]
```
思路： 利用字典复制链表节点。


## 2. 两数相加(Medium)

[https://leetcode-cn.com/problems/add-two-numbers/](https://leetcode-cn.com/problems/add-two-numbers/)

### Description
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。


### Solution
```python
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(l1.val + l2.val)
        cur = head
        while l1.next or l2.next:
            l1 = l1.next if l1.next else ListNode()
            l2 = l2.next if l2.next else ListNode()
            cur.next = ListNode(l1.val + l2.val + cur.val // 10)
            cur.val = cur.val % 10
            cur = cur.next
        if cur.val >= 10:
            cur.next = ListNode(cur.val // 10)
            cur.val = cur.val % 10
        return head
```
思路：  
1. 先将l1和l2头节点的值加起来赋值给新链表的头节点
2. 遍历两个链表，只要有一个链表还没有遍历到末尾，就继续遍历
3. 每次遍历生成一个当前节点cur的下一个节点，其值为两链表对应节点的和再加上当前节点cur产生的进位  
4. 更新进位后的当前节点cur的值
5. 循环结束后，因为首位可能产生进位，因此如果cur.val是两位数的话，新增一个节点
6. 返回头节点
































