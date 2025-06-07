# 任务一 说明

## RecBole及其依赖库的安装与使用

RecBole是一个功能强大的推荐系统相关python库，内含大量推荐系统模型和一些经典的数据集，以及各种训练所需模块的配置。

安装RecBole库的具体方法见官方文档 Install RecBole：https://recbole.io/docs/get_started/install.html

**注意**：RecBole中部分代码只适配**较低版本**的numpy、torch、scipy库，使用过高/过低版本均有可能报错（详情见bugs_fix）。有关依赖库版本的详细信息请见Github repositories中的environment.yml文件，推荐使用conda一键导入库信息并创建环境。

## 代码内容说明

RecBole功能的详细使用说明见官方文档 Usage：https://recbole.io/docs/user_guide/usage.html

### 如何运行并训练模型

本任务示例代码给出两种方式：使用Quick Start中的run_recbole一键运行和使用不同模块运行。

task_1_quickstart.py 使用 run_recbole 一键加载模型和数据集、完成设置、训练和评估模型，详情见官方文档 https://recbole.io/docs/user_guide/usage/run_recbole.html。对于已经完善的模型测试任务，推荐使用这一方法。

task_1_module.py 使用 Config, Trainer 等模块按步骤进行模型设置、数据集加载、训练模型、评估模型，详情见官方文档 https://recbole.io/docs/user_guide/usage/use_modules.html。对于需要增加新的操作或进行修改的模型，推荐使用这一方法。

本任务中使用的模型 LightGCN 详情见官方文档 https://recbole.io/docs/user_guide/model/general/lightgcn.html，在学习阶段曾研读过该论文，请阅读并了解该模型。

### 如何设置超参数

设置参数的具体操作见官方文档 https://recbole.io/docs/user_guide/config/parameters_configuration.html

共有三种参数设置方法：导入设置文件、在代码中定义参数字典、使用命令行输入。其优先级为：命令行>参数字典>导入设置文件>默认设置。一般用于多个模型的参数使用文件导入设置，用于单个模型且在测试中保持不变的参数使用参数字典设置，用于单个模型且需要修改对比的参数使用命令行设置。

本任务中需要对比eval_step, stopping_step两个超参数设置带来的影响，故这两个参数选择命令行输入，其它参数选择参数字典。

命令行中具体的输入格式示例为：

```cmd
python task_1_module.py --eval_step=5 --stopping_step=10
```

**请使用命令行运行程序！**

## 实验结果说明

代码运行日志存放在log文件夹中，记录了模型配置、训练过程命令行输出等。

训练结果存放在saved文件夹中，可以读取训练结果文件用于评估（见任务二）。