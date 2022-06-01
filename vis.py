import json
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import stats


bonds = [[1.2, 1.8], [3.2, 3.8]]

def vis(split):
    with open(f'./data/{split}.json', 'r') as f:
        data = json.load(f)
    vals = [e[1] for e in data]
    plt.hist(vals, bins=50)
    plt.title(f'Fluorescence distribution of {split} set')
    plt.savefig(f'./imgs/{split}.png')
    print(len(vals))
    # for b in bonds:
    #     print(len([i for i in vals if i >= b[0] and i <= b[1]]) / len(vals))
    
# vis('train')
# vis('valid')
# vis('test')


def spearmanr():
    x = np.arange(0, 1, 0.01)
    y = np.array([np.sqrt(1 - (1 - i)**2) for i in x])
    plt.figure(figsize=(6, 6))

    plt.scatter(x, y)
    spr = stats.spearmanr(x, y)[0]
    pr = stats.pearsonr(x, y)[0]
    print(spr, pr)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Spearman Correlation = 1\nPearson Correlation = 0.916')
    # plt.text(2, 4, '$(x - 1)^2 + y^2 = 1$')
    plt.savefig('./imgs/spearmanr.png', bbox_inches='tight')

spearmanr()