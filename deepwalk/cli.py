import sys
import random

from . import graph
from . import walks as serialized_walks

def deepwalk():
    if len(sys.argv) < 2:
        print('Usage:')
        print('$1 EDGE_FILE UNDIRECTED N_WALKS WALK_LEN SEED')
        sys.exit(1)

    edge_file  = sys.argv[1]
    undirected = bool(int(sys.argv[2])) # 0->False, 1->True
    n_walks    = int(sys.argv[3])
    walk_len   = int(sys.argv[4])
    seed       = int(sys.argv[5])

    G = graph.load_edgelist(edge_file, undirected=undirected)

    walks = graph.build_deepwalk_corpus(G,
                                        num_paths=n_walks,
                                        path_length=walk_len,
                                        alpha=0,
                                        rand=random.Random(seed))

    # print walks on standard output
    for w in walks:
        print(' '.join(w))
