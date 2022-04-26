#import the random lib to generate random numbers
from random import randrange
 
 
# A Treap Node
class TreapNode:
    
    def __init__(self, data, priority=100, left=None, right=None):
        #Initializing data
        self.data = data
        #Initializing priority
        self.priority = randrange(priority)
        #Initializing left
        self.left = left
        #Initailizing right
        self.right = right

#recursive function to left rotate a given key.
def rotateLeft(root):
    #stores the right node of root in R
    R = root.right
    X = root.right.left
#stores the value of left node of R in X.
 
    # rotates structure and the initial root becomes left node of the R and X becomes right node of the initial root 
    R.left = root
    root.right = X
 
    # here, R is set as a new root.
    return R
 
# recursive function to right rotate a given treap.
def rotateRight(root):
    # initialises the left node of root as L and Y as right node of Y.
    L = root.left
    Y = root.left.right
 
    # rotate the given treap and the initial root becomes right node of L and Y becomes left node of the initial root.
    L.right = root
    root.left = Y
 
    # L becomes   the new root of the treap 
    return L
 
 
# Defining a recursive function to insert a given key with a priority into treap
def insertNode(root, data):
 
    #base case: if root is none
    if root is None:
	#return the data by calling function TreapNode
        return TreapNode(data)
 
    # if the given data is less than the root node
    if data < root.data:
	#insert in the left subtree
        root.left = insertNode(root.left, data)
 
        #if heap property is violated
        if root.left and root.left.priority > root.priority:
            #rotate right
            root = rotateRight(root)
    else:
        # If not left, insert in the right subtree
        root.right = insertNode(root.right, data)
 
        # rotate left if the heap property is violated
        if root.right and root.right.priority > root.priority:
            root = rotateLeft(root)
    #return the root
    return root
 
 
# Defining a recursive function to search for a key in a given treap
def searchNode(root, key):
 
    # if the key is not present in the tree
    if root is None:
        #return false if it is not there
        return False
 
    # if the key is found
    if root.data == key:
        #return true if it is there
        return True
 
    # if the key is less than the root node
    if key < root.data:
        #calling the searchNode function again and searching in left subtree
        return searchNode(root.left, key)
 
    # if the key is greater than the root node
    #calling the searchNode function again and searching in right subtree
    return searchNode(root.right, key)
 
 
#Defining a recursive function to delete a key from a given treap
def deleteNode(root, key):
 
    # base case: the key is not found in the tree
    if root is None:
	#return none
        return None
 
    # if the key is less than the root node
    if key < root.data:
      #recur the function again in left subtree
        root.left = deleteNode(root.left, key)
 
    # if the key is more than the root node
    elif key > root.data:
        #recur the function in right subtree
        root.right = deleteNode(root.right, key)
 
    # if the key is found
    else:
 
        # Case 1: node to be deleted has no children (it is a leaf node)
        if root.left is None and root.right is None:
            # deallocate the memory and update root to None
            root = None
 
        # Case 2: node to be deleted has two children
        elif root.left and root.right:
            # if the left child has less priority than the right child
            if root.left.priority < root.right.priority:
                # call `rotateLeft()` on the root
                root = rotateLeft(root)
 
                # recursively delete the left child
                root.left = deleteNode(root.left, key)
            else:
                # call `rotateRight()` on the root
                root = rotateRight(root)
 
                # recursively delete the right child
                root.right = deleteNode(root.right, key)
 
        # Case 3: node to be deleted has only one child
        else:
            # choose a child node
            child = root.left if (root.left) else root.right
            root = child
    #returning the root value
    return root
 
 
# Utility function to print two-dimensional view of a treap using
# reverse inorder traversal
def printTreap(root, space):
    #defining the height of the treap
    height = 10
 
    # Base case
    if root is None:
        #if root is none then return
        return
 
    # increase the distance between levels
    space += height
 
    # print the right child first
    printTreap(root.right, space)
 
    # print the current node after padding with spaces
    for i in range(height, space):
        print(' ', end='')
    #printing the data and priority of root
    print((root.data, root.priority))
 
    # print the left child
    printTreap(root.left, space)

def s_op():
    # taking some random treap keys
    keys = [5, 2, 1, 4, 9, 8, 10]
         
    # constructing a treap, initial root is none
    root = None
    for key in keys:
        #inserting each keys in treap
        root = insertNode(root, key)
    #printing the constructed treap
    print("Constructed :\n\n")
    printTreap(root, 0)
    while(1):
        #giving option to user to select
        print("\n\nSelect any option from below to perform respective operation")
        print("1. Insert Node")
        print("2. Search Node")
        print("3. Delete Node")
        print("4. Exit")
        #taking input from user to perform operation
        select=int(input("Enter your choice: "))
        #if selected option is 1 then perform insert
        if select==1:
            #taking node value from user to insert into treap
            i1=int(input("\nInsert node: "))
            #inserting the node value given by user by calling insertNode function
            root = insertNode(root, i1)
            #printing the treap
            printTreap(root, 0)
        #if selected option is 2 then perform search
        elif select==2:
            #taking node value from user to search into treap
            s1=int(input("\nSearch node: "))
            #if the node is present then print true else false by calling searchNode function
            print(searchNode(root, s1))
        #if selected option is 3 then perform delete   
        elif select==3:
            #taking node value from user to delete from treap
            d1=int(input("\nDelete node: "))
            #deleting the node value taken from user by calling deleteNode function
            root = deleteNode(root, d1)
            #printing the treap after deleting the node
            printTreap(root, 0)
        #if selected option is 4 then exit 
        elif select==4:
            exit
            break
        #else not a valid choice go back again
        else:
            print("\nPlease enter valid choice\n")   
#to check whether the current script is running own or being imported somewhere
if __name__ == '__main__':
    #calling the s_op function to construct and to perform operations
    s_op()
    
    




