class Solution(object):
    def maxPoints(self, points):
        if len(points) <= 2:
            return len(points)
        
        max_points = 0
        
        for i in range(len(points)):
            slope_map = defaultdict(int)
            overlap = 0
            curr_max = 0
            
            for j in range(i + 1, len(points)):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                
                if dx == 0 and dy == 0:
                    overlap += 1
                    continue
                
                gcd_val = self.gcd(dx, dy)
                slope = (dx // gcd_val, dy // gcd_val)
                slope_map[slope] += 1
                curr_max = max(curr_max, slope_map[slope])
            
            max_points = max(max_points, curr_max + overlap + 1)
        
        return max_points
    
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a