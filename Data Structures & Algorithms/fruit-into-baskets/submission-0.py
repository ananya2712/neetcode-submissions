class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        hashmap = defaultdict(int)
        left = 0
        res = 0
        total = 0

        for r in range(len(fruits)):
            hashmap[fruits[r]] +=1
            total +=1

            while len(hashmap) > 2:
                f = fruits[left]
                hashmap[f] -=1
                total -=1
                left +=1
                if not hashmap[f]:
                    hashmap.pop(f)
            res = max(res,total)

        return res