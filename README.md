[中文主页](./README.zh-CN.md)
# Dataflow-Gen

<p align="center">
  <img src="./static/images/DataFlow_gen.png">
</p>
<a href="https://opensource.org/license/apache-2-0" target="_blank">
    <img alt="License: apache-2-0" src="https://img.shields.io/github/license/saltstack/salt" />
</a>
<a href="https://github.com/Open-DataFlow/Dataflow-Gen" target="_blank">
    <img alt="GitHub Stars" src="https://img.shields.io/github/stars/Open-DataFlow/Dataflow-Gen?style=social" />
</a>
<a href="https://github.com/Open-DataFlow/Dataflow-Gen/issues" target="_blank">
    <img alt="Open Issues" src="https://img.shields.io/github/issues-raw/Open-DataFlow/Dataflow-Gen" />
</a>

DataFlow-Eval is a data evaluation system to evaluate data quality from multiple dimensions. We mainly support SOTA algorithms within academic papers with strong theoretical support.

We now support text, image, video and multimodality data types.

## Table of Contents
- [DataFlow-Eval](#dataflow-eval)
  - [Table of Contents](#table-of-contents)
  - [Module and Modality Support](#module-and-modality-support)
  - [🔥 News](#news)
  - [🛠 Installation](#installation)
  - [🚀 Quick Start](#quick-start)
    - [Quick Evaluation](#quick-evaluation)
    - [Quick Process](#quick-process)  
  - [💪 Jupyter Notebook Demo](#jupyter-notebook-demo)
    - [Text](#text)
    - [Image](#image)
    - [Video](#video)
  - [📌 Data Evaluation Documentation](#data-evaluation-documentation)
    - [Text Documentation](#text-documentation)
    - [Image Documentation](#image-documentation)
    - [Video Documentation](#video-documentation)
  - [🧠 Data Evaluation Algorithms](#data-evaluation-algorithms)
    - [Text Algorithms](#text-algorithms)
    - [Image Algorithms](#image-algorithms)
    - [Video Algorithms](#video-algorithms)
  - [👋 Awesome Data Evaluation](#awesome-data-evaluation)

## Module and Modality Support

| Module\Modality     | Text | Image | Video | Image-Text Pair | Video-Text Pair |
| ------------------- | ---- | ----- | ----- | --------------- | --------------- |
| **Data Evaluation** | ✅    | ✅     | ✅     | ✅               | ✅               |

## News
- [2024-10-14] 🎉 We summarize data evaluation papers and codes in [👋 Awesome Data Generation](./Awesome_Data_Generation.md)
- [2024-12-27] 🎉 Our first data-centric evaluation system is now open source.

## Installation


## Quick Start
### Quick Evaluation:
```
cd path/to/DataFlow
python eval.py --config configs/eval/text_scorer_example1.yaml
python eval.py --config configs/eval/image_eval_example.yaml
python eval.py --config configs/eval/video_scorer.yaml
```
### Quick Process:
```
cd path/to/DataFlow
python process.py --config configs/process/text_process_example.yaml
python process.py --config configs/process/image_filter.yaml
python process.py --config configs/process/video_process.yaml
```

## Jupyter Notebook Demo

### Text

- [Text Evaluation Demo](./demos/text_eval/text_eval_example.ipynb)
- [文本评估示例](./demos/text_eval/text_eval_example.zh-CN.ipynb)
- [Text Process Demo](./demos/text_process/text_process_example.ipynb)
- [文本处理示例](./demos/text_process/text_process_example.zh-CN.ipynb)
  
### Image

- [Image Evaluation Demo](./demos/image_eval/image_eval_example.ipynb)
- [图片评估示例](./demos/image_eval/image_eval_example.zh-CN.ipynb)
- [Image Process Demo](./demos/image_process/image_process_example.ipynb)
- [图片处理示例](./demos/image_process/image_process_example.zh-CN.ipynb)
  
### Video

- [Video Evaluation Demo](./demos/video_eval/video_eval_example.ipynb)
- [视频评估示例](./demos/video_eval/video_eval_example.zh-CN.ipynb)
- [Video Process Demo](./demos/video_process/video_process_example.ipynb)
- [视频处理示例](./demos/video_process/video_process_example.zh-CN.ipynb)

## Data Evaluation & Process Documentation

For the usage of evaluation, please refer to the following documents👇

### Text Documentation

- [Text Data Evaluation User Documentation (English)](./dataflow/Eval/Text/README.md)
- [文本数据评估使用文档 (中文)](./dataflow/Eval/Text/README.zh-CN.md)
- [Text Data Evaluation User Documentation (English)](./dataflow/process/text/README.md)
- [文本数据评估使用文档 (中文)](./dataflow/process/text/README.zh-CN.md)

### Image Documentation

- [Image Data Evaluation User Documentation (English)](./dataflow/Eval/image/README.md)
- [图像数据评估使用文档 (中文)](./dataflow/Eval/image/README.zh-CN.md)
- [Image Data Process User Documentation (English)](./dataflow/process/image/README.md)
- [图像数据处理使用文档 (中文)](./dataflow/process/image/README.zh-CN.md)

### Video Documentation

- [Video Data Evaluation User Documentation (English)](./dataflow/Eval/video/README.md)
- [视频数据评估使用文档 (中文)](./dataflow/Eval/video/README.zh-CN.md)
- [Video Data Process User Documentation (English)](./dataflow/process/video/README.md)
- [视频数据处理使用文档 (中文)](./dataflow/process/video/README.zh-CN.md)

## Data Evaluation & Process Algorithms

We summarize the SOTA algorithms from academic papers for data evaluation.
### Text Algorithms

- [Text Evaluation Algorithm Document (English)](./docs/text_metrics.md)
- [文本算法介绍文档 (中文)](./docs/text_metrics.zh-CN.md)
- [Text Evaluation Algorithm Document (English)](./docs/text_process.md)
- [文本算法介绍文档 (中文)](./docs/text_process.zh-CN.md)

### Image Algorithms

- [Image Evaluation Algorithm Document (English)](./docs/image_metrics.md)
- [图像数据评估使用文档 (中文)](./docs/image_metrics.zh-CN.md)
- [Image Evaluation Algorithm Document (English)](./docs/image_process.md)
- [图像数据评估使用文档 (中文)](./docs/image_process.zh-CN.md)

### Video Algorithms

- [Video Evaluation Algorithm Document (English)](./docs/video_metrics.md)
- [视频数据评估使用文档 (中文)](./docs/video_metrics.zh-CN.md)
- [Video Evaluation Algorithm Document (English)](./docs/video_process.md)
- [视频数据评估使用文档 (中文)](./docs/video_process.zh-CN.md)

## Awesome Data Evaluation
- [👋 Awesome Data Evaluation](./Awesome_Data_Evaluation.md)
