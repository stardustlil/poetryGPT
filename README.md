# PoetryGPT

**PoetryGPT** 是一个基于 PyTorch 实现的字符级 Transformer 模型，旨在学习并生成具有古诗词韵律和风格的文本。项目涵盖了从原始数据清洗、字符编码到 Transformer 模型构建与训练的全流程。

## 项目简介

本项目通过对宋词数据集的清洗，构建了一个字符级的语言模型。

* 架构：采用经典的 Decoder-only Transformer 架构，包含多头自注意力机制（Multi-Head Attention）和前馈神经网络（FeedForward）。

* 特性：
    * 支持通过 <START> 标记引导生成。
    * 采用 Top-k 和 Top-p 采样策略，提升生成诗词的自然度。
    * 自带自动终止机制，检测到 <END> 标记时停止生成。
## 环境依赖
建议使用带有 CUDA 支持的 GPU 环境以获得更快的训练速度。
## 数据处理
数据清洗脚本 clean_data.py 将原始的 ci.song.json 转换为训练所需的 input.txt。

## 模型训练
项目包含一个 Jupyter Notebook 文件 poetryGPT.ipynb，详细记录了训练过程。
