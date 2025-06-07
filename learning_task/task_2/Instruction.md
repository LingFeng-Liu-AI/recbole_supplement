# 任务二 说明

## 代码内容说明

代码的评估任务可由Trainer.evaluate实现。可从任务一得到的saved文件夹中选择一个文件，用 load_data_and_model 读取设置、数据集、模型参数（见官方文档 https://recbole.io/docs/recbole/recbole.quick_start.quick_start.html#recbole.quick_start.quick_start.load_data_and_model），再对 config 进行评估所需的修改。

使用 Jupyter Notebook 运行评估程序，这是因为 Jupyter 变量可以暂存，不需要重复加载模型。

task_2_without_patch.ipynb 中由 Trainer.evaluate 直接实现了评估。由于该函数在处理 'averagepopularity' 指标时存在bug（详情见bugs_fix/learning_task_2/Averagepopularity），需要使用 monkey patch 进行修复，task_2_with_patch.ipynb 中将 Trainer.evaluate 替换为 monkey patch 以实现对包括'averagepopularity' 指标的评估。

## 实验结果说明

代码与运行结果均保存在.ipynb文件中。由于 task_2_with_patch 的输出结果过长，将其训练过程省略的结果放在output.txt中。