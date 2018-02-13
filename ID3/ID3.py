import sys
from random import randint
from math import log
from dec_tree import *

# declaring variables

pos = []
neg = []
data = []
num_of_attr = 0
num_of_instances = 0
num_of_test_instances = 0
attr_used = []
attr_names = []
lst1=''
lst2=''

#calculating entropy of output class

def calc_entropy():
    global pos,neg,data,num_of_attr,num_of_instances,a,attr_names
    a=2
    file = open(train)

    for line in file:
        data += [line.split()]

    
    num_of_attr = len(data[0])-1
    attr_names.append(data[0][0:num_of_attr])
    num_of_instances = len(data)-1

    for i in range(num_of_attr+1):
        column = [x[i] for x in data]
        p=0
        n=0
        for j in column:
        #print j
            if ( j== '1' ):
                p=p+1
            elif (j == '0'):
                n=n+1
            
        pos.append(p)
        neg.append(n)
        
    pos_prob = float(pos[num_of_attr])/num_of_instances
    neg_prob = float(neg[num_of_attr])/num_of_instances

    entropy_of_label = (-pos_prob*log(pos_prob,2)) + (-neg_prob*log(neg_prob,2))

    return entropy_of_label

#selecting the splitting attribute at root based on information gain(i.e minimum conditional enropy)

def select_first_attribute() :
    global data,num_of_attr,num_of_instances,neg,attr_used
    
    ctr0=0
    ctr1=0
    label = []
    avg_entropies = []

    for d in range(1,num_of_instances+1):
        label.append(int(data[d][num_of_attr]))

    for i in range(num_of_attr):
        if i in attr_used:
            continue
        else:
            column = [x[i] for x in data]
            ctr0=ctr1=lp=rn=0

            for j in range(num_of_instances):
                if ((column[j+1] == '0')and(label[j] == 0)):
                    ctr0 = ctr0+1
                if ((column[j+1] == '1')and(label[j] == 1)):
                    ctr1 = ctr1+1
                if ((column[j+1] == '0')and(label[j] == 1)):
                    lp += 1
                if ((column[j+1] == '1')and(label[j] == 0)):
                    rn += 1

            neg_con_ent=float(-(float(ctr0)/neg[i])*log((float(ctr0)/neg[i]),2)) + float(-((float(neg[i]-ctr0))/neg[i])*log((float(neg[i]-ctr0)/neg[i]),2))
            pos_con_ent=float(-(float(ctr1)/pos[i])*log((float(ctr1)/pos[i]),2)) + float(-((float(pos[i]-ctr1))/pos[i])*log((float(pos[i]-ctr1)/pos[i]),2))

            avg_entropies.append(((float(neg[i])/num_of_instances)*neg_con_ent)+((float(pos[i])/num_of_instances)*pos_con_ent))

        attr_used.append(avg_entropies.index(min(avg_entropies)))
    index_of_attr = avg_entropies.index(min(avg_entropies))

    tree.add_children(tree.determine_which_node(tree),lp,ctr0,ctr1,rn,index_of_attr)


def get_splitting_node():
    print(tree.determine_which_node(tree)).pos
    print(tree.determine_which_node(tree)).neg
            
