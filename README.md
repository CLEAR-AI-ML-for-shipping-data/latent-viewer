# LatentViewer

LatentViewer is a visualisation tool to inspect image embeddings.
It uses principal component analysis to display the embedding vectors as a point
cloud.
Individual points can be selected to display an image, as well as its nine
closest neighbours.

Additionally, there is the possibility to train an SVM classifier through an
active learning method.
This is particularly useful when dealing with embeddings of an unlabeled data set.
