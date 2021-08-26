class Solution:
    def numTrees(self, n: int) -> int:

        #base case 
        # n = 0, 0 node we have 1 tree
        # n = 1, 1 node we have 1 tree

        # we make (n+1) instead of (n) is because the numTree[0] represent the base case 0 node
        numTree = [1] * (n+1)

        #we start from 2 is because n =0, 1 are all base cases
        for node in range(2, n+1):
            totalNumTree = 0

            # we would calculate the number of the different Trees where the root is from 1 to node
            # ex: numTree[4] = (numTree[ 0 ] * numTree[ 3 ]) + (numTree[ 1 ] * numTree[ 2 ]) + (numTree[ 2 ] * numTree[ 1 ]) + (numTree[ 3 ] * numTree[ 0 ] )
            for eachRoot in range(1, node+1):
                left = eachRoot - 1
                right = node - eachRoot
                totalNumTree += numTree[left] * numTree[right]
            
            numTree[node] = totalNumTree
        
        return numTree[-1]