def split_entropy():
    global data,num_of_attr
    pos_current = (tree.determine_which_node(tree)).pos
    neg_current = (tree.determine_which_node(tree)).neg
    pos_cprob = float(pos_current)/(pos_current + neg_current)
    neg_cprob = float(neg_current)/(pos_current + neg_current)    
    entropy_of_current_node = (-pos_cprob*log(pos_cprob,2)) + (-neg_cprob*log(neg_cprob,2))
    path_attributes = []
    path = []
    node = tree.determine_which_node(tree)
    temp = tree.determine_which_node(tree)
    while (node != tree.return_root()):
        path_attributes.append(tree.return_parent(node).attr)
        path.append(node.split)
        node = node.parent
    if (len(path_attributes)==num_of_attr):
        if (temp.pos>temp.neg):
            temp.label = 1
        elif (temp.pos<temp.neg):
            temp.label = 0

    attr_left = []
    avg_entropies = []
    for i in range(num_of_attr):
        if i in path_attributes:
            continue
        else:
            attr_left.append(i)
            count = 0
            ctr0=0
            ctr1=0
            lp = 0
            rn = 0
            tot_neg = 0
            tot_pos = 0
            neg_con_ent = 0
            pos_con_ent = 0            
            subset_data = []
            column = [x[i] for x in data]
            for j in range(1,num_of_instances+1):

                count = 0
                for k in range(len(path)):                
                    if ( int(data[j][path_attributes[k]]) == path[k] ):
                        count += 1                    
                if ( count == len(path) ):
                    subset_data.append(j)                

            for l in range(len(subset_data)):                
                if ((data[subset_data[l]][i] == '0') and (data[subset_data[l]][num_of_attr] == '0')):
                    ctr0 += 1
                if ((data[subset_data[l]][i] == '1') and (data[subset_data[l]][num_of_attr] == '1')):
                    ctr1 += 1
                if ((data[subset_data[l]][i] == '0') and (data[subset_data[l]][num_of_attr] == '1')):
                    lp += 1
                if ((data[subset_data[l]][i] == '1') and (data[subset_data[l]][num_of_attr] == '0')):
                    rn += 1
                if (data[subset_data[l]][i] == '0'):
                    tot_neg += 1
                    #print (tot_neg)
                if (data[subset_data[l]][i] == '1'):
                    tot_pos += 1
            neg_con_ent=float(-(float(ctr0)/tot_neg)*log((float(ctr0)/tot_neg),2)) + float(-((float(tot_neg-ctr0))/tot_neg)*log((float(tot_neg-ctr0)/tot_neg),2))
            pos_con_ent=float(-(float(ctr1)/tot_pos)*log((float(ctr1)/tot_pos),2)) + float(-((float(tot_pos-ctr1))/tot_pos)*log((float(tot_pos-ctr1)/tot_pos),2))
            avg_entropies.append(((float(tot_neg)/len(subset_data))*neg_con_ent)+((float(tot_pos)/len(subset_data))*pos_con_ent))
    attr_to_split = attr_left[avg_entropies.index(min(avg_entropies))]
    tree.add_children(tree.determine_which_node(tree),lp,ctr0,ctr1,rn,attr_to_split)
    return 1

#testing accuracy of the test file

def test(test_file):
    global num_of_test_instances
    test_file = open(test_file)
    test_data = []
    matches = 0
    testing_accuracy = 200
    for line in test_file:
        test_data += [line.split()]

    num_of_test_instances = len(test_data)-1
    current = Node(0,0)
    current_attr = -2
    
    for i in range(1,num_of_test_instances + 1):
        current = tree.return_root()
        flg = 1
        while (flg): 
            current_attr = current.attr
            if(data[i][current_attr] == '0'):
                current=current.left
                if (current.attr == -1):
                    if (current.pos > current.neg):
                        current.label = 1
                    elif (current.pos < current.neg):
                        current.label = 0
                    flg = 0
            elif(data[i][current_attr] == '1'):
                current=current.right
                if (current.attr == -1):
                    if (current.pos > current.neg):
                        current.label = 1
                    elif (current.pos < current.neg):
                        current.label = 0
                    flg = 0
        if (current.label == int(data[i][num_of_attr])):
            matches += 1
    testing_accuracy = ((float(matches)/num_of_test_instances))*100
    return (testing_accuracy)

#pruning based on the pruning factor
    
