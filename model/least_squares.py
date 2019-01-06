import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def display(X, names):
    labels = ["Age", "G", "GS", "MP", "FG", "FGA", "FG%", "3P", "3PA", "3P%", "2P", "2PA", "2P%", "eFG%", "FT", "FTA", "FT%", "ORB", "DRB", "TRB", "AST", "STL", "BLK", "TOV", "PF", "PTS"]
    Xdf = pd.DataFrame(X, index=names, columns=labels)
    print(Xdf)

    r,c = X.shape

    fig, ax = plt.subplots()
    for i in range(0,r):
        ax.plot(labels, X[i,:], label=names[i])
    ax.legend()
    plt.show()

    return


def calc(X,y):

    r,c = X.shape

    # calculate eigenvectors and eignevalues
    [U,S,VH] = np.linalg.svd(X, full_matrices=False)
    V = VH.T

    #print(U)
    #print(np.diag(S))
    #print(V)
    # least squares approximation using eigenvectors and eignevalues
    w_hat = V @ np.linalg.inv(np.diag(S)) @ U.T @ y
    print(w_hat)

    return w_hat