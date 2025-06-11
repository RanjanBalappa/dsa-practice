class Solution:
    def get_y_range(self, active_intervals):
        y_last = -1
        active_intervals.sort()
        cur_area = 0
        for y_start, y_end in active_intervals:
            area = max(0, y_end - max(y_start, y_last))
            cur_area += area
            y_last = max(y_end, y_last)
        return cur_area

    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        events = []
        START = 0
        END = 1
        for x1, y1, x2, y2 in rectangles:
            events.append((x1, y1, y2, START))
            events.append((x2, y1, y2, END))
        events.sort()
        x_last = events[0][0]
        cumu_interval = []
        total_area = 0
        for event in events:
            y_range = self.get_y_range(cumu_interval)
            total_area += y_range * (event[0] - x_last)
            if event[3] == START:
                cumu_interval.append((event[1], event[2]))
            else:
                cumu_interval.remove((event[1], event[2]))
            
            x_last = event[0]
        
        return total_area % (10**9 + 7)


        