# Movielens-1M-Classified
## This is an edited version of movielens-1m dataset
### Original dataset: movielens-1m-original
This folder contains movielens-1m dataset in the original format from Koblenz Network Collection. 

The meaning of the columns in out.movielens-1m are: 
    First column: ID of from node;
    Second column: ID of to node;
    Third column: edge weight;
    Fourth column: timestamp of the edge;



### Static dataset: movielens-1m
This folder contains static version of full movielens-1m dataset. The original movielens-1m dataset provides node attribute as users and items. We further classify the nodes into more types by the number of edges they have. Nodes with more edges belong to attributes with higher numbers. The files node_attr.txt and edge.txt respectively denotes the node attributes and edge attributes, where the last column is the attribute. The files node_attr_sub.txt and edge_sub.txt denotes note attributes and edge attributes for a sub-graph of movielens-1m, which we used for graph alignment task, where ground_truth.txt records the correct match.

This static version of movielens-1m can be obtained by running dataprocessing.py. The number of nodes in the sub-graph can be adjusted by hyperparameter NUM_NODES_SUB.



### Temporal dataset: movielens-1m-temporal
This folder contains temporal version of movielens-1m dataset. node_attr.txt and edge.txt file is the same as that in static dataset. We add files with suffix "_sorted" as edges sorted by timestamps. The files with suffix "_initial" records the initial graph.

Similar to static dataset movielens-1m, files with "_sub" is for the sub-graph alignment task, and the ground_truth.txt file contains the correct match.

This temporal version of movielens-1m can be obtained by running dataprocessing_temporal.py. The number of edges in the initial graph can be adjusted by hyperparameter INITIAL_RATIO.



### DINGAL-fitting dataset: movielens-1m-dingal
This folder contains movielens-1m dataset in the DINGAL format, which is from the paper "Dynamic Knowledge Graph Alignment", AAAI 2021. The code to run DINGAL on movielens-1m, bitcoinalpha and wikilens is provided at https://github.com/Violet24K/Simplified_DINGAL.

This version can be obtained by running dataprocessing_dingal.py.



### change_file
This folder contains change lists for two scenarios in our research work: node attribute change and edge attribute change. For the file node_attr_change.txt, the first column is the node to change in the subgraph, and the second column is the attribute that this node is changing to. For the file edge_attr_change.txt, the first and second column is the edge to change in the whole graph (not in the sub-graph), and the third column is the attribute that this edge is changing to.



## Reference
If you're using this processed temporal dataset, please consider citing our research work:
```
@inproceedings{DBLP:conf/www/LiFH23,
  author       = {Zihao Li and
                  Dongqi Fu and
                  Jingrui He},
  title        = {Everything Evolves in Personalized PageRank},
  booktitle    = {Proceedings of the {ACM} Web Conference 2023, {WWW} 2023, Austin,
                  TX, USA, 30 April 2023 - 4 May 2023},
  pages        = {3342--3352},
  publisher    = {{ACM}},
  year         = {2023},
  url          = {https://doi.org/10.1145/3543507.3583474},
  doi          = {10.1145/3543507.3583474},
  timestamp    = {Tue, 02 May 2023 14:07:23 +0200},
  biburl       = {https://dblp.org/rec/conf/www/LiFH23.bib},
  bibsource    = {dblp computer science bibliography, https://dblp.org}
}
```