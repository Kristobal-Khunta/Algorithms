#
##


def cnt_pairs_with_r(sorted_dist, r):
    count = 0
    if len(sorted_dist) == 1:
        return 0
    r_idx = 1
    for l_idx in range(len(sorted_dist)):
        while r_idx < len(sorted_dist) and sorted_dist[r_idx] - sorted_dist[l_idx] <= r:
            r_idx += 1

        # print("left", l_idx, len(sorted_dist) - r_idx)
        count += len(sorted_dist) - r_idx
    return count


def main():
    n, r = map(int, input().split())
    dist_start = list(map(int, input().split()))
    count = cnt_pairs_with_r(dist_start, r)
    # Если бы нас спрашивали про парней,то  каждая пара должна учитываться дважды count = single_count * 2
    # но нас спрашивают, сколькими способами можно бвырать 2 памятика.

    print(count)


if __name__ == "__main__":
    main()
