import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        indexed_tasks = []
        for i, (enqueue_time, process_time) in enumerate(tasks):
            indexed_tasks.append((enqueue_time, process_time, i))
            
     
        indexed_tasks.sort()
        
        result = []
        min_heap = []
        curr_time = 0
        i = 0
        n = len(tasks)
        
        while i < n or min_heap:
           
            if not min_heap and curr_time < indexed_tasks[i][0]:
                curr_time = indexed_tasks[i][0]
                
            
            while i < n and indexed_tasks[i][0] <= curr_time:
                enqueue_time, process_time, index = indexed_tasks[i]
                
                heapq.heappush(min_heap, (process_time, index))
                i += 1
                
           
            process_time, index = heapq.heappop(min_heap)
            curr_time += process_time
            result.append(index)
            
        return result