from typing import Iterable, List, Tuple


def is_line_allowed(value: int, intervals: Iterable[Tuple[int, int]]) -> bool:
    """Return True if a fold line at the given coordinate avoids all rectangles."""
    for left, right in intervals:
        if left < value < right:
            return False
    return True


def is_segment_clear(left: int, right: int, intervals: Iterable[Tuple[int, int]]) -> bool:
    """Return True if every point strictly between left and right is clear of rectangles."""
    mid = (left + right) / 2.0
    for l, r in intervals:
        if l < mid < r:
            return False
    return True


def minimal_gap(bounds: Tuple[int, int], intervals: List[Tuple[int, int]], edge_points: Iterable[int]) -> int:
    low, high = bounds
    positions = sorted(set(p for p in edge_points if low <= p <= high))

    allowed_points = set()
    for pos in positions:
        if is_line_allowed(pos, intervals):
            allowed_points.add(pos)

    # Inspect gaps between consecutive critical positions
    for i in range(len(positions) - 1):
        left = positions[i]
        right = positions[i + 1]
        gap = right - left
        if gap <= 0:
            continue
        if is_segment_clear(left, right, intervals):
            if gap >= 3:
                return 1
            if gap == 2:
                middle = left + 1
                allowed_points.add(middle)

    sorted_allowed = sorted(allowed_points)

    min_gap = float('inf')
    for i in range(len(sorted_allowed) - 1):
        min_gap = min(min_gap, sorted_allowed[i + 1] - sorted_allowed[i])

    return int(min_gap)


def main() -> None:
    N = int(input())
    rects = [tuple(map(int, input().split())) for _ in range(N)]
    px1, py1, px2, py2 = map(int, input().split())

    x_intervals = [(x1, x2) for x1, _, x2, _ in rects]
    y_intervals = [(y1, y2) for _, y1, _, y2 in rects]

    x_points = [px1, px2]
    y_points = [py1, py2]

    for x1, y1, x2, y2 in rects:
        x_points.extend([x1, x2])
        y_points.extend([y1, y2])

    min_width = minimal_gap((px1, px2), x_intervals, x_points)
    min_height = minimal_gap((py1, py2), y_intervals, y_points)

    print(min_width * min_height)


if __name__ == "__main__":
    main()
