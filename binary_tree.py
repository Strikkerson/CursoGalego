from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root == None:
            self.root = TreeNode(val)
        else:
            self.insert_recursive(self.root, val)

    def insert_recursive(self, node, val):
        if val > node.val:
            if node.right:
                self.insert_recursive(node.right, val)
            else:
                node.right = TreeNode(val)
        else:
            if node.left:
                self.insert_recursive(node.left, val)
            else:
                node.left = TreeNode(val)
    
    def search(self, val):
        return self._search_recursive(self.root, val)

    def _search_recursive(self, node, val):
        if not node:
            return False
        
        if val == node.val:
            return True
        
        if val > node.val:
            return self._search_recursive(node.right, val)

        return self._search_recursive(node.left, val)
    
    def dfs(self, val):
        return self._dfs_recursive(self.root, val)

    def _dfs_recursive(self, node, val):
        if not node:
            return False
        
        if val == node.val:
            return True

        return self._dfs_recursive(node.left, val) or self._dfs_recursive(node.right, val)
    
    def bfs(self, val):
        if self.root == None:
            return False
        
        queue = deque()
        queue.append(self.root)

        while queue:
            node = queue.popleft()

            if node.val == val:
                return True
        
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)

        return False

        
    
    def preorder_traversal(self):
        result = []
        self._preorder_recursive(self.root, result)

        return result

    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.val)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)

        return result
    
    def _inorder_recursive(self, node, result):
       if node: 
            self._inorder_recursive(node.left, result)
            result.append(node.val)
            self._inorder_recursive(node.right, result)

    def postorder_traversal(self):
        result = []
        self._postorder_recursive(self.root, result)

        return result
    
    def _postorder_recursive(self, node, result):
       if node: 
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.val)



tree = BinaryTree()
values_to_insert = [5, 3, 1, 10, 7, 15]
for val in values_to_insert:
    tree.insert(val)

print(tree.search(5))
print(tree.search(10))
print(tree.search(17))
print(tree.bfs(5))
print(tree.bfs(10))
print(tree.bfs(17))
print(tree.dfs(5))
print(tree.dfs(10))
print(tree.dfs(17))

print("Preorder Traversal:", tree.preorder_traversal())
print("Inorder Traversal:", tree.inorder_traversal())
print("Postorder Traversal:", tree.postorder_traversal())


        

            



        