fig, axs = plt.subplots(3)
    (centers1, labels) = find_cluster(x_wm, 3)
    (centers2, labels) = find_cluster(x_my, 3)
    (centers3, labels) = find_cluster(x_wy, 3)
    axs[0].scatter(x_wm[:, 0], x_wm[:, 1], c=y1, s=50, cmap='viridis')
    axs[0].set(xlabel='week', ylabel='month')
    axs[1].scatter(x_my[:, 0], x_my[:, 1], c=y2, s=50, cmap='viridis')
    axs[1].set(xlabel='month', ylabel='year')
    axs[2].scatter(x_wy[:, 0], x_wy[:, 1], c=y3, s=50, cmap='viridis')
    axs[2].set(xlabel='week', ylabel='year')
    axs[0].scatter(centers1[:, 0], centers1[:, 1], c='pink', s=200, alpha=0.9)
    axs[1].scatter(centers2[:, 0], centers2[:, 1], c='pink', s=200, alpha=0.9)
    axs[2].scatter(centers3[:, 0], centers3[:, 1], c='pink', s=200, alpha=0.9)
    plt.show()

    buy=week_and_month.predict([[0.05,0.1]])
    sell=week_and_month.predict([[-0.02,-0.1]])




