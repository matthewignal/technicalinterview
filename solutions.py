def question1(s, t):
    # Accounting for edge cases
    if len(s) < len(t):
        return False
    if len(t) == 0:
        return False

    # Create a dictionary of letter occurrences
    def make_letter_dict(string):
        letter_dict = {}
        for letter in string:
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
        return letter_dict

    # Make dictionary for both strings using lowercase letters
    t_dict = make_letter_dict(t.lower())
    s = s.lower()
    # For each slice in s of length t, see if there are the same number of
    # each letter
    for i in range(len(s) - len(t) + 1):
        substring_s = s[i: i + len(t)]
        s_dict = {}
        for letter in substring_s:
            if letter in t_dict.keys():
                if letter not in s_dict.keys():
                    s_dict[letter] = 1
                else:
                    s_dict[letter] += 1
            else:
                break
        if s_dict == t_dict:
            return True
    return False

def question2(string):
    def find_substrings(string):
        substring_list = []
        # for each letter, find all substrings beginning with that letter
        for i in range(len(string)):
            for j in range(i, len(string)):
                substring_list.append(string[i:j+1])
        # sort by longest
        substring_list.sort(key=len, reverse=True)
        return substring_list

    substrings = find_substrings(string)

    def pal(substrings):
        for i in substrings:
            # determine if palindrome, since we've sorted by longest
            if i == i[::-1]:
                if len(i) == 1:
                    return "No palindromes found!"
                else:
                    return i
    return pal(substrings)


def question3(G):
    parent = dict()
    rank = dict()

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(node1, node2):
        root1 = find(node1)
        root2 = find(node2)
        if root1 == root2:
            print "Invalid Input"
        # determine parent based on BST node
        elif root1 > root2:
            parent[root2] = root1
        elif root1 < root2:
            parent[root1] = root2
        else:
            rank[root1] += 1
            parent[root2] = root1

    def kruskal(G):
        nodes = G.keys()
        for node in nodes:
            parent[node] = node
            rank[node] = 0
        # Convert from adjacency list to (x, y, z)
        graph = []
        for key, value in G.items():
            for val in value:
                graph.append(tuple(key) + val)
        # Sort by weight
        if len(graph) < 1:
            return "Invalid Input"
        edges = sorted(graph, key=lambda x: x[2])

        mst = []
        # find tree parents and determine order
        for edge in edges:
            node1, node2, weight = edge
            if find(node1) != find(node2):
                union(node1, node2)
                mst.append(edge)
        # convert back to adjacency list
        from collections import defaultdict
        adjacency_list = defaultdict(list)
        for k, v1, v2 in mst:
            adjacency_list[k].append((v1, v2))
        return dict(adjacency_list)
    return kruskal(G)


def question4(T, r, n1, n2):
    # Account for some edge cases
    if n1 == n2 or n1 is None or n2 is None or r is None:
        return "Invalid Input"

    smaller_node = min(n1, n2)
    larger_node = max(n1, n2)

    while r is not None:
        # If r is between smaller and larger nodes, it must be the lca
        if smaller_node <= r <= larger_node:
            return r
        # replace with a new root if otherwise
        elif r > larger_node:
            # new root must be smaller
            possible = T[r][:r]
            r = [index for index, item in enumerate(possible) if item == 1][0]
        elif r < smaller_node:
            # new root must be larger
            possible = T[r][r:]
            r = [index for index, item in enumerate(possible) if item == 1][0]


def question5(ll, m):
    x = ll
    y = ll
    for i in range(m):
        if x is None:
            return None
        x = x.next
    while x is not None:
        x = x.next
        y = y.next
    if y is not None:
        return y.data
    else:
        return "Invalid Input"

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

# linked list

one = Node(7)
two = Node(6)
three = Node(5)
four = Node(3)
five = Node(7)
six = Node(5)
seven = Node(11)
eight = Node(2)
nine = Node(4)
ten = Node(8)

one.next = two
two.next = three
three.next = four
four.next = five
five.next = six
six.next = seven
seven.next = eight
eight.next = nine
nine.next = ten

print "Q1:", question1(s="udacity", t="dau")
# Expected: True
print "Q1:", question1(s=[], t="ad")
# Expected: False
print "Q1:", question1(s="", t="")
# Expected: False

print "Q2:", question2(string="growogtghgtg")
# Expected: gtghgtg
print "Q2:", question2(string="")
# Expected: Invalid Input
print "Q2:", question2(string="for")
# Expected: No palindromes found!

print "Q3:", question3(G={'A': [('B', 2)], 'B': [('A', 2), ('C', 5)],
                          'C': [('B', 5)]})
# Expected: {'A': [('B', 2)], 'C': [('B', 5)]}
print "Q3:", question3(G={'A': [('B', 0)], 'B': [('A', 0)]})
# Expected: {'A': [('B', 0)]}
print "Q3:", question3(G={})
# Expected: Invalid Input

print "Q4:", question4([[0, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [1, 0, 0, 0, 1],
                        [0, 0, 0, 0, 0]],
                       3,
                       1,
                       4)
# Expected: 3
print "Q4:", question4([[0, 1, 0, 1]],
                       1,
                       1,
                       1)
# Expected: Invalid Input
print "Q4:", question4([[1, 0, 1, 'x']],
                       1,
                       1,
                       1)
# Expected: Invalid Input
print "Q5:", question5(one, 4)
# Expected: 11
print "Q5:", question5(two, 0)
# Expected: Invalid Input
print "Q5:", question5(three, -1)
# Expected: Invalid Input
