class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:

        # sort clips by start time
        clips.sort(key=lambda x : x[0])

        # if we don't have a clip starting at time 0, the problem is impossible
        if clips[0][0] != 0:
            return -1

        # memoization
        cache = {} # clip index : min number of steps it takes to get to the end

        # dfs portion
        def dfs(clip_index):

            # avoid repeated work
            if clip_index in cache:
                return cache[clip_index]
            
            # base case, we found a clip that reaches the end
            if clips[clip_index][1] >= time:
                cache[clip_index] = 1
                return 1
            
            # dfs future clips
            res = float('inf')
            for i in range(clip_index + 1, len(clips)):

                curr_clip = clips[clip_index]
                next_clip = clips[i]

                # ensure that we are actually going forward and that the end of the current clip and the start of the next clip are connected
                if next_clip[0] > curr_clip[0] and next_clip[0] <= curr_clip[1] and next_clip[1] > curr_clip[1]:
                    res = min(res, 1 + dfs(i))

            cache[clip_index] = res
            return res
        
        # find the best clip to start with -> [0, greatest end time]
        start_index = 0
        for i in range(1, len(clips)):
            if clips[i][0] != 0:
                break
            if clips[i][1] > clips[start_index][1]:
                start_index = i
        
        # call dfs
        res = dfs(start_index)
        if res == float('inf'):
            return -1
        return res