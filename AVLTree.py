# Group Members: Michael Jung (ID:10680322), Timothy Sanders (01002147), Megan Ng (ID: 00756276)

# Date: 4/21/25

# Course: Spr25_CS_034 CRN 39575
#--------------------------------------------------------------------------------------------
# Create a test tree manually
#          50                                                  
#        /    \                                                 
#       30     70                                                
#     /   \   /   \                                               
#    20   40  60   80    
# The tree above is balanced since all the balance factors are between {-1, 0, 1}
# The Balance Factor for each node are: 50:0, 30:0,70:0, 20:0, 40:0, 60:0, 80:0
# Print AVL Tree with indentation
# Print the nodes pre-order, in-order, post-order to visualize the balancing of tree after the deletion and insertion of nodes
# ######################################################

from Node import Node

# --- AVL Tree Class ---
class AVLTree():

