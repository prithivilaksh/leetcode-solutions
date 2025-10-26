# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Codec:

#     def serialize(self, root):
#         """Encodes a tree to a single string.
        
#         :type root: TreeNode
#         :rtype: str
#         """

#         data=[]
#         def preorder(root):
#             if not root: data.append("#")
#             else:
#                 data.append(str(root.val))
#                 preorder(root.left)
#                 preorder(root.right)

#         preorder(root)
#         return ' '.join(data)
        

#     def deserialize(self, data):
#         """Decodes your encoded data to tree.
        
#         :type data: str
#         :rtype: TreeNode
#         """

#         data=data.split(' ')
#         pos=-1

#         def preorder():
#             nonlocal pos
#             pos+=1
#             if data[pos]=="#": return None
#             root=TreeNode(int(data[pos]))
#             root.left=preorder()
#             root.right=preorder()
#             return root

#         return preorder()

        

# # Your Codec object will be instantiated and called as such:
# # ser = Codec()
# # deser = Codec()
# # ans = deser.deserialize(ser.serialize(root))



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        def preorder(root):
            if not root: return "#,"
            data=str(root.val)+","
            data+=preorder(root.left)
            data+=preorder(root.right)
            return data

        return preorder(root)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        it=iter(data.split(','))

        def preorder():
            val=next(it)
            if val=="#": return None
            root=TreeNode(int(val))
            root.left=preorder()
            root.right=preorder()
            return root

        return preorder()

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))









# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def preorder(root):
            if not root: return "#,"
            data=f"{root.val},"
            data+=preorder(root.left)
            data+=preorder(root.right)
            return data
        return preorder(root)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        it=iter(data.split(","))
        def preorder():
            val=next(it)
            if val=="#": return None
            node=TreeNode(int(val))
            node.left=preorder()
            node.right=preorder()
            return node
        return preorder()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))



