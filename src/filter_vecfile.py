import numpy as np
from utils import Corpus
import codecs
import argparse

def trim_text(target_sentence_dict, filename):
    vocab = {}
    vectors = []
    with codecs.open(filename, "r", "utf-8") as f:
        f.readline()
        with codecs.open(filename + '.trimmed', "w", "utf-8") as fh:
            for line in f:
                fields = line.strip().split(" ")
                if fields[0] in target_sentence_dict:
                    fh.write(line)
                else:
                    pass

    return vocab, vectors


if __name__ == '__main__':

    train_set = Corpus("../data/train.src", "../data/train.tgt")
    print "Printing train_set source sentences: ", train_set.source_sentences[0], len(train_set.source_sentences), train_set.source_idx2word[0], len(train_set.source_idx2word)
    print "Printing train_set target sentences: ", train_set.target_sentences[0], len(train_set.target_sentences), len(train_set.target_idx2word)
    #trim_text(train_set.target_word2idx)

    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = vars(parser.parse_args())

    trim_text(train_set.source_word2idx, **args)
