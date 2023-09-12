"""
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
Serialize and Deserialize Binary Tree
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val


class Codec:
    def serialize(self, root):
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()

# class Codec:
#
#     # Serialization
#     def serialize(self, root):
#         """ Encodes a tree to a single string.
#         :type root: TreeNode
#         :rtype: str
#         """
#
#         def rserialize(root, string):
#             """ a recursive helper function for the serialize() function."""
#             # check base case
#             if root is None:
#                 string += 'None,'
#             else:
#                 string += str(root.val) + ','
#                 string = rserialize(root.left, string)
#                 string = rserialize(root.right, string)
#             return string
#
#         return rserialize(root, '')
#
#     # Deserialization
#     def deserialize(self, data):
#         """Decodes your encoded data to tree.
#         :type data: str
#         :rtype: TreeNode
#         """
#
#         def rdeserialize(l):
#             """ a recursive helper function for deserialization."""
#             if l[0] == 'None':
#                 l.pop(0)
#                 return None
#
#             root = TreeNode(l[0])
#             l.pop(0)
#             root.left = rdeserialize(l)
#             root.right = rdeserialize(l)
#             return root
#
#         data_list = data.split(',')
#         root = rdeserialize(data_list)
#         return root
