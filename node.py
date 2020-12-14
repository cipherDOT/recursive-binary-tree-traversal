

# Node object :
# {
#   contains a left and right member,
#   which are also nodes (that is how we define them)
# }
class Node(object):
    def __init__(self, value):
        self.value = value
        # we set the initial values of the left , right members
        # as None, and we later define them as Nodes themselves
        self.left = None
        self.right = None

    def traverse(self):
        # we print the value of the node we are visiting.
        print(self.value, end=" ")

        # if there is left member traverse it...
        if self.left:
            self.left.traverse()

        # if there is right member traverse it...
        if self.right:
            self.right.traverse()


# the tree, hard - coded.
node = Node(8)
node.left = Node(3)
node.right = Node(10)
node.left.left = Node(1)
node.left.right = Node(6)
node.left.right.left = Node(4)
node.left.right.right = Node(7)
node.right.right = Node(14)
node.right.right.left = Node(13)

if __name__ == "__main__":

    # we need to traverse the initial node, but
    # since the traverse method is recursive, it prints the whole tree
    node.traverse()
