from weakref import ref
import numpy as np
import json


splits = ['train', 'valid', 'test']

def tape_reader(split):
    data = []
    p = np.load(f'./data/tape/{split}.npz', allow_pickle=True)
    seq_labl = json.load(open(f'./data/{split}.json', 'r'))
    # print(len(p), len(seq_labl))
    # for i in p:
    #     data.append((i))
    #     data.append((i, p[i]))
    for idx in range(len(seq_labl)):
        data.append(
            {
                'seq': seq_labl[idx][0],
                'embed': p[f'{split}-{idx:05d}'],
                'labl': seq_labl[idx][1]
            }
        )

    return data

valid = tape_reader('valid')
# print(valid[0]['embed'].item()['avg'])

anchor = valid[0]
print(anchor['labl'])
exit(0)
# anchor_embed = anchor['embed'].item()['avg']
# print(anchor_embed.size)
# anchor_embed = anchor['embed'].item()['pooled']
# print(anchor_embed.size)

import tqdm
import torch


def predict(train, valid, test, use_valid=False, use_abs=False, embed_type='pooled'):
    assert embed_type in ['pooled', 'avg'], 'should choose pooled/avg'
    # input data: [{'seq', 'embed', 'labl'}]
    anchor = train[0]
    anchor_embed = anchor['embed'].item()[embed_type]
    # print(anchor_embed.size())

    test = test[1:]

    if use_valid:
        refs = train[1:] + valid[1:]
    else:
        refs = train[1:]


    # ref_embed_labl = []
    embed_mat = torch.empty(len(refs), anchor_embed.size)
    embed_val = torch.empty(len(refs))

    for idx in range(len(refs)):
        sample = refs[idx]

        if use_abs:
            # ref_embed_labl.append((sample['embed'].item()[embed_type], sample['labl']))
            embed_mat[idx: idx + 1] = sample['embed'].item()[embed_type]
            embed_val[idx: idx + 1] = sample['labl']
        else:
            # ref_embed_labl.append((sample['embed'].item()[embed_type] - anchor_embed, sample['labl'] - anchor['labl']))
            embed_mat[idx: idx + 1] = sample['embed'].item()[embed_type] - anchor_embed
            embed_val[idx: idx + 1] = sample['labl'] - anchor['labl']
            test = [e - anchor_embed for e in test]

        # print(ref_embed_labl[-1])
        # break
    print(embed_mat[:2], embed_val.shape[:2], embed_val.shape[123:125])
    print(embed_mat.shape, embed_val.shape)

    preds = []
    for sample in tqdm.tqdm(test):
        dot_sim = torch.matmul(embed_mat, )
        for r in ref_embed_labl:
            preds.append()

train = tape_reader('train')
valid = tape_reader('valid')
test = tape_reader('test')

predict(train, valid, test)
