CUDA_VISIBLE_DEVICES=1 task=train bash e2.sh
CUDA_VISIBLE_DEVICES=2 task=valid bash e2.sh
CUDA_VISIBLE_DEVICES=2 task=test bash e2.sh
