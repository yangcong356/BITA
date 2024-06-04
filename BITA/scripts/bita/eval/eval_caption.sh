CUDA_VISIBLE_DEVICES=0,1,2,3 python -m torch.distributed.run --nproc_per_node=4 evaluate.py --cfg-path /BITA/project/bita/eval/caption_eval.yaml
