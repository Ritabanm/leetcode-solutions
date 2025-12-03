class Solution:
    def treeQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        edge_weight_curr = {}

        x = defaultdict(list)
        for i,j,k in edges:
            x[i].append((j,k))
            x[j].append((i,k))
            
            edge_weight_curr[min(i,j),max(i,j)] = k

        class tree_node:
            def __init__(self):
                self.l = None
                self.r = None
                self.val = inf
                self.lazy = 0
        
        
        tour = []
        root_dist = {}
        #depth = {}
        parent = {}
        node_to_tour_index = {}



        def eulers_tour(i, par = -1, dist = 0, dep = 0):
            tour.append(i)
            root_dist[i] = dist
            #depth[i] = dep
            parent[i] = par

            for j,k in x[i]:
                if j!=par:
                    eulers_tour(j, i, dist + k, dep + 1)
                    tour.append(i)
        
        eulers_tour(1)

        for i in range(len(tour)):
            if tour[i] in node_to_tour_index:
                a,b = node_to_tour_index[tour[i]]
                node_to_tour_index[tour[i]] = [min(a,i),max(a,i)]
            else:
                node_to_tour_index[tour[i]] = [i,i]
        
        tn = len(tour)

        def insert_weight(node, i, j):
            
            if i>j:return

            if i==j:
                
                node.val = root_dist[tour[i]]
                #print('insert', i, j, node.val)
                return 
            
            m = (i+j)//2
            if not node.l:
                node.l = tree_node()
            if not node.r:
                node.r = tree_node()
            
            insert_weight(node.l, i, m)
            insert_weight(node.r, m+1, j)
        
        lazy = {}

        def update_weight(node, i, j, qi, qj, val):
            if qi>j or qj<i or i>j:
                return
            
            if node.lazy!=0:
                
                if node.l:
                    node.l.lazy+= node.lazy
                if node.r:
                    node.r.lazy+= node.lazy
                if i==j:
                    node.val+= node.lazy
                
                node.lazy = 0

            if qi<=i and qj>=j:
                node.lazy+= val

                #print(i,j, qi, qj, val, node.lazy)

                return 
            
            m = (i+j)//2
            update_weight(node.l, i,m,qi,qj,val)
            update_weight(node.r, m+1,j,qi,qj,val)
        
        def get_weight(node, i,j, ind):
            
            if ind<i or ind>j or i>j or not node:
                return 0
            
            #print('get weight', i,j, ind, node.val, node.lazy)

            if node.lazy!=0:
                
                if node.l:
                    node.l.lazy+= node.lazy
                if node.r:
                    node.r.lazy+= node.lazy
                if i==j:
                    node.val+= node.lazy 
                
                node.lazy = 0
                
            if i==j==ind:
                
                return node.val
            
            m = (i+j)//2
            return get_weight(node.l, i,m, ind) + get_weight(node.r, m+1, j, ind)

        weight_node = tree_node()
        insert_weight(weight_node, 0, tn - 1)

        
        res = []
        for i in queries:
            if i[0]==2:
                qi, qj = node_to_tour_index[i[1]]
                res.append(get_weight(weight_node, 0, tn-1, qi))

            else:
                a, b = i[1:3]
                if parent[b]==a:
                    a = b

                qi, qj = node_to_tour_index[a]

                #curr_weight = get_weight(weight_node, 0, tn-1, qi)
                curr_weight = edge_weight_curr[min(i[1],i[2]), max(i[1],i[2])]

                val = i[-1] - curr_weight

                edge_weight_curr[min(i[1],i[2]), max(i[1],i[2])] = i[-1]

                #print(a, qi, qj, curr_weight, val, edge_weight_curr)

                update_weight(weight_node, 0, tn-1, qi, qj, val)

        #print(tour, root_dist)
        #print(node_to_tour_index)

        return res