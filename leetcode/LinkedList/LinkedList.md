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
* 206 Reverse Linked List
* 21 Merge Two Sorted Lists
* 83 Remove Duplicates from Sorted List(Recap 26、80)
* 19 Remove Nth Node From End of List
* 24 Swap Nodes in Pairs
* 445 Add Two  Numbers II
* 234 Palindrome Linked List(Recap 125、680 in 对撞双指针)
* 725 Split Linked List in Parts
* 328 Odd Even Linked List

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
        return head.nex
```

**思路**：创建一个新的头指针，然后遍历两个链表，依次把小的元素所在的链表接入创建的指针。边界情况一个是其中一个链表为空，另一个情况是两个链表长度不一，一个链表会优先遍历完，直接把另一个链表接到最后即可。


## 83. Remove Duplicates from Sorted List(Easy)

[https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/)

### Description
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

### Solution(快慢指针)
```python
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return
        slower, faster = head, head.next
        while faster:
            while faster and  slower.val == faster.val:
                faster = faster.next
            slower.next = faster
            if not faster: break

            slower = slower.next
            faster = faster.next
        return head
```

**思路**：和第26题唯一不一样的地方就是数据结构从列表换成了链表，但是解题思路是一样的，设计一个快指针和慢指针。快指针遇到和慢指针指向元素值一样则跳过，大于慢指针则更新慢指针，快指针继续向前搜索。


## 19. Remove Nth Node From End of List(Medium)

[https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/)

### Description
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点.

### Solution(hash table)
```python
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head: return
        pointer_dict = {}
        idx = 1
        cur = head
        while cur:
            pointer_dict[idx] = cur
            cur = cur.next
            idx += 1
        pointer_dict[idx] = cur
        length = idx
        # 删除头节点的情况
        if length == n+1:
            return head.next
        pointer_dict[length-n-1].next = pointer_dict[length-n+1]
        return head
```

**思路**：题目中要求遍历一遍来求解，我自然而然就想到利用空间换时间，利用字典把遍历过程中每个节点的下标储存起来，遍历过后用O(1)的时间找到需要删除的元素。

### Solution Two(双指针 划窗)
```python
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head: return
        # 利用dummy处理删除头节点的情况
        dummy = ListNode()
        dummy.next = head
        p1, p2 = dummy, dummy
        # p1、p2中间相间隔n-1个节点
        for i in range(n):
            p2 = p2.next
        # 当p2达到链表最后一个节点时，p1到达待删除节点的前一个节点
        while p2.next:
            p1 = p1.next
            p2 = p2.next
        p1.next = p1.next.next
        return dummy.next
```

**思路**：这种思路非常巧妙，利用两个指针构建一个n size的划窗，划窗尾部到底时，首部也就找到了倒数第n个元素。这里由于是两个指针一前一后遍历所以时间复杂度要略高于第一种方法，但是节省了空间。


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































