import random
import matplotlib.pyplot as plt
import numpy as np
if __name__ == '__main__':
    color = {"R": np.zeros((28,28,3)), "G": np.zeros((28,28,3)),"B": np.zeros((28,28,3))}
    color["R"][:,:,0] = 1
    color["G"][:,:,1] = 1
    color["B"][:,:,2] = 1
    A = ["RGB","RBG","GBR","GRB", "BRG", "BGR"]
    random.shuffle(A)

    for k,i in enumerate(A, start = 1):
        for j in range(1,4):
            plt.subplot(1,3,j)
            plt.imshow(color[i[j-1]])
            plt.axis("off")
        plt.tight_layout()
        plt.gcf().set_size_inches(16,8)
        plt.suptitle(k)
        plt.show()
        plt.clf()
