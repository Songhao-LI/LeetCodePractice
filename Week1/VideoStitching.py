class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        start, end, res = -1, 0, 0
        for clip in sorted(clips):
            if end >= time or clip[0] > end:
                break
            if clip[1] <= end:
                continue

            if clip[0] <= start:
                end = clip[1]
            else:
                res += 1
                start, end = end, clip[1]

        return res if end >= time else -1
