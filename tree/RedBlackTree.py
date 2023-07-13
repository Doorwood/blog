RED=1
BLACK=0
class Node:
    def __init__(self,val=None,color=BLACK):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.color = color
    def __str__(self):
        return str(self.val)
    @staticmethod
    def newNode(val):
        node = Node(val,RED)
        node.left = Node()
        node.right = Node()
        node.left.parent = node
        node.right.parent = node
        return node

    def sibling(self):
        if not self.parent:
            return None
        if self.isLeft():
            return self.parent.right
        else:
            return self.parent.left
    def delete(self):
        if self.parent:
            if self.isLeft():
                self.parent.left=Node()
            else:
                self.parent.right=Node()


    def isLeft(self):
        if not self.parent:
            return False
        return self.parent.left==self

    def isLeaf(self):
        return not self.left.val and not self.right.val

    def isBlack(self):
        return self.color==BLACK
    def isRed(self):
        return self.color==RED
    def isNull(self):
        return self.val==None
# #Characteristic:
# # 1.Root is always black
# # 2.Leaves are always black and are all NIL
# # 3.All paths have the same number of black nodes
# # 4.Children of a red node is black.Hence possible parent of red node is black
class RBTree:
    def __init__(self):
        self.root=None
        self.ll=False
        self.lr=False
        self.rr=False
        self.rl=False

    def insert(self,val):
        if not self.root:
            self.root = Node.newNode(val)
            self.root.color = BLACK
        else:
            self.root = self.insertInternal(self.root,val)

        return self
    # Recursively insert

    def insertInternal(self,node,val):
        # out condition
        if node.isNull():
            return Node.newNode(val)
        conflict = False
        # 1.judge left or right and check if have conflict
        if val>node.val:
            node.right = self.insertInternal(node.right,val)
            node.right.parent = node
            if node != self.root:
                if node.isRed() and node.right.isRed():
                    conflict=True
        else:
            node.left = self.insertInternal(node.left,val)
            node.left.parent = node
            if node!=self.root:
                if node.isRed() and node.left.isRed():
                    conflict = True
        ##      b
        ##   r     b
        ## r

        if self.ll:
            node = self.rightRotate(node)
            node.color = BLACK
            node.right.color = RED
            self.ll=False
        elif self.lr:
            node.left = self.leftRotate(node.left)
            node.left.parent = node.left
            node = self.rightRotate(node)
            node.color = BLACK
            node.right.color = RED
            self.lr=False
        elif self.rr:
            node = self.leftRotate(node)
            node.color = BLACK
            node.left.color = RED
            self.rr=False
        elif self.rl:
            node.right = self.rightRotate(node.right)
            node.right.parent = node
            node =self.leftRotate(node)
            node.color = BLACK
            node.left.color = RED
            self.rl=False

        if conflict:
            sibling = node.sibling()
            if sibling.isBlack():
                if node.isLeft():
                    if node.left.isRed():
                        self.ll=True
                    else:
                        self.lr=True
                else:
                    if node.left.isRed():
                        self.rl = True
                    else:
                        self.rr = True
            else:
                node.color = BLACK
                sibling.color = BLACK
                if node.parent!=self.root:
                    node.parent.color = RED

        return node


    def search(self,val,node):
        if node.val==val:
            return node
        if val>node.val:
            return self.search(val,node.right)
        else:
            return self.search(val,node.left)

    def delete(self,val):
        node = self.search(val,self.root)
        self.deleteNode(node)
    # steps:
    #  1.BST commmon delete
    #  2.fix double Black
    #
    def successorNode(self,node):
        if node.isLeaf():
            return node
        if node.left.isNull:
            cur = node.right
            while not cur.isLeaf():
                cur = cur.left
            return cur
        return node.left
    def deleteNode(self,node):
        successorNode = self.successorNode(node)
        if node.isLeaf():
            if node.isRed():
                node.delete()
            else:
                # checkDoubleBlack
                self.fixBlackLack(node)
                node.delete()
            return
        if node.left.isNull() or node.right.isNull():
            if node.isRed():
                if node.left.isNull():
                    node.parent.right = node.right
                    node.right.parent =  node.parent
                else:
                    node.parent.left = node.left
                    node.left.parent = node.parent
            else:
                if node.isLeft():
                    node.parent.left=successorNode
                    successorNode.parent = node.parent
                else:
                    node.parent.right = successorNode
                    successorNode.parent = node.parent
                self.fixBlackLack(successorNode)
                # checkDoubleBlack
            return

        successorNode.val,node.val = node.val,successorNode.val
        self.deleteNode(successorNode)
    # Why need check black?
    # When we want to delete a black node,the black path change,fixing double black's goal is to dismiss the effect on it
    # Key point is that can we get a red node from the other side(sibling)
    #     b
    #b(s)   b
    #         r
    def fixBlackLack(self,node):
        if node==self.root:
            return
        parent = node.parent
        sibling = node.sibling()
        if sibling.isBlack():
            if sibling.left.isRed() or sibling.right.isRed():
                newParent = None
                gp = parent
                if sibling.isRight():
                    if sibling.right.isRed():
                        sibling.right.color = BLACK
                        newParent = self.leftRotate(parent)
                    else:
                        sibling.left.color = BLACK
                        parent.right = self.rightRotate(sibling)
                        parent.right.parent = parent
                        newParent = self.leftRotate(parent)
                else:
                    # left sibling
                    if sibling.left.isRed:
                        sibling.left.color = BLACK
                        newParent = self.rightRotate(parent)
                    else:
                        sibling.right.color = BLACK
                        parent.left = self.leftRotate(sibling)
                        parent.left.parent = parent
                        newParent = self.rightRotate(parent)
                if not gp:
                    if newParent.isLeft():
                        gp.left = newParent
                        gp.left.parent=  gp
                    else:
                        gp.right=newParent
                        gp.right.parent = gp
                return
            else:
                # s:b no red children
                sibling.color=RED
                if parent.isBlack():
                    self.fixBlackLack(parent)
                else:
                    parent.color = BLACK

        else:
            # red sibling
            gp = parent.parent
            sibling.color = BLACK
            parent.color = RED
            if sibling.isRight():
                newParent = self.leftRotate(parent)
                self.fixBlackLack(parent.left)
            else:
                newParent = self.rightRotate(parent)
                self.fixBlackLack(parent.right)
            if not gp:
                if newParent.isLeft:
                    gp.left = newParent
                    gp.left.parent = gp
                else:
                    gp.right = newParent
                    gp.right.parent = gp




    def leftRotate(self,node):
        right = node.right
        node.right = right.left
        node.right.parent = node
        right.left = node
        right.left.parent = node
        return right
    def rightRotate(self,node):
        left = node.left
        node.left = left.right
        node.left.parent = node
        left.right = node
        left.right.parent = node
        return left
    def inorder(self):
        def traverse(node):
            cur=[]
            if node.isNull():
                return cur
            cur.extend(traverse(node.left))
            cur.append(node.val)
            cur.extend(traverse(node.right))
            return cur
        return traverse(self.root)
    def height(self):
        def getHeight(node):
            if node.isNull():
                return 0
            return max(getHeight(node.left),getHeight(node.right))+1
        return getHeight(self.root)

    def printTree(self):
        def traverse(node, level=0, label=''):

            if node.isNull():
                return
            print('   ' * level, label, node.val, '(' + ("b" if node.color==BLACK else "r") + ')')
            traverse(node.left, level + 1, 'L:')
            traverse(node.right, level + 1, 'R:')

        traverse(self.root)



if __name__ == '__main__':
    tree = RBTree()
    tree.insert(1).insert(2).insert(3).insert(4).insert(5).insert(6)
    tree.delete(6)
    tree.delete(5)
    tree.print_binary_tree()