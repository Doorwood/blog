class Node:
    def __init__(self,val=0,left=None,right=None,parent=None):
        self.val=val
        self.left = left
        self.right = right
        self.parent = parent
    def isLeaf(self):
        return not self.left and not self.right
    def hasChildren(self):
        return self.left and self.right
    def hasOneKid(self):
        if self.isLeaf() or self.hasChildren():
            return False

        return True
    def leftChild(self,kid):
        self.left = kid
        if kid:
            kid.parent = self
    def rightChild(self,kid):
        self.right = kid
        if kid:
            kid.parent = self

    def __str__(self):
        return "val:" + str(self.val)
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self,val):
        if not self.root:
            self.root = Node(val)
        else:
            self.root = self.insertHelper(self.root,val)
            self.root.parent = None
    def addAll(self,arr):
        for val in arr:
            self.insert(val)
    def insertHelper(self,node,val):
        if not node:
            return Node(val)

        if val>node.val:
            node.rightChild(self.insertHelper(node.right,val))

        else:
            node.leftChild(self.insertHelper(node.left,val))
        lh = self.height(node.left)
        rh = self.height(node.right)
        if abs(lh-rh)>1:
            if lh>rh:
                return self.rightRotate(node)
            else:
                return self.leftRotate(node)
        return node


        return node

    ## leaf just delete
    ## one child child replace
    ## children,find inorder successor node
    def delete(self,val):
        self.root = self.deleteHelper(self.root,val)


    def deleteHelper(self,node,val):
        if not node:
            return None
        if val>node.val:
            node.rightChild(self.deleteHelper(node.right,val))
        elif val<node.val:
            node.leftChild(self.deleteHelper(node.left,val))
        else:
            if node.isLeaf():
                return None
            elif node.hasOneKid():
                if node.left:
                   return node.left
                else:
                    return node.right
            else:
                successor = self.successorNode(node)
                successor.val,node.val = node.val,successor.val
                node.rightChild(self.deleteHelper(node.right,val))




        lh = self.height(node.left)
        rh = self.height(node.right)
        if abs(lh-rh)>1:
            if lh>rh:
                return self.rightRotate(node)
            else:
                return self.leftRotate(node)
        return node
    def leftRotate(self,node):
        newParent = node.right
        node.parent = newParent
        node.right = newParent.left
        if node.right:
            node.right.parent = node
        newParent.left = node
        return newParent
    def rightRotate(self,node):
        newParent = node.left
        node.parent = newParent
        node.left = newParent.right
        if node.left:
            node.left.parent = node
        newParent.right = node
        return newParent
    def printTree(self):
        def traverse(node, level=0, label=''):

            if not node:
                return
            print('   ' * level, label, node.val)
            traverse(node.left, level + 1, 'L:')
            traverse(node.right, level + 1, 'R:')

        traverse(self.root)

    def height(self,node):
        if not node:
            return 0
        return max(self.height(node.left),self.height(node.right))+1

    def successorNode(self,node):
        if node.hasChildren:
            cur = node.right
            while cur.left:
                cur = cur.left
            return cur
        return None
if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.addAll([1,2,3,4])
    tree.delete(1)
    tree.delete(3)
    tree.delete(4)
    tree.printTree()