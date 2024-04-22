# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def getNode(node, depth):
            if node == None:
                return
            if depth == len(res):
                res.append(node.val)
            getNode(node.right, depth + 1)
            getNode(node.left, depth + 1)
        getNode(root, 0)
        return res


    def _rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque()
        if root != None:
            q.appendleft(root)

        while len(q) != 0:
            sz = len(q)
            curr_value = 0
            for i in range(sz):
                curr_node = q.pop()
                if curr_node.left:
                    q.appendleft(curr_node.left)
                if curr_node.right:
                    q.appendleft(curr_node.right)
                if i == sz - 1:
                    res.append(curr_node.val)
        
        return res