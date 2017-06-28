Filtering pre-trained word vectors
=======

Author: John Chung

This is a simple python script to filter through a pre-trained word vector file. The script will filter only a given word and its embeddings that exist in your training sets.

I specifically use Facebook's fastText pre-trained vectors.

https://github.com/facebookresearch/fastText/blob/master/pretrained-vectors.md

How to run (run from src folder):

`$ python filter_pre python filter_vecfile.py wiki.zh.vec`

In the example above, I am filtering a text file of pre-trained Chinese word vectors.

TODO: Error handling, Allow dimensionality as input.
