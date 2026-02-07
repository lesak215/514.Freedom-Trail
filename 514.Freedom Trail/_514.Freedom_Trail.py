from collections import defaultdict

class Solution:
    def findRotateSteps(self, ring, key):
        n = len(ring)
        m = len(key)
        
        pos_map = defaultdict(list)
        for i, ch in enumerate(ring):
            pos_map[ch].append(i)
        
        dp = [[float('inf')] * n for _ in range(m)]
        
        for p in pos_map[key[0]]:
            dp[0][p] = min(p, n - p) + 1
        
        for i in range(1, m):
            for cur_pos in pos_map[key[i]]:
                for prev_pos in pos_map[key[i - 1]]:
                    diff = abs(prev_pos - cur_pos)
                    dist = min(diff, n - diff)
                    dp[i][cur_pos] = min(dp[i][cur_pos], dp[i - 1][prev_pos] + dist + 1)
        
        return min(dp[-1][p] for p in pos_map[key[-1]])