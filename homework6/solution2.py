import collections

def solution(priorities, location):
    rank = {}

    q = collections.deque()

    for i, priority in enumerate(priorities):
        rank[i] = priority
        q.append(i)

    canPrint = True
    order = 1

    while q:
        canPrint = True

        paper = q.popleft()

        for copy in q:
            if rank[copy] > rank[paper]:
                q.append(paper)
                canPrint = False
                break
        
        if canPrint:
            if paper == location:
                return order
            order += 1


        