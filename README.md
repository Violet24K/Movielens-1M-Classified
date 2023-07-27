# Movielens-1M-Classified
## This is an edited version of movielens-1m dataset
### Original dataset: movielens-1m-original
This folder contains movielens-1m dataset in the original format from Koblenz Network Collection. 

The meaning of the columns in out.movielens-1m are: 
    First column: ID of from node 
    Second column: ID of to node
    Third column: edge weight
    Fourth column: timestamp of the edge


### Static dataset: movielens-1m
This folder contains static version of full movielens-1m dataset. The files node_attr.txt and edge.txt respectively denotes the node attributes and edge attributes, where the last column is the attribute. The files node_attr_sub.txt and edge_sub.txt denotes note attributes and edge attributes for a sub-graph of movielens-1m, which we used for graph alignment task, where ground_truth.txt records the correct match.

This static version of movielens-1m can be obtained by running dataprocessing.py.




### Temporal dataset: movielens-1m-temporal




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