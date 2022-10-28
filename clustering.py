import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import pandas as pd
from sklearn.decomposition import PCA
#from Jvis import JTSNEBASE, JTSNE
from sklearn.cluster import KMeans

expr_mat = pd.read_csv("./GSE126074_CellLineMixture_SNAREseq_cDNA_counts.tsv", sep="\t")

scale_factor= 1000
print(expr_mat)
expr_mat = expr_mat.values