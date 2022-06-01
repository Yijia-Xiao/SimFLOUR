with open('oral.txt', 'r') as f:
	data = f.readlines()

for l in data:
	print(l.replace('嗯', '').replace('呃', '').replace('厄', '').replace('啊', '').replace('，，', '，').replace('。，', '。').replace('，。', '。').replace('。。', '。'))
