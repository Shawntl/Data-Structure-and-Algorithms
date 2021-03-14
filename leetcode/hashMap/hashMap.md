|   layout  |   title | date | author  | tag |
|  ----  | ----  | ---- | ---- | ---- |
|  post | LinkedList |  2021-03-13 | Shawn_Song  | leetcode
-------

# Hash表


## Content
* 299. bulls and cows

## 299. bulls and cows(Easy)

[https://leetcode-cn.com/problems/bulls-and-cows/](https://leetcode-cn.com/problems/bulls-and-cows/)


### Solution(Brute force)
```python
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # 1. 将secret存入字典，键为字符，值为1
        # 2. 遍历第一遍字符，计算bull数
        # 3. 遍历第二遍字符，计算cow数
        secret_dict = {x:secret.count(x) for x in secret}
        n = len(secret)
        bull, cow = 0, 0
        for i in range(n):
            if guess[i] == secret[i]:
                bull += 1
                secret_dict[guess[i]] -= 1
                
        for j in range(n):
            if guess[j] not in secret_dict.keys():
                continue
            
            if guess[j] != secret[j] and secret_dict[guess[j]] > 0:
                secret_dict[guess[j]] -= 1
                cow += 1
    
        return str(bull)+'A'+str(cow)+'B'
```

**思路**：暴力法，两次遍历。利用字典先将频数存起来。












