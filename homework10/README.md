# 프로그래머스 문제풀이

## 가사 찾기

---

### 소스 코드

```python
def solution(words, queries):
    class Node:
        def __init__(self, value=None):
            self.value = value
            self.child = dict()
            self.len_dict = dict()

    class Trie:
        def __init__(self):
            self.root = Node()

        def add(self, value:str):
            node = self.root
            for c in value:
                # add dictionary for wildcard
                if len(value) not in node.len_dict:
                    node.len_dict[len(value)] = 0
                node.len_dict[len(value)] += 1
                if c not in node.child: # There is no child
                    new_node = Node(c)
                    node.child[c] = new_node
                    node = new_node
                else:
                    node = node.child[c]
            node.child['*'] = None

        def search(self, queri):
            node = self.root
            for c in queri:
                if c == '?':
                    return node.len_dict[len(queri)] if len(queri) in node.len_dict else 0
                if c in node.child:
                    node = node.child[c]
                else:
                    return 0

            return 0

        # def print(self):
        #     node = self.root
        #     queue = []
        #     queue.append(node)
        #     while queue:
        #         root = queue[0]
        #         del queue[0]

        #         if root.value is not None:
        #             print(root.value, end = " ")

        #         if  '*' in root.child:
        #             print('*')
        #             continue

        #         for node in root.child.values():
        #             queue.append(node)
    
    reversed_words = [word[::-1] for word in words]

    trie = Trie()
    for word in words:
        trie.add(word)

    reversed_trie = Trie()
    for word in reversed_words:
        reversed_trie.add(word)

    answer = []

    for queri in queries:
        if queri[0] == '?':
            answer.append(reversed_trie.search(queri[::-1]))
        else:
            answer.append(trie.search(queri))
    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(words, queries)) # [3, 2, 4, 1, 0]
```

### Output
```
[3, 2, 4, 1, 0]
```