
from ..solution import Solution
from ..mat import as_matrix, each_index, each_nearest_neighbour
import heapq
from numpy import zeros
from numpy.typing import NDArray
from math import inf


def extend_risk_map(risk_map: NDArray) -> NDArray:
    xs, ys = risk_map.shape
    xl, yl = xs*5, ys*5
    ext_risk_map = zeros((xl, yl), dtype=int)

    # copy in small cave
    for I in each_index(risk_map):
        ext_risk_map[I] = risk_map[I]

    # copy right
    for x in range(xs):
        for y in range(ys, yl):
            ext_risk_map[x, y] = (ext_risk_map[x, y-ys] % 9) + 1

    # copy down
    for x in range(xs, xl):
        for y in range(yl):
            ext_risk_map[x, y] = (ext_risk_map[x-xs, y] % 9) + 1

    return ext_risk_map


def dijkstra(risk_map: NDArray) -> int:
    init, target = (0, 0), (risk_map.shape[0]-1, risk_map.shape[1]-1)
    pq = [(0, init)]
    dist = {I:inf for I in each_index(risk_map)}
    dist[init] = 0
    min_path = inf

    while len(pq) >= 1:
        _, u = heapq.heappop(pq)
        V = [v for v in each_nearest_neighbour(risk_map, u)]
        for v in V:
            alt = dist[u] + risk_map[v]
            if v == target and alt < min_path:
                return alt
            elif alt < dist[v]:
                heapq.heappush(pq, (alt, v))
                dist[v] = alt


def solve(input: list[str]) -> Solution:
    risk_map = as_matrix(input)
    ext_risk_map = extend_risk_map(risk_map)
    return Solution(dijkstra(risk_map), dijkstra(ext_risk_map))
