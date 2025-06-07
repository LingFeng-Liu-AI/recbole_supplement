## 任务一参考代码-use modules
# 主要部分代码说明见recbole官方文档Usage/Use Modules: https://recbole.io/docs/user_guide/usage/use_modules.html

from logging import getLogger
from recbole.config import Config
from recbole.data import create_dataset, data_preparation
from recbole.model.general_recommender import LightGCN
from recbole.trainer import Trainer
from recbole.utils import init_seed, init_logger

import recbole.evaluator.collector
import copy

new_Collector = recbole.evaluator.collector.Collector
import torch

# monkey patch: 修复evaluator的bug: 'Counter' object has no attribute 'cpu'
def get_data_struct_new(self):
    """Get all the evaluation resource that been collected.
    And reset some of outdated resource.
    """
    for key in self.data_struct._data_dict:
        if isinstance(self.data_struct._data_dict[key], torch.Tensor):
            self.data_struct._data_dict[key] = self.data_struct._data_dict[key].cpu()
        else:
            self.data_struct._data_dict[key] = self.data_struct._data_dict[key] 
    returned_struct = copy.deepcopy(self.data_struct)
    for key in ["rec.topk", "rec.meanrank", "rec.score", "rec.items", "data.label"]:
        if key in self.data_struct:
            del self.data_struct[key]
    return returned_struct

new_Collector.get_data_struct = get_data_struct_new

if __name__ == '__main__':
    
    # 超参数配置
    parameter_dict = {
        # data 超参数配置
        'load_col' : {'inter': ['user_id', 'item_id']},
        'user_inter_num_interval' : '[16,inf)',
        'item_inter_num_interval' : '[16,inf)',
        # training 超参数配置
        'train_batch_size' : 8192,
        'eval_batch_size' : 8192,
        'epochs': 5000,
        # evaluation 超参数配置
        'metrics': ['Recall', 'MRR', 'NDCG', 'Hit', 'Precision', 'map', 'averagepopularity'],
        'eval_args' : {'split': {'RS': [0.8, 0.1, 0.1]}, 'order': 'RO', 'group_by': 'none', 'mode': {'valid': 'full', 'test': 'full'}},
        # model 超参数配置
        'n_layers': 3
    }
    
    # 用参数字典完成配置
    config = Config(model='LightGCN', dataset='amazon-books-23', config_dict=parameter_dict)

    # 随机数种子初始化
    init_seed(config['seed'], config['reproducibility'])

    # logger初始化
    init_logger(config)
    logger = getLogger()

    # 将设置写入logger
    logger.info(config)

    # 创建数据集并填充数据
    dataset = create_dataset(config)
    logger.info(dataset)

    # 将数据集分为训练集、验证集和测试集
    train_data, valid_data, test_data = data_preparation(config, dataset)

    # 加载并初始化模型
    model = LightGCN(config, train_data.dataset).to(config['device'])
    logger.info(model)

    # 加载并初始化trainer
    trainer = Trainer(config, model)

    # training
    best_valid_score, best_valid_result = trainer.fit(train_data, valid_data)
    print(best_valid_score)
    print(best_valid_result)

    # test
    test_result = trainer.evaluate(test_data)
    print(test_result)