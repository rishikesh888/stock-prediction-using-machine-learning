def find_cluster(x, n_clusters, reseed=2):
    rng = np.random.RandomState(reseed)
    i = rng.permutation(x.shape[0])[:n_clusters]
    centers = x[i]
    while True:
      labels = pairwise_distances_argmin(x, centers)
      new_centers = np.array([x[labels == i].mean(0) for i in range(n_clusters)])
      if (np.all(centers == new_centers)):
          break
      centers = new_centers
    return (centers, labels)