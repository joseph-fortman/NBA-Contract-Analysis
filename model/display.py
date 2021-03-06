import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

training_file = 'data/matrix.csv'
names_file = 'data/names.csv'

def stats(w_hat, y):
    names = pd.read_csv(names_file, names=['Name'])
    df = pd.read_csv(training_file)

    r,c = df.shape

    norm = np.sqrt(np.square(df).sum(axis=0))
    # take the norm
    #norm = pd.DataFrame((df.values / df.values.max(axis=0)))

    fig, ax = plt.subplots()
    for i in range(0,2):
        ax.plot(list(df), df.iloc[i,:], label=names.iloc[i,0])
        #ax.plot(list(norm), norm.iloc[i,:], label=names.iloc[i,0])
    ax.legend()
    plt.show()

    return

# display eigenvectors and values for analysis
def eigens(X):
    # calculate eigenvectors and eignevalues
    [U,S,V] = np.linalg.svd(X, full_matrices=False)
    V = V.T
    # plot and save model Eigenvalues
    fig, ax = plt.subplots()
    index = np.arange(len(S))

    ax.plot(index, S, 'go')
    ax.set(xlabel='index', ylabel='S value', title='Eigenvalues')
    ax.grid()

    fig.savefig("model/test.png")
    plt.show()

    # print dimensions
    print ("U: ")
    print (U.shape)
    print ("S:")
    print (S.shape)
    print ("V: ")
    print (V.shape)
    return

## mixed visuals

# What do GMs pay the most for?
def pay_trends(X):
    a,b = X.shape
    print (X.shape)
    X = np.hstack((X,np.zeros([a,1])))
    # per year pay = salary left / years left
    X[:,32] = X[:,31] / X[:,30]
    # returns indices that would sort the matrix
    indices = np.argsort(X[:,32])
    # sort the matrix
    X = X[indices]
    # delete salary columns
    X = np.delete(X,[27,28,29,30,31,32], 1)
    # take the norm
    X_norm = X / X.max(axis=0)
    # display
    fig, ax = plt.subplots()
    ax.pcolormesh(X_norm)
    plt.show()
