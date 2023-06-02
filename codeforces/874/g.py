def remove_branch(tree, node1, node2):
    tree[node1].remove(node2)
    tree[node2].remove(node1)

    if len(tree[node1]) == 0:
        del tree[node1]

    if len(tree[node2]) == 0:
        del tree[node2]


def task(n, e):
    if n % 3 != 0:
        print(-1)
        return

    unvisited = set()

    for i in range(n):
        unvisited.add(i + 1)

    tree = {}
    edges = {}

    for i in range(n - 1):
        u, v = e[i]

        if not u in tree:
            tree[u] = set()

        if not v in tree:
            tree[v] = set()

        tree[u].add(v)
        tree[v].add(u)

        if not u in edges:
            edges[u] = {}

        if not v in edges:
            edges[v] = {}

        edges[u][v] = i + 1
        edges[v][u] = i + 1

    ans = 0
    cuts = []

    while len(tree) > 0:

        leafs = set()
        for u in tree:
            if len(tree[u]) == 1:
                leafs.add(u)

        parents = {}
        for leaf in leafs:
            parent = list(tree[leaf])[0]

            if not parent in parents:
                parents[parent] = []

            parents[parent].append(leaf)

        for parent in parents:
            if not parent in tree:
                print(-1)
                return

            leafs_count = len(parents[parent])

            if leafs_count > 2:
                print(-1)
                return

            elif leafs_count == 2:

                for leaf in parents[parent]:
                    remove_branch(tree, parent, leaf)
                    unvisited.remove(leaf)
                unvisited.remove(parent)

                if parent in tree:
                    for cut in list(tree[parent]):
                        cuts.append([parent, cut])
                        remove_branch(tree, parent, cut)
                        ans += 1

            elif leafs_count == 1:
                if len(tree[parent]) < 2:
                    print(-1)
                    return

                elif len(tree[parent]) == 2:
                    leaf = parents[parent][0]
                    remove_branch(tree, parent, leaf)

                    parent_parent = list(tree[parent])[0]
                    remove_branch(tree, parent, parent_parent)

                    unvisited.remove(parent)
                    unvisited.remove(leaf)
                    unvisited.remove(parent_parent)

                    if parent_parent in tree:
                        for cut in list(tree[parent_parent]):
                            ans += 1
                            cuts.append([parent_parent, cut])
                            remove_branch(tree, parent_parent, cut)

    if len(unvisited) > 0:
        print(-1)
        return

    print(ans)

    ans_edges = []
    for u, v in cuts:
        ans_edges.append(str(edges[u][v]))

    print(" ".join(ans_edges))


t = int(input())
for i in range(0, t):
    n = int(input())
    e = []
    for j in range(n - 1):
        u, v = map(int, input().split())
        e.append([u, v])

task(n, e)
