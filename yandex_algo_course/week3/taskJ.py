def expand_positions(positions):
    new_positions = set()
    for pos in positions:
        new_pos1 = (pos[0] + 1, pos[1])
        new_pos2 = (pos[0] - 1, pos[1])
        new_pos3 = (pos[0], pos[1] + 1)
        new_pos4 = (pos[0], pos[1] - 1)
        # new_positions.add(pos)
        new_positions.add(new_pos1)
        new_positions.add(new_pos2)
        new_positions.add(new_pos3)
        new_positions.add(new_pos4)
    return new_positions | positions


def add_postions_t_time(positions, t):
    for _ in range(t):
        positions = expand_positions(positions)
    return positions


def navigator_check(coords_nav, postitions, navigator_dist):
    new_positios = set()
    for _ in range(navigator_dist):
        
    for pos in postitions:
        x_d = abs(pos[0] - coords_nav[0])
        if x_d >= navigator_dist:
            pass
        y_d = abs(pos[1] - coords_nav[1])
        if y_d >= navigator_dist:
            pass
        manh_dist = x_d + y_d
        if manh_dist <= navigator_dist:
            new_positios.add(pos)
    return new_positios


t, d, N = map(int, input().split())

possible_positions = set()
possible_positions.add((0, 0))
n = 0
while n != N:
    possible_positions = add_postions_t_time(possible_positions, t)
    coords_nav = tuple(map(int, input().split()))
    possible_positions = navigator_check(coords_nav, possible_positions, d)
    n += 1

print(len(possible_positions))
for p in possible_positions:
    print(p[0], p[1])
