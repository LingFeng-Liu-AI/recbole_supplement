# 任务清单

## 总体目标概述

本项目的任务主要是使用recbole实现一系列debias recommendation（去偏推荐）、geneneral recommendation（一般推荐任务，即协同过滤） 算法，其中大部分工作recbole自己已经完成（不过可能存在bug）、或者原论文已经提供实现代码（需要基于recbole重新实现）。

## 任务介绍

（完成后请更新任务前的to do方框，打勾✅）

### 一、debias recommendation baseline

该部分已在recbole2.0（[https://recbole.io/cn/subpackage.html](https://recbole.io/cn/subpackage.html)）的子项目 RecBole-Debias（[https://github.com/JingsenZhang/RecBole-Debias](https://github.com/JingsenZhang/RecBole-Debias)） 中完成了很多baseline。
但是其代码有bug，不能直接跑通。

1\.

1. [ ] 跑通RecBole-Debias(可能需要对其中的bug进行修改)
    尤其是以下五个模型（本身已经实现，可能需要调整采样策略等，另外这些方法的backbone都是mf，我们需要添加使用LightGCN实现）

    **Selection Bias**:
    - [ ] **[MF-IPS](recbole_debias/model/debiased_recommender/mf_ips.py)** from Schnabel *et al.*: [Recommendations as Treatments: Debiasing Learning and Evaluation](http://proceedings.mlr.press/v48/schnabel16.pdf) (ICML 2016).

    **Popularity Bias**:
    - [ ] **[PDA](recbole_debias/model/debiased_recommender/pda.py)** from Zhang *et al.*: [Causal intervention for leveraging popularity bias in recommendation](https://arxiv.org/pdf/2105.06067.pdf) (SIGIR 2021).
    - [ ] **[MACR](recbole_debias/model/debiased_recommender/macr.py)** from Wei *et al.*: [Model-Agnostic Counterfactual Reasoning for Eliminating Popularity Bias in Recommender System](https://arxiv.org/pdf/2010.15363.pdf) (KDD 2021).
    - [ ] **[DICE](recbole_debias/model/debiased_recommender/dice.py)** from Zheng *et al.*: [Disentangling User Interest and Conformity for Recommendation with Causal Embedding](https://arxiv.org/pdf/2006.11011.pdf?ref=https://githubhelp.com) (WWW 2021).
    - [ ] **[CausE](recbole_debias/model/debiased_recommender/cause.py)** from Bonner *et al.*: [Causal Embeddings for Recommendation](https://arxiv.org/pdf/1706.07639.pdf?ref=https://githubhelp.com) (RecSys 2018).
  
2\.

1. [ ] 基于recbole1.2.1完成以下工作的复现
    backbone选择MF和LightGCN
    - [ ] （1）PC Popularity-opportunity bias in collaborative filtering.（[https://dl.acm.org/doi/10.1145/3437963.3441820](https://dl.acm.org/doi/10.1145/3437963.3441820)）(MF、LightGCN)
        Reg Popularity-opportunity bias in collaborative filtering.（[https://dl.acm.org/doi/10.1145/3437963.3441820](https://dl.acm.org/doi/10.1145/3437963.3441820)）(MF、LightGCN)(同一篇论文中的两种方法)
    - [ ] （2）LightGCN-IPS
    - [ ] （3）LightGCN-PDA
    - [ ] （4）LightGCN-MACR
    - [ ] （5）LightGCN-DICE
    - [ ] （6）LightGCN-CausE
    - [ ] （7）Adjnorm Investigating Accuracy-Novelty Performance for Graph-based Collaborative Filtering ([https://dl.acm.org/doi/10.1145/3477495.3532005](https://dl.acm.org/doi/10.1145/3477495.3532005))(MF、LightGCN)
    - [ ] （8）SAM-REG Connecting User and Item Perspectives in Popularity Debiasing for Collaborative Recommendation（[https://arxiv.org/pdf/2006.04275](https://arxiv.org/pdf/2006.04275)）(MF、LightGCN)
    - [ ] （9）xQuad Managing Popularity Bias in Recommender Systems with Personalized Re-ranking（[https://arxiv.org/abs/1901.07555](https://arxiv.org/abs/1901.07555)）(MF、LightGCN)
    - [ ] （10）APDA Adaptive Popularity Debiasing Aggregator for Graph Collaborative Filtering（[https://dl.acm.org/doi/10.1145/3539618.3591635](https://dl.acm.org/doi/10.1145/3539618.3591635)）（only LightGCN）
    - [ ] （11）PopGo Robust Collaborative Filtering to Popularity Distribution Shift([https://dl.acm.org/doi/10.1145/3627159](https://dl.acm.org/doi/10.1145/3627159)) (MF、LightGCN)
    - [ ] （12）CD2AN Co-training Disentangled Domain Adaptation Network for Leveraging Popularity Bias in Recommenders（[https://dl.acm.org/doi/pdf/10.1145/3477495.3531952](https://dl.acm.org/doi/pdf/10.1145/3477495.3531952)）
    - [ ] （13）DCRS Disentangled Representation for Diversified Recommendations([https://dl.acm.org/doi/10.1145/3539597.3570389](https://dl.acm.org/doi/10.1145/3539597.3570389))

### 二、geneneral recommendation

主要是基于recbole1.2.1实现一些今年来最新的推荐算法，其中部分基于GNN的算法在recbole2.0（[https://recbole.io/cn/subpackage.html](https://recbole.io/cn/subpackage.html)）的子项目 RecBole-GNN（[https://github.com/RUCAIBox/RecBole-GNN](https://github.com/RUCAIBox/RecBole-GNN)）已经经过针对GNN计算优化完成，我们需要迁移回recbole1.2.1中(为了公平比较不同baseline)。

**tip：** 重点验证University of Hong Kong的paper，网络上关于他们的工作（关于图对比学习、推荐系统）有很多质疑（这是一个可以发表文章的点）。

1\.

1. [ ] 迁移工作

    - [ ] **[DirectAU](recbole_gnn/model/general_recommender/directau.py)** from Wang *et al.*: [Towards Representation Alignment and Uniformity in Collaborative Filtering](https://arxiv.org/abs/2206.12811) (KDD 2022).
    - [ ] **[SimGCL](recbole_gnn/model/general_recommender/simgcl.py)** from Yu *et al.*: [Are Graph Augmentations Necessary? Simple Graph Contrastive Learning for Recommendation](https://arxiv.org/abs/2112.08679) (SIGIR 2022).
    - [ ] **[XSimGCL](recbole_gnn/model/general_recommender/xsimgcl.py)** from Yu *et al.*: [XSimGCL: Towards Extremely Simple Graph Contrastive Learning for Recommendation](https://arxiv.org/abs/2209.02544) (TKDE 2023).
    - [ ] **[LightGCL](recbole_gnn/model/general_recommender/lightgcl.py)** from Cai *et al.*: [LightGCL: Simple Yet Effective Graph Contrastive Learning for Recommendation](https://arxiv.org/abs/2301.03633)
    - [ ] **[HMLET](recbole_gnn/model/general_recommender/hmlet.py)** from Kong *et al.*: [Linear, or Non-Linear, That is the Question!](https://arxiv.org/abs/2111.07265) (WSDM 2022).
    - [ ] **[SSL4Rec](recbole_gnn/model/general_recommender/ssl4rec.py)** from Yao *et al.*: [Self-supervised Learning for Large-scale Item Recommendations](https://arxiv.org/abs/2007.12865) (CIKM 2021).

2\.

1. [ ] 最新baseline
    - [ ] （1）HGCN HGCH: A Hyperbolic Graph Convolution Network Model for Heterogeneous Collaborative Graph Recommendation([http://arxiv.org/abs/2304.02961](http://arxiv.org/abs/2304.02961))
    - [ ] （2）HCCF Hypergraph Contrastive Collaborative Filtering([https://dl.acm.org/doi/10.1145/3477495.3532058](https://dl.acm.org/doi/10.1145/3477495.3532058))
    - [ ] （3）UltraGCN UltraGCN: Ultra Simplification of Graph Convolutional Networks for Recommendation([https://dl.acm.org/doi/10.1145/3459637.3482291](https://dl.acm.org/doi/10.1145/3459637.3482291))
    - [ ] （4）LightCCF Unveiling Contrastive Learning's Capability of Neighborhood Aggregation for Collaborative Filtering([http://arxiv.org/abs/2504.10113](http://arxiv.org/abs/2504.10113))

## 进度安排

- （1）现在到期末考试结束前（大概6月28日）：一、1. 2.（1）（2）（3）（4）（5）（6）
    注：大部分RecBole-Debias都已经实现，需要迁移到LightGCN模型上
    最低要求：跑通RecBole-Debias
- （2）期末考试结束到7月20日：一、2.（7）（8）（9）（10）（11）（12）（13）
- （3）7月20日之后：二、1. 2.（1）（2）（3）（4）

## 代码检查方法

实现一个模型之后，在一个数据集上进行训练，训练结束之后通过权重文件加载模型在测试集再进行一次测试。
如果 训练正常不报错 and 加载模型的测试结果和训练时的结果相同 则视为复现成功。
其次，测试结果相对于公认Baseline（如LightGCN）的效果改变与原论文差不多即可（如果相差较大可能是因为实现的有问题或者原论文报告有偏差，如果属于后者，这会是产生新的idea的地方）。
