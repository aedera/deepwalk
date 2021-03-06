# DeepWalk

This is a fork of the original DeepWalk available here

https://github.com/phanein/deepwalk

Unlike the original DeepWalk, this fork only extracts walks from a list of
edges, not including the optimization step used to build graph node
embeddings.

To build node embeddings, you can use any suitable optimizer. For example,
word2vec:

https://github.com/tmikolov/word2vec

## Installation

To install this fork, your computer simply needs to have installed Python 3.6
and Pip. If so, use this command

```bash
pip install -U "deepwalk @ git+https://github.com/aedera/deepwalk.git"
```

## Use

Once installed, DeepWalk can be run from command line with this command

```bash
deepwalk examples/edges.txt 0 2 10 1234
```

This extracts approximately 2 walks of length 10 from each node for the graph
described in the input file `examples/edges.txt` assuming directed edges (0,
use 1 to assume undirected edges). The last parameter (1234) sets a seed for
replication.

The above command outputs the walks to standard output.
