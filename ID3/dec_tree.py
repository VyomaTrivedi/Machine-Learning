class Node():

      def __init__(self,pos,neg): 

          self.attr = -1
          self.pos = pos
          self.neg = neg
          self.split = -1
          self.label = None
          #self.level = None
          self.left = None
          self.right= None
          self.parent = None

class dec_tree():

    def __init__(self,pos,neg):

        self.root = Node(pos,neg)
        self.count = 1
        self.leafs = 0
        self.leaf_list = []

    def start(self,pos,neg):

        self.root = Node(pos,neg)
        self.count += 1

    def update_count(self,count):
        self.count = count

    def return_root(self):
        return self.root

    def return_num_leaf(self):
        return self.leafs   

    def return_parent(self,node):
        return node.parent

    def return_count(self):
        return self.count
      
    def return_left(self):
        return self.left

    def return_right(self):
        return self.right

    def return_leaf_list(self):
        return self.leaf_list

    def add_children(self,node,lp,ln,rp,rn,attr):

        node.attr = attr
        node.left = Node(lp,ln)
        node.left.split = 0
        node.left.parent = node
        node.right = Node(rp,rn)
        node.right.split = 1
        node.right.parent = node
        self.count += 2

    def determine_which_node(self,tree):

        if self.count == 0 :
            return 0
        elif self.count == 1 :
            return tree.root
        else:
            thislevel = [tree.root]
            while thislevel:
                nextlevel = list()
                for n in thislevel:


                    if n.left :
                        if ((n.left.pos == 0)or(n.left.neg == 0)) :
                            if (n.left.pos == 0) :
                                n.left.label = 0                                
                            elif (n.left.neg == 0) :
                                n.left.label = 1                                    
                        else :
                            nextlevel.append(n.left)
                    elif (n.label != (-1)) :
                        return n
                    else :
                        continue
                        
                    if n.right :
                        if ((n.right.pos == 0)or(n.right.neg == 0)) :
                            if (n.right.pos == 0) :
                                n.right.label = 0
                            elif (n.right.neg == 0) :
                                n.right.label = 1                                    
                        else :
                            nextlevel.append(n.right)
                    elif (n.label != (-1)) :
                        return n
                    else :
                        continue
                    
                thislevel = nextlevel

    def display(self,node):
        if(node.left != None):
            display(node.left)
        print (node.attr)        
        if(node.right != None):
            display(node.right)

    def traverse(self,rootnode):
      thislevel = [rootnode]      
      while thislevel:
        nextlevel = list()
        for n in thislevel:
          if n.attr == -1:
                self.leafs += 1
                self.leaf_list.append(n)
          if n.left: nextlevel.append(n.left)
          if n.right: nextlevel.append(n.right)
        print
        thislevel = nextlevel
