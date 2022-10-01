from dataset_property import DATASET_SIZE
# 1 is sub nodes
sub_node = open('./movielens-1m-temporal/node_attr_sub.txt', 'r')
ent_ids_1_file = open('./movielens-1m-dingal/ent_ids_1', 'w')
for line in sub_node.readlines():
    items = line.strip().split(',')
    node_id = int(items[0])
    ent_ids_1_file.write(str(node_id + DATASET_SIZE) + '\t' + str(node_id + DATASET_SIZE) + '\n')
sub_node.close()
ent_ids_1_file.close()

# 2 is all nodes
all_node = open('./movielens-1m-temporal/node_attr.txt')
ent_ids_2_file = open('./movielens-1m-dingal/ent_ids_2', 'w')
for line in all_node.readlines():
    items = line.strip().split(',')
    node_id = items[0]
    ent_ids_2_file.write(items[0] + '\t' + items[0] + '\n')
all_node.close()
ent_ids_2_file.close()


# ref_ent_nodes: sub to whole
ground_truth_file = open('./movielens-1m-temporal/ground_truth.txt', 'r')
ref_ent_ids_file = open('./movielens-1m-dingal/ref_ent_ids', 'w')
for line in ground_truth_file.readlines():
    items = line.strip().split(',')
    node_in_whole = items[0]
    node_in_sub = items[1]
    ref_ent_ids_file.write(str(int(node_in_sub) + DATASET_SIZE) + '\t' + node_in_whole + '\n')
ground_truth_file.close()
ref_ent_ids_file.close()


# generate_embedding
embedding_file = open('./movielens-1m-dingal/generate_embedding.txt', 'w')

# triples_1: sub edges
sub_edge_file = open('./movielens-1m-temporal/edge_sorted_sub.txt', 'r')
triples_1_file = open('./movielens-1m-dingal/triples_1', 'w')
for line in sub_edge_file.readlines():
    items = line.strip().split(',')
    triples_1_file.write(str(int(items[0]) + DATASET_SIZE) + '\t' + items[2] + '\t' + str(int(items[1]) + DATASET_SIZE) + '\n')
    embedding_file.write(str(int(items[0]) + DATASET_SIZE) + '\t' + str(int(items[1]) + DATASET_SIZE) + '\t' + items[2] + '\n')
sub_edge_file.close()
triples_1_file.close()


# triples_2: whole graph edges
edge_file = open('./movielens-1m-temporal/edge_sorted.txt', 'r')
triples_2_file = open('./movielens-1m-dingal/triples_2', 'w')
for line in edge_file.readlines():
    items = line.strip().split(',')
    triples_2_file.write(items[0] + '\t' + items[2] + '\t' + items[1] + '\n')
    embedding_file.write(items[0] + '\t' + items[1] + '\t' + items[2] + '\n')
edge_file.close()
triples_2_file.close()

embedding_file.close()


