import json

split = ['train', 'valid', 'test']
def process(spl):
    with open(f'./data/{spl}.json', 'r') as f:
        data = json.load(f)
    with open(f'./data/{spl}.fasta', 'w') as f:
        for idx, item in enumerate(data):
            f.write(f'>{spl}-{idx:05d}\n{item[0]}\n')



for spl in split:
    process(spl)

# import numpy as np
# p = np.load('./data/valid.npz', allow_pickle=True)
# for i in p:
#     print(i, p[i])
#     break
