Filtering pre-trained word vectors
=======

Author: John Chung

This is a simple python script to filter through a pre-trained word vector file. The script will filter only a given word and its embeddings that exist in your training sets.

I specifically use Facebook's fastText pre-trained vectors.

https://github.com/facebookresearch/fastText/blob/master/pretrained-vectors.md

How to run (run from src folder):

`$ python filter_pre python filter_vecfile.py wiki.zh.vec`

In the example above, I am filtering a text file of pre-trained Chinese word vectors.

Using Dynet, loading the pre-trained embeddings would look something like this:

```
from dynet import *
from utils import Corpus
import numpy as np
from bleu import get_bleu_score

RNN_BUILDER = GRUBuilder

class nmt_dynet:
      def __init__(self, src_vocab_size, tgt_vocab_size, src_word2idx, src_idx2word, tgt_word2idx, tgt_idx2word, word_d, gru_d, gru_layers):
      .
      .
      .

      def load_src_preembeddings(self, filename):
          vocab = {}
          vectors = []
          with codecs.open(filename, "r", "utf-8") as f:
              f.readline()
              for i, line in enumerate(f):
                  fields = line.strip().split(" ")
                  vocab[fields[0]] = i
                  vectors.append(list(map(float, fields[1:])))

         pre_embeddings_list = []
         randomly_init_embeddings = np.random.rand(300)

         for key in sorted(self.src_idx2word):
              if self.src_idx2word[key] in vocab:
                  if len(vectors[vocab[self.src_idx2word[key]]]) != 300:
                      pre_embeddings_list.append(randomly_init_embeddings)
                  else:
                      pre_embeddings_list.append(vectors[vocab[self.src_idx2word[key]]])
              else:
                  pre_embeddings_list.append(randomly_init_embeddings)

         self.source_embeddings.init_from_array(np.array(pre_embeddings_list))


def main(train_src_file, train_tgt_file, dev_src_file, dev_tgt_file, model_file, num_epochs, embeddings_init = None, seed = 0):
    .
    .
    .
    encoder_decoder = nmt_dynet(len(train_set.source_word2idx), len(train_set.target_word2idx), train_set.source_word2idx, train_set.source_idx2word, train_set.target_word2idx, train_set.target_idx2word, 300, 300, 2)
    encoder_decoder.load_src_preembeddings("wiki.zh.vec.trimmed")
    encoder_decoder.load_tgt_preembeddings("wiki.en.vec.trimmed")

```
