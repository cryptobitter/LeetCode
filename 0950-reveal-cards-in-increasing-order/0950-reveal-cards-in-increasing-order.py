from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        deck.sort()

        index_queue = deque(range(n))  
        result = [0] * n

        for value in deck:              
            reveal_pos = index_queue.popleft()   
            result[reveal_pos] = value           

            if index_queue:
                index_queue.append(index_queue.popleft())  

        return result