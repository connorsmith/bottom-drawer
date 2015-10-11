class TreeNode:
    def __init__(self, val = None,  parent = None, leftChild = None, rightChild = None):
        self.parent = parent
        self.val = val
        self.leftChild = leftChild
        self.rightChild = rightChild

    def getVal(self):
        return self.val

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def getParent(self):
        return self.parent

    def replaceData(self, val, leftChild, rightChild):
        self.val = val
        
        self.leftChild = leftChild
        if self.leftChild:
            self.leftChild.parent = self

        self.rightChild = rightChild
        if self.rightChild:
            self.rightChild.parent = self

    def getDepth(self):
        pass

class BinaryTree:
    def __init__(self, root = TreeNode):
        self.root = root

    def insertVal(self, val, currentNode):
        if val < currentNode.val:
            lc = currentNode.getLeftChild()
            if lc:
                self.insertVal(val, lc)
            else:
                currentNode.leftChild = TreeNode(val, currentNode)
        else:
            rc = currentNode.getRightChild()
            if rc:
                self.insertVal(val, rc)
            else:
                currentNode.rightChild = TreeNode(val, currentNode)

    def isSuperbalanced(self):
        return 
        ''' Check to see if the max level diff between any leaves is one or less '''
        superbalanced = True

        lc = root.getLeftChild()
        if lc:
            superbalanced = superbalanced and lc.isSuperbalanced()
        else:
            pass

        rc = root.getRightChild()
        if rc:
            depthOfRightSubtree = rc.getDepth()
        else:
            depthOfRightSubtree = 0

        if abs(depthOfRightSubtree - depthOfLeftSubtree) <= 1:
            return True
        else:
            return False

    def printVals(self, currentNode, depth = 0):
        if currentNode:
            spaceString = '-' * depth
            print('%s%s'%(spaceString, currentNode.val))
            self.printVals(currentNode.getLeftChild(), depth+1)
            self.printVals(currentNode.getRightChild(), depth+1)
        else:
            return 

def main():
    t = BinaryTree(TreeNode(10))
    t.insertVal(5, t.root)
    t.insertVal(15, t.root)
    t.insertVal(20, t.root)
    t.insertVal(0, t.root)
    t.insertVal(1, t.root)
    t.insertVal(6, t.root)
    t.printVals(t.root)

if __name__ == "__main__":
    main()

