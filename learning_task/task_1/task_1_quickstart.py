## 任务一参考代码-quick start
# 主要部分代码说明见recbole官方文档Usage/Use run_recbole: https://recbole.io/docs/user_guide/usage/run_recbole.html
from recbole.quick_start import run_recbole
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
run_recbole(model='LightGCN', dataset='amazon-books-23', config_dict=parameter_dict)