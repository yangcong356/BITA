# BITA
This is the official code for "Bootstrapping Interactive Image-Text Alignment for Remote Sensing Image Captioning"

 ## Dependencies
  The project environment in my local is PyTorch 2.0:
  
  `pip install -r requirements.txt`


 ## Dataset
This paper utilizes the [NWPU-Caption, RSICD, and UCM-Caption datasets](https://1drv.ms/f/s!AvupDOrrrLbs7UaAbjbAaM06ywh2?e=tcE6Nn). During the pre-training phase, we exclusively employ the training sets of these three datasets. For the final fine-tuning stage, please uncomment the val and test fields for the three datasets located in the BITA/configs/datasets/ directory.

 ## Weights
The download links for the weights from the two-stage pre-training and the final fine-tuning stage are [available](https://1drv.ms/f/s!AvupDOrrrLbs7T8J5HpD-gHTny6D?e=RhcJxi) here. Within this, the 'Caption' folder contains the model weights with the best validation accuracy on the validation set during the fine-tuning stage.

 ## Pre-training (stage1)
In the first stage of pre-training, the visual encoder used for training is ViT-L/14 from CLIP. Please ensure the value of the 'pretrained' field in the 'BITA/configs/models/bita/bita_pretrain_vitL.yaml' file is set to 'https://storage.googleapis.com/sfr-vision-language-research/LAVIS/models/BLIP2/blip2_pretrained_vitL.pth'. Then, run the following script:
```
bash ./scripts/bita/train/pretrain_stage1.sh
```

 ## Pre-training (stage2)
"In the second stage of pre-training, please replace the value of the 'pretrained' field in the 'BITA/configs/models/bita/bita_pretrain_opt2.7b.yaml' file with the weights from the completion of the first stage of pre-training, located at '/usr/code/BITA/BITA_weights/Stage1/checkpoint_best.pth'. Then, run the following script:"
```
bash ./scripts/bita/train/pretrain_stage2.sh
```

 ## Fine-tune & Evaluation
In the final fine-tuning stage, please replace the value of the 'pretrained' field in the 'BITA/configs/models/bita/bita_caption_opt2.7b.yaml' file with the weights from after the completion of the second stage of pre-training, '/usr/code/BITA/BITA_weights/Stage2/checkpoint_best.pth'. Then, run the following script:
```
bash ./scripts/bita/train/train_caption.sh
```

## Evaluating Only
```
bash ./scripts/bita/eval/eval_caption.sh
```


## Acknowledgments
This implementation is largely based on the code of [LAVIS - A Library for Language-Vision Intelligence](https://github.com/salesforce/LAVIS/tree/main/lavis). Thanks a lot.


## Citation
If you find our work helpful for your research, please consider citing the following BibTeX entry.

```
@article{10415446,
  author={Yang, Cong and Li, Zuchao and Zhang, Lefei},
  journal={IEEE Transactions on Geoscience and Remote Sensing}, 
  title={Bootstrapping Interactive Image–Text Alignment for Remote Sensing Image Captioning}, 
  year={2024},
  volume={62},
  number={},
  pages={1-12},
  doi={10.1109/TGRS.2024.3359316}}

```
