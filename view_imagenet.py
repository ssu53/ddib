# %%

import os
import random
from PIL import Image
import re
import matplotlib.pyplot as plt


# %%

path = "/pasteur/u/shiye/datasets/ILSVRC2012_val"


# List all image files in the directory
image_files = [os.path.join(path, f) for f in os.listdir(path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

# Sample 36 images
sampled_files = random.sample(image_files, 36)

# Plot images in a 6x6 grid
fig, axes = plt.subplots(6, 6, figsize=(12, 12))
for ax, img_path in zip(axes.flatten(), sampled_files):
    img = Image.open(img_path)
    ax.imshow(img)
    ax.axis('off')
plt.tight_layout()
plt.show()


# %%


path = "/pasteur2/u/shiye/ddib/experiments/imagenet_339to340"

# Find all translated images
translated_images = [f for f in os.listdir(path) if re.match(r'(\d+_\d+)_translated_\d+\.PNG', f)]

# Get the first max_pairs image pairs
max_pairs = 16
pairs = []
for fname in translated_images:
    base_match = re.match(r'(\d+_\d+)_translated_\d+\.PNG', fname)
    if not base_match:
        continue
    base_name = base_match.group(1)
    original_name = f"{base_name}.PNG"
    translated_path = os.path.join(path, fname)
    original_path = os.path.join(path, original_name)
    if os.path.exists(original_path):
        pairs.append((original_path, translated_path))
    if len(pairs) == max_pairs:
        break

# Arrange 2 pairs per row: 8 rows, 4 columns (orig, trans, orig, trans, ...)
fig, axes = plt.subplots(8, 4, figsize=(12, 24), 
                        gridspec_kw={'wspace': 0.4, 'hspace': 0.2})  # wspace only between pairs

for idx, (orig_path, trans_path) in enumerate(pairs):
    row = idx // 2
    col = (idx % 2) * 2
    # Remove whitespace between orig and translated
    if col == 0:
        axes[row, col + 1].get_shared_x_axes().join(axes[row, col], axes[row, col + 1])
        plt.setp(axes[row, col + 1].spines.values(), linewidth=0)
        plt.setp(axes[row, col].spines.values(), linewidth=0)
    # Original image
    img_orig = Image.open(orig_path)
    axes[row, col].imshow(img_orig)
    axes[row, col].set_title('Original', fontsize=8)
    axes[row, col].axis('off')
    # Translated image
    img_trans = Image.open(trans_path)
    axes[row, col + 1].imshow(img_trans)
    axes[row, col + 1].set_title('Translated', fontsize=8)
    axes[row, col + 1].axis('off')

# Remove horizontal space between orig and translated columns
fig.subplots_adjust(wspace=0, hspace=0.2)
for row in range(8):
    axes[row,1].set_position([
        axes[row,0].get_position().x1, 
        axes[row,1].get_position().y0, 
        axes[row,1].get_position().width, 
        axes[row,1].get_position().height
    ])
    axes[row,3].set_position([
        axes[row,2].get_position().x1 + 0.04,  # keep space between pairs
        axes[row,3].get_position().y0, 
        axes[row,3].get_position().width, 
        axes[row,3].get_position().height
    ])

plt.show()
# %%
