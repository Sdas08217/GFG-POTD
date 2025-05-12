import heapq

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        # Sort meetings by start time
        meetings.sort(key=lambda x: x[0])
        
        # min-heap of available rooms (by room number)
        free = list(range(n))
        heapq.heapify(free)
        
        # min-heap of busy rooms: (free_time, room_number)
        busy: list[tuple[int,int]] = []
        
        # count how many meetings each room hosts
        count = [0]*n
        
        for start, end in meetings:
            # free up any rooms that have become available by 'start'
            while busy and busy[0][0] <= start:
                free_time, room = heapq.heappop(busy)
                heapq.heappush(free, room)
            
            if free:
                # assign to the smallest-numbered free room
                room = heapq.heappop(free)
                actual_start = start
                actual_end = end
            else:
                # no free rooms: wait for the next one to free
                free_time, room = heapq.heappop(busy)
                delay = end - start
                actual_start = free_time
                actual_end = free_time + delay
            
            # mark room as busy until actual_end
            heapq.heappush(busy, (actual_end, room))
            count[room] += 1
        
        # return the room with the highest count (break ties by smaller room number)
        return min(
            range(n),
            key=lambda i: (-count[i], i)
        )
