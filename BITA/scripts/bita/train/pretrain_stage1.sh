CUDA_VISIBLE_DEVICES=0,1,2,3 python -m torch.distributed.run --nproc_per_node=4 train.py --cfg-path /BITA/project/bita/train/pretrain_stage1.yaml