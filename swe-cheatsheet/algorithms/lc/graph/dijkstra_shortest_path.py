from collections import defaultdict, namedtuple, deque
from typing import Dict, List, Tuple

"""
Using a priority queue
A min-priority queue is an abstract data type that provides 3 basic operations : 
add_with_priority(), decrease_priority() and extract_min(). As mentioned earlier, 
using such a data structure can lead to faster computing times than using a basic queue.
 Notably, Fibonacci heap (Fredman & Tarjan 1984) or Brodal queue offer optimal 
 implementations for those 3 operations.  
"""



Edge = namedtuple('Edge', ['sink', 'weight'])


def shortest_path(vertices, adj: Dict[int, List[Edge]], start: int) -> (dict, dict):
    q = list(vertices)
    prev = {v: None for v in vertices}
    dist = {v: float('inf') for v in vertices}
    dist[start] = 0
    while q:
        source = _extract_min(q, dist)
        for sink, weight in adj[source]:
            if dist[source] + weight < dist[sink]:
                dist[sink] = dist[source] + weight
                prev[sink] = source

    return dist, prev

def _extract_min(q: list, dist: dict):
    min_val = float('inf')
    min_vertex = None
    min_ind = None
    for i, v in enumerate(q):
        if dist[v] < min_val:
            min_val = dist[v]
            min_vertex = v
            min_ind = i

    q.pop(min_ind)
    return min_vertex


def _get_adjacency(edges: List[Tuple[int, int, int]]) -> Dict[int, List[Edge]]:
    g = defaultdict(list)
    for u, v, w in edges:
        g[u].append(Edge(sink=v, weight=w))
    return g


class PQueue:
    @classmethod
    def add(cls, queue, val, priority):
        pass
    @classmethod
    def extract_min(cls, queue):
        return queue[0]
    @classmethod
    def decrease_key(cls, queue, k, new_val):
        pass


def dijkstra(graph, source):
    """Sketch of priority queue solution"""
    q = []
    dist = {source: 0}
    prev = dict()
    for v in graph:
        if v != source:
            dist[v] = float('inf')
        prev[v] = None
        PQueue.add(q, v, dist[v])

    while q:
        source = PQueue.extract_min(q)
        for sink, weight in graph[source]:
            alt = dist[source] + weight
            if alt < dist[sink]:
                dist[sink] = alt
                prev[sink] = source
                PQueue.decrease_key(q, sink, alt)

    return dist, prev

def t():
    adj = _get_adjacency([
        (1, 2, 5),
        (1, 4, 1),
        (1, 3, 10),
        (2, 3, 2),
        (4, 3, 3),
        (3, 5, 10),
    ])
    dist, prev = shortest_path([1, 2, 3, 4, 5], adj, start=1)
    print(dist)
    print(prev)

    goal = 5
    print(f'dist to {goal} is {dist[goal]}')
    cur = goal
    path = deque([])
    while cur is not None:
        path.appendleft(cur)
        cur = prev[cur]
    print(f'path to {goal} is {path}')


t()


def dijkstra_shortest_path(vertices, adj: Dict[int, set], start: int) -> (dict, dict):
    dist = {v: float('inf') for v in vertices}
    dist[start] = 0
    prev = {v: None for v in vertices}
    q = [v for v in vertices]
    while q:
        source = PQueue.extract_min(q)
        for sink, weight in adj[source]:
            cost = dist[source] + weight
            if cost < dist[sink]:
                dist[sink] = cost
                prev[sink] = source
                PQueue.decrease_key(q, sink, cost)

    return dist, prev
