def conquest_campaign(N, M, L, battalion):
    def build_captured(battalion, i=0, captured=None):
        if captured is None:
            captured = set()
        if i >= 2 * L:
            return captured
        return build_captured(battalion, i + 2, captured | {(battalion[i], battalion[i + 1])})

    captured = build_captured(battalion)

    def neighbors(x, y):
        possible_neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        return list(filter(lambda cell: 1 <= cell[0] <= N and 1 <= cell[1] <= M, possible_neighbors))

    def capture_new_cells(cells, accumulated):
        if not cells:
            return accumulated
        current = cells[0]
        new_neighbors = [neighbor for neighbor in neighbors(*current) if neighbor not in accumulated]
        return capture_new_cells(cells[1:], accumulated | set(new_neighbors))

    def capture_day(captured):
        new_captured = capture_new_cells(list(captured), captured)
        return new_captured

    def days_count(captured, day):
        if len(captured) == N * M:
            return day
        return days_count(capture_day(captured), day + 1)

    return days_count(captured, 1)

N, M, L = 3, 4, 2
battalion = [2, 2, 3, 4]
print(conquest_campaign(N, M, L, battalion)) 