def pruning():
    nodes = []
    a=0
    num_of_nodes_pruned = int((pruning_factor) * (tree.return_count()))
    nodes = tree.return_leaf_list()
    while(num_of_nodes_pruned>0):
        node_num = randint(0,(len(nodes)-1))
        prun = nodes[node_num]
        if (prun.parent.right == prun):
            if (prun.parent.left !=None):
                nodes.remove(prun.parent.left)
                nodes.remove(prun)
        elif (prun.parent.left == prun):
            if (prun.parent.right != None):
                nodes.remove(prun.parent.right)
                nodes.remove(prun)                
        prun_parent = tree.return_parent(prun)
        prun_parent.attr = -1
        if (prun_parent.left != None):
            prun_parent.left = None
            num_of_nodes_pruned -= 1
            a+=1
            tree.update_count((tree.return_count())-1)
        if (prun_parent.right != None):
            prun_parent.right = None
            a+=1
            tree.update_count((tree.return_count())-1)
            num_of_nodes_pruned -= 1
        if (prun_parent.pos>prun_parent.neg):
            prun_parent.label = 1
        elif (prun_parent.pos<prun_parent.neg):
            prun_parent.label = 0
    return a
    

#traversing the tree in pre-order
            
def preorder(node,ctr0):
    global lst1,lst2
    if node.left:
        ctr0+=1
        lst1+=attr_names[0][node.attr]

        lst1+='= 0'

        preorder(node.left)
    print (lst1)
    lst1=''
    if node.right:
        ctr1+=1
        lst1+=attr_names[0][node.attr]

        lst1+='= 1'     

        preorder(node.right)
    print (lst1)

#printing the tree
    
def DisplayTree(node, count):
    if node.left != None:
        s = "| "*(count + 1)
        print s,
        if(node.left.left != None):
            print (attr_names[0][node.attr]), "=", "0", ":"
        else:
            print (attr_names[0][node.attr]), "=", "0", ":",
        DisplayTree(node.left,count + 1)
    else: 

        print (node.label)
    if node.right != None:
        s = "| "*(count + 1)
        print s,
        if(node.right.right!=None):
            print (attr_names[0][node.attr]), "=", "1", ":"
        else:
            print (attr_names[0][node.attr]), "=", "1", ":",
        DisplayTree(node.right,count + 1)     

#function calls
    
node = Node(0,0)
temp = Node(0,0)
prun = Node(0,0)
prun_parent = Node(0,0)
t1=0
t2=0

#taking input from the user

train = raw_input("Enter training file path:")
test_path = raw_input("Enter test file path:")
pruning_factor = float(input("Enter pruning factor:"))

calc_entropy()

tree = dec_tree(pos[num_of_attr],neg[num_of_attr])

select_first_attribute()

while (1):
    try:
        split_entropy()
    except ValueError:
        break

node=tree.return_root()
t1=test(train)
t2=test(test_path)
tree.traverse(node)

print ("Tree before pruning")
print("______________________")
print('\n')
DisplayTree(node, 0)
print ('\n')
print ('Pre-Pruned Accuracy')
print ('---------------------')
print ('Number of training instances = ',num_of_instances)
print ('Number of training attributes(including label) = ',(num_of_attr+1))
print ("Total number of nodes in the tree = ",(tree.return_count()))
print ("Number of leaf nodes in the tree = ",tree.return_num_leaf())
print ("Accuracy of the model on the training dataset = ",t1)
print ('\n')
print ("Number of testing instances = ",num_of_test_instances)
print ("Number of testing attributes = ",num_of_attr)
print ("Accuracy of the model on the testing dataset = ",t2)
print ('\n')

p=pruning()
#tree.traverse(node)
t11=test(train)
t22=test(test_path)

print ("Tree after pruning")
print("______________________")
print('\n')
DisplayTree(node, 0)
print('\n')
print ("Post-Pruned Accuracy")
print ("---------------------")
print ("Number of training instances = ",num_of_instances)
print ("Number of training attributes(including label) = ",(num_of_attr+1))
print ("Total number of nodes in the tree = ",(tree.return_count()-1))
print p
print ("Number of leaf nodes in the tree = ",(tree.return_num_leaf()-p))
print ("Accuracy of the model on the training dataset = ",t11)
print ("\n")
print ("Number of testing instances = ",num_of_test_instances)
print ("Number of testing attributes = ",num_of_attr)
print ("Accuracy of the model on the testing dataset = ",t22)
