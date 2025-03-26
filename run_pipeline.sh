#!/bin/bash

# 设置变量
source /opt/conda/bin/activate
conda activate dataflow-gen
which python
yaml_file_path="$1"
json_file_path="$2"
key="$3"
save_path="$4"
mid_path="$5"

# 执行 Python 脚本
python DataFlow-Gen/run_pipeline.py \
  --config "$yaml_file_path" \
  --meta_path "$json_file_path" \
  --text_key "$key" \
  --save_folder "$save_path" \
  --base_folder "$mid_path"