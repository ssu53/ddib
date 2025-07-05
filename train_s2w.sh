MODEL_FLAGS="--in_channels 3 --num_channels 256 --out_channels 3 --num_res_blocks 4 --attention_resolutions 2 --dropout 0.3 --channel_mult 2,2 --conv_resample False --dims 2 --num_classes None --use_checkpoint False --num_heads 1 --num_head_channels -1 --num_heads_upsample -1 --use_scale_shift_norm True --resblock_updown False --use_new_attention_order True --with_fourier_features False --class_cond False --image_size 64"
DIFFUSION_FLAGS="--diffusion_steps 1000 --noise_schedule linear"
TRAIN_FLAGS="--lr 1e-4 --batch_size 32"
python scripts/image_train.py --data_dir /pasteur/u/shiye/datasets/summer2winter_yosemite/trainA $MODEL_FLAGS $DIFFUSION_FLAGS $TRAIN_FLAGS


# currently centre crops to size 64. need to update to 256 and apply vae!