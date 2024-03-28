class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        graph = defaultdict(set)
        for i in range(len(routes)):
            for stop in routes[i]:
                graph[stop].add(i)

        visited_stops = set()
        visited_stops.add(source)
        visited_buses = set()
        q = deque()
        q.appendleft((source, 0))

        # do bfs to stops(think about how to optimize the space complexity)
        while q:
            sz = len(q)
            for _ in range(sz):
                cur_stop, step = q.pop()
                if cur_stop == target:
                    return step
                for bus in graph[cur_stop]:
                    if bus not in visited_buses:
                        visited_buses.add(bus)
                        for stop in routes[bus]:
                            if stop not in visited_stops:
                                visited_stops.add(stop)
                                q.appendleft((stop, step + 1))
        return -1