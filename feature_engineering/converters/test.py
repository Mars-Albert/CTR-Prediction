__author__ = 'mars'



import hashlib
target_cat_feats = ['C9-a73ee510', 'C22-', 'C17-e5ba7672', 'C26-', 'C23-32c7478e', 'C6-7e0ccccf', 'C14-b28479f6', 'C19-21ddcdc9', 'C14-07d13a8f', 'C10-3b08e48b', 'C6-fbad5c96', 'C23-3a171ecb', 'C20-b1252a9d', 'C20-5840adea', 'C6-fe6b92e5', 'C20-a458ea53', 'C14-1adce6ef', 'C25-001f3601', 'C22-ad3062eb', 'C17-07c540c4', 'C6-', 'C23-423fab69', 'C17-d4bb7bd8', 'C2-38a947a1', 'C25-e8b83407', 'C9-7cc72ec2']


for j, feat in enumerate(target_cat_feats, start=1):
    print(j,feat)



for feat in ['abc-123','cde-321']:
    field=feat.split('-')[0]
    print(field)


a=[]
a.append((1,3))
a.append((3,1))
print(a)

def hashstr(str, nr_bins):
    return int(hashlib.md5(str.encode('utf8')).hexdigest(), 16)%(nr_bins-1)+1

def gen_hashed_fm_feats(feats, nr_bins=1e+6):
    feats = [(field, hashstr(feat, nr_bins)) for (field, feat) in feats]
    feats.sort()
    print(feats)
    feats = ['{0}'.format(idx) for (field, idx) in feats]
    return feats


feats=[]
feats.append(('a','1234'))
field='b'
feat='124124'
feats.append((field,feat))
field='c'
feat='664124'
feats.append((field,feat))
field='d'
feat='11124'
feats.append((field,feat))
print(feats)

feats=gen_hashed_fm_feats(feats)
print(feats)

