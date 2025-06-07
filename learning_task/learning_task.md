# recbole入门学习任务

本文档将给出一些学习任务，帮助大家入门recbole框架。

## 任务一：早停策略对模型训练的影响

在这个任务中，我们将使用不同的早停策略来训练LightGCN模型，并比较它们的训练时间和性能差异。

### 基本配置

- **模型**：LightGCN
- **数据集**：amazon-books-23

### 详细配置

#### 模型相关设置

```python
'n_layers': 3
```

#### 数据集处理相关设置

```python
'load_col': {'inter': ['user_id', 'item_id']},
'user_inter_num_interval': '[16,inf)',  # 过滤交互次数少于16的用户
'item_inter_num_interval': '[16,inf)',  # 过滤交互次数少于16的物品
```

#### 训练相关设置

```python
'train_batch_size': 8192,
'eval_batch_size': 8192,
'metrics': ['Recall', 'MRR', 'NDCG', 'Hit', 'Precision', 'map', 'averagepopularity'],
'eval_args': {'split': {'RS': [0.8, 0.1, 0.1]}, 'order': 'RO', 'group_by': 'none', 'mode': {'valid': 'full', 'test': 'full'}},
'epochs': 5000,
```

### 早停策略对比

需要对比在以下四组设置下模型的训练时间和性能变化：

1. **设置 A**:

   ```python
   'eval_step': 5,      # 每5个epoch评估一次
   'stopping_step': 10, # 连续10次评估无提升则停止
   ```

2. **设置 B**:

   ```python
   'eval_step': 1,      # 每1个epoch评估一次
   'stopping_step': 10, # 连续10次评估无提升则停止
   ```

3. **设置 C**:

   ```python
   'eval_step': 5,     # 每5个epoch评估一次
   'stopping_step': 5, # 连续5次评估无提升则停止
   ```

4. **设置 D**:

   ```python
   'eval_step': 1,     # 每1个epoch评估一次
   'stopping_step': 5, # 连续5次评估无提升则停止
   ```

### 实验分析

请比较四组实验结果，分析：

1. 评估频率（eval_step）对训练效率和模型性能的影响
2. 早停阈值（stopping_step）对训练效率和模型性能的影响
3. 哪种设置在时间效率和模型性能之间取得了最佳平衡

## 任务二：加载训练好的模型并评估

在这个任务中，我们将加载任务一中训练好的模型权重，并进行评估。

### 评估配置

- **评估指标**：'Recall', 'MRR', 'NDCG', 'Hit', 'Precision', 'map', 'averagepopularity'
- **TopK值**：[10, 20, 50]

### 实验步骤

1. 选择任务一中训练好的一个模型权重文件
2. 在Jupyter Notebook中加载模型并评估
3. 验证评估结果是否与训练日志末尾的指标一致

### 结果验证

比较得到的评估结果与训练日志末尾记录的指标是否一致。如果结果一致，则表明模型加载和评估成功。
