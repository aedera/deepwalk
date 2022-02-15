# DeepWalk

This repo is a simple adaption of the original DeepWalk available here

https://github.com/phanein/deepwalk

to only extract walks from a list of edges. In other words, the optimization
step used for the original DeepWalk to build graph node embeddings is not
included.

## Installation

To install the DeepWalk shared here, your computer simply needs to have
installed Python 3.6 and Pip. If so, use this command

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

The above command outputs the walks to the standard output.
