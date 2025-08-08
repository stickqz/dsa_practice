from typing import (
    List,
)

class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequence_reconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        nodes = reduce(set.union, seqs, set())

        # check if all nodes are present in the seqs
        if nodes != set(org):
            return False
        
        n = len(org)
        adj = defaultdict(list)
        indeg = [0]*(n+1)

        # Graph construcion
        for s in seqs:
            for u, v in zip(s, s[1:]):
                adj[u].append(v)
                indeg[v] += 1

        # Start BFS with nodes having indegree 0    
        q = [n for n in org if indeg[n] == 0]
        order = []

        while q:
            # if anytime there is more than 1 ele in q => res won't be unique
            if len(q) !=1:
                return False

            n = q.pop()

            for nh in adj[n]:
                indeg[nh]-=1

                if indeg[nh] ==0:
                    q.append(nh)
        
        return len(order) == n


## TOPOLOGICAL SORT
# TC - O(V + E)
# SC - O(V + E)