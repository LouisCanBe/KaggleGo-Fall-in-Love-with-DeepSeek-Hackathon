# 定义kaggle public api 工具
from camel.toolkits import FunctionTool
import subprocess

kaggleApiTools = []

def list_kaggle_competitions() -> str:
    """列出当前活动的Kaggle比赛。
    
    Args:
        None

    Returns:
        str: 比赛列表的输出。
    
    工具名称: list_competitions_tool
    命令: kaggle competitions list
    """
    result = subprocess.run(['kaggle', 'competitions', 'list'], capture_output=True, text=True)
    return result.stdout

# 将新工具函数包装为工具
list_competitions_tool = FunctionTool(list_kaggle_competitions)
kaggleApiTools.append(list_competitions_tool)

def download_kaggle_competition(competition: str) -> str:
    """下载与指定比赛相关的文件。

    Args:
        competition (str): 比赛名称。例如，https://www.kaggle.com/competitions/titanic比赛的名称为'titanic'。

    Returns:
        str: 下载结果的输出。

    工具名称: download_competition_tool
    命令: kaggle competitions download -c <competition>
    """
    result = subprocess.run(['kaggle', 'competitions', 'download', '-c', competition], capture_output=True, text=True)
    return result.stdout

# 将新工具函数包装为工具
download_competition_tool = FunctionTool(download_kaggle_competition)
kaggleApiTools.append(download_competition_tool)

def submit_kaggle_competition(competition: str, file_path: str, message: str) -> str:
    """提交到指定的Kaggle比赛。

    Args:
        competition (str): 比赛名称。例如，https://www.kaggle.com/competitions/titanic比赛的名称为'titanic'。
        file_path (str): 提交的文件路径。
        message (str): 提交消息。

    Returns:
        str: 提交结果的输出。

    工具名称: submit_competition_tool
    命令: kaggle competitions submit -c <competition> -f <file_path> -m <message>
    """
    result = subprocess.run(['kaggle', 'competitions', 'submit', '-c', competition, '-f', file_path, '-m', message], capture_output=True, text=True)
    return result.stdout

# 将新工具函数包装为工具
submit_competition_tool = FunctionTool(submit_kaggle_competition)
kaggleApiTools.append(submit_competition_tool)

def list_kaggle_datasets(keyword: str) -> str:
    """列出与搜索关键词匹配的数据集。

    Args:
        keyword (str): 搜索关键词。

    Returns:
        str: 数据集列表的输出。

    工具名称: list_datasets_tool
    命令: kaggle datasets list -s <keyword>
    """
    result = subprocess.run(['kaggle', 'datasets', 'list', '-s', keyword], capture_output=True, text=True)
    return result.stdout

# 将新工具函数包装为工具
list_datasets_tool = FunctionTool(list_kaggle_datasets)
kaggleApiTools.append(list_datasets_tool)

def download_kaggle_dataset(dataset: str) -> str:
    """下载与指定数据集相关的文件。

    Args:
        dataset (str): 数据集名称。

    Returns:
        str: 下载结果的输出。

    工具名称: download_dataset_tool
    命令: kaggle datasets download -d <dataset>
    """
    result = subprocess.run(['kaggle', 'datasets', 'download', '-d', dataset], capture_output=True, text=True)
    return result.stdout

# 将新工具函数包装为工具
download_dataset_tool = FunctionTool(download_kaggle_dataset)
kaggleApiTools.append(download_dataset_tool)

def create_kaggle_dataset(path: str) -> str:
    """创建新的Kaggle数据集。

    Args:
        path (str): 数据集文件夹路径。

    Returns:
        str: 创建结果的输出。

    工具名称: create_dataset_tool
    命令: kaggle datasets create -p <path>
    """
    result = subprocess.run(['kaggle', 'datasets', 'create', '-p', path], capture_output=True, text=True)
    return result.stdout

# 将新工具函数包装为工具
create_dataset_tool = FunctionTool(create_kaggle_dataset)
kaggleApiTools.append(create_dataset_tool)

def version_kaggle_dataset(path: str, message: str) -> str:
    """创建现有数据集的新版本。

    Args:
        path (str): 数据集文件夹路径。
        message (str): 版本消息。

    Returns:
        str: 创建版本结果的输出。

    工具名称: version_dataset_tool
    命令: kaggle datasets version -p <path> -m <message>
    """
    result = subprocess.run(['kaggle', 'datasets', 'version', '-p', path, '-m', message], capture_output=True, text=True)
    return result.stdout

# 将新工具函数包装为工具
version_dataset_tool = FunctionTool(version_kaggle_dataset)
kaggleApiTools.append(version_dataset_tool)

def list_kaggle_kernels(keyword: str) -> str:
    """列出与搜索关键词匹配的笔记本。

    Args:
        keyword (str): 搜索关键词。

    Returns:
        str: 笔记本列表的输出。

    工具名称: list_kernels_tool
    命令: kaggle kernels list -s <keyword>
    """
    result = subprocess.run(['kaggle', 'kernels', 'list', '-s', keyword], capture_output=True, text=True)
    return result.stdout

# 将新工具函数包装为工具
list_kernels_tool = FunctionTool(list_kaggle_kernels)
kaggleApiTools.append(list_kernels_tool)

def push_kaggle_kernel(path: str) -> str:
    """推送笔记本到Kaggle。

    Args:
        path (str): 笔记本文件夹路径。

    Returns:
        str: 推送结果的输出。

    工具名称: push_kernel_tool
    命令: kaggle kernels push -p <path>
    """
    result = subprocess.run(['kaggle', 'kernels', 'push', '-p', path], capture_output=True, text=True)
    return result.stdout

# 将新工具函数包装为工具
push_kernel_tool = FunctionTool(push_kaggle_kernel)
kaggleApiTools.append(push_kernel_tool)

def pull_kaggle_kernel(kernel: str, path: str) -> str:
    """拉取指定的Kaggle笔记本。

    Args:
        kernel (str): 笔记本名称。
        path (str): 下载路径。

    Returns:
        str: 拉取结果的输出。

    工具名称: pull_kernel_tool
    命令: kaggle kernels pull <kernel> -p <path> -m
    """
    result = subprocess.run(['kaggle', 'kernels', 'pull', kernel, '-p', path, '-m'], capture_output=True, text=True)
    return result.stdout

# 将新工具函数包装为工具
pull_kernel_tool = FunctionTool(pull_kaggle_kernel)
kaggleApiTools.append(pull_kernel_tool)

# 定义函数以列出比赛文件
def list_kaggle_competition_files(competition: str = None) -> str:
    """列出比赛文件。

    Args:
        competition (str): 比赛名称。例如，https://www.kaggle.com/competitions/titanic比赛的名称为'titanic'。

    Returns:
        str: 比赛文件列表的输出。

    工具名称: list_competition_files_tool
    命令: kaggle competitions files [<competition>]
    """
    command = ['kaggle', 'competitions', 'files']
    if competition:
        command.append(competition)
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

# 将新工具函数包装为工具
list_competition_files_tool = FunctionTool(list_kaggle_competition_files)
kaggleApiTools.append(list_competition_files_tool)

# 定义函数以获取比赛排行榜
def get_kaggle_leaderboard(competition: str, show: bool = False, download: bool = False) -> str:
    """获取比赛排行榜。

    Args:
        competition (str): 比赛名称。例如，https://www.kaggle.com/competitions/titanic比赛的名称为'titanic'。
        show (bool): 是否显示排行榜。
        download (bool): 是否下载排行榜。

    Returns:
        str: 排行榜信息的输出。

    工具名称: get_leaderboard_tool
    命令: kaggle competitions leaderboard [<competition>] [--show] [--download]
    """
    command = ['kaggle', 'competitions', 'leaderboard']
    if competition:
        command.append(competition)
    if show:
        command.append('--show')
    if download:
        command.append('--download')
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

# 将新工具函数包装为工具
get_leaderboard_tool = FunctionTool(get_kaggle_leaderboard)
kaggleApiTools.append(get_leaderboard_tool)

# 定义函数以列出比赛提交
def list_kaggle_submissions(competition: str = None) -> str:
    """列出比赛提交。

    Args:
        competition (str): 比赛名称。例如，https://www.kaggle.com/competitions/titanic比赛的名称为'titanic'。

    Returns:
        str: 提交列表的输出。

    工具名称: list_submissions_tool
    命令: kaggle competitions submissions [<competition>]
    """
    command = ['kaggle', 'competitions', 'submissions']
    if competition:
        command.append(competition)
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

# 将新工具函数包装为工具
list_submissions_tool = FunctionTool(list_kaggle_submissions)
kaggleApiTools.append(list_submissions_tool)

# 定义函数以获取数据集的元数据
def get_kaggle_dataset_metadata(dataset: str) -> str:
    """下载数据集的元数据。

    Args:
        dataset (str): 数据集名称。

    Returns:
        str: 数据集元数据的输出。

    工具名称: get_dataset_metadata_tool
    命令: kaggle datasets metadata <dataset>
    """
    command = ['kaggle', 'datasets', 'metadata', dataset]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

# 将新工具函数包装为工具
get_dataset_metadata_tool = FunctionTool(get_kaggle_dataset_metadata)
kaggleApiTools.append(get_dataset_metadata_tool)

# 定义函数以获取数据集的创建状态
def get_kaggle_dataset_status(dataset: str) -> str:
    """获取数据集的创建状态。

    Args:
        dataset (str): 数据集名称。

    Returns:
        str: 数据集状态的输出。

    工具名称: get_dataset_status_tool
    命令: kaggle datasets status <dataset>
    """
    command = ['kaggle', 'datasets', 'status', dataset]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

# 将新工具函数包装为工具
get_dataset_status_tool = FunctionTool(get_kaggle_dataset_status)
kaggleApiTools.append(get_dataset_status_tool)

# 定义函数以初始化内核的元数据文件
def init_kaggle_kernel_metadata(path: str) -> str:
    """初始化内核的元数据文件。

    Args:
        path (str): 文件夹路径。

    Returns:
        str: 初始化结果的输出。

    工具名称: init_kernel_metadata_tool
    命令: kaggle kernels init -p <path>
    """
    command = ['kaggle', 'kernels', 'init', '-p', path]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

# 将新工具函数包装为工具
init_kernel_metadata_tool = FunctionTool(init_kaggle_kernel_metadata)
kaggleApiTools.append(init_kernel_metadata_tool)

# 定义函数以获取模型
def get_kaggle_model(model: str, path: str = None) -> str:
    """获取模型。

    Args:
        model (str): 模型名称。
        path (str): 下载路径。

    Returns:
        str: 模型信息的输出。

    工具名称: get_model_tool
    命令: kaggle models get <model> [-p <path>]
    """
    command = ['kaggle', 'models', 'get', model]
    if path:
        command.extend(['-p', path])
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

# 将新工具函数包装为工具
get_model_tool = FunctionTool(get_kaggle_model)
kaggleApiTools.append(get_model_tool)

# 定义函数以列出模型
def list_kaggle_models(search: str = None) -> str:
    """列出模型。

    Args:
        search (str): 搜索关键词。

    Returns:
        str: 模型列表的输出。

    工具名称: list_models_tool
    命令: kaggle models list [-s <search>]
    """
    command = ['kaggle', 'models', 'list']
    if search:
        command.extend(['-s', search])
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

# 将新工具函数包装为工具
list_models_tool = FunctionTool(list_kaggle_models)
kaggleApiTools.append(list_models_tool)

# 定义函数以初始化模型的元数据文件
def init_kaggle_model_metadata(path: str) -> str:
    """初始化模型的元数据文件。

    Args:
        path (str): 文件夹路径。

    Returns:
        str: 初始化结果的输出。

    工具名称: init_model_metadata_tool
    命令: kaggle models init -p <path>
    """
    command = ['kaggle', 'models', 'init', '-p', path]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

# 将新工具函数包装为工具
init_model_metadata_tool = FunctionTool(init_kaggle_model_metadata)
kaggleApiTools.append(init_model_metadata_tool)

# 定义函数以创建新模型
def create_kaggle_model(path: str) -> str:
    """创建新模型。

    Args:
        path (str): 文件夹路径。

    Returns:
        str: 创建结果的输出。

    工具名称: create_model_tool
    命令: kaggle models create -p <path>
    """
    command = ['kaggle', 'models', 'create', '-p', path]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

# 将新工具函数包装为工具
create_model_tool = FunctionTool(create_kaggle_model)
kaggleApiTools.append(create_model_tool)

# 定义函数以删除模型
def delete_kaggle_model(model: str) -> str:
    """删除模型。

    Args:
        model (str): 模型名称。

    Returns:
        str: 删除结果的输出。

    工具名称: delete_model_tool
    命令: kaggle models delete <model>
    """
    command = ['kaggle', 'models', 'delete', model]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

# 将新工具函数包装为工具
delete_model_tool = FunctionTool(delete_kaggle_model)
kaggleApiTools.append(delete_model_tool)

# 定义函数以更新模型
def update_kaggle_model(path: str) -> str:
    """更新模型。

    Args:
        path (str): 文件夹路径。

    Returns:
        str: 更新结果的输出。

    工具名称: update_model_tool
    命令: kaggle models update -p <path>
    """
    command = ['kaggle', 'models', 'update', '-p', path]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

# 将新工具函数包装为工具
update_model_tool = FunctionTool(update_kaggle_model)
kaggleApiTools.append(update_model_tool)

# 定义函数以获取模型实例
def get_kaggle_model_instance(model_instance: str, path: str = None) -> str:
    """获取模型实例。

    Args:
        model_instance (str): 模型实例名称。
        path (str): 下载路径。

    Returns:
        str: 模型实例信息的输出。

    工具名称: get_model_instance_tool
    命令: kaggle models instances get <model_instance> [-p <path>]
    """
    command = ['kaggle', 'models', 'instances', 'get', model_instance]
    if path:
        command.extend(['-p', path])
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

# 将新工具函数包装为工具
get_model_instance_tool = FunctionTool(get_kaggle_model_instance)
kaggleApiTools.append(get_model_instance_tool)

# 定义函数以初始化模型实例的元数据文件
def init_kaggle_model_instance_metadata(path: str) -> str:
    """初始化模型实例的元数据文件。

    Args:
        path (str): 文件夹路径。

    Returns:
        str: 初始化结果的输出。

    工具名称: init_model_instance_metadata_tool
    命令: kaggle models instances init -p <path>
    """
    command = ['kaggle', 'models', 'instances', 'init', '-p', path]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

# 将新工具函数包装为工具
init_model_instance_metadata_tool = FunctionTool(init_kaggle_model_instance_metadata)
kaggleApiTools.append(init_model_instance_metadata_tool)

# 定义函数以创建新的模型实例
def create_kaggle_model_instance(path: str) -> str:
    """创建新的模型实例。

    Args:
        path (str): 文件夹路径。

    Returns:
        str: 创建结果的输出。

    工具名称: create_model_instance_tool
    命令: kaggle models instances create -p <path>
    """
    command = ['kaggle', 'models', 'instances', 'create', '-p', path]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

# 将新工具函数包装为工具
create_model_instance_tool = FunctionTool(create_kaggle_model_instance)
kaggleApiTools.append(create_model_instance_tool)

# 定义函数以删除模型实例
def delete_kaggle_model_instance(model_instance: str) -> str:
    """删除模型实例。

    Args:
        model_instance (str): 模型实例名称。

    Returns:
        str: 删除结果的输出。

    工具名称: delete_model_instance_tool
    命令: kaggle models instances delete <model_instance>
    """
    command = ['kaggle', 'models', 'instances', 'delete', model_instance]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

# 将新工具函数包装为工具
delete_model_instance_tool = FunctionTool(delete_kaggle_model_instance)
kaggleApiTools.append(delete_model_instance_tool)

# 定义函数以更新模型实例
def update_kaggle_model_instance(path: str) -> str:
    """更新模型实例。

    Args:
        path (str): 文件夹路径。

    Returns:
        str: 更新结果的输出。

    工具名称: update_model_instance_tool
    命令: kaggle models instances update -p <path>
    """
    command = ['kaggle', 'models', 'instances', 'update', '-p', path]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

# 将新工具函数包装为工具
update_model_instance_tool = FunctionTool(update_kaggle_model_instance)
kaggleApiTools.append(update_model_instance_tool)

# 定义函数以创建新的模型实例版本
def create_kaggle_model_instance_version(model_instance: str, path: str, notes: str) -> str:
    """创建新的模型实例版本。

    Args:
        model_instance (str): 模型实例名称。
        path (str): 文件夹路径。
        notes (str): 版本说明。

    Returns:
        str: 创建结果的输出。

    工具名称: create_model_instance_version_tool
    命令: kaggle models instances versions create <model_instance> -p <path> -n <notes>
    """
    command = ['kaggle', 'models', 'instances', 'versions', 'create', model_instance, '-p', path, '-n', notes]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

# 将新工具函数包装为工具
create_model_instance_version_tool = FunctionTool(create_kaggle_model_instance_version)
kaggleApiTools.append(create_model_instance_version_tool)

# 定义函数以下载模型实例版本
def download_kaggle_model_instance_version(model_instance_version: str, path: str) -> str:
    """下载模型实例版本。

    Args:
        model_instance_version (str): 模型实例版本名称。
        path (str): 下载路径。

    Returns:
        str: 下载结果的输出。

    工具名称: download_model_instance_version_tool
    命令: kaggle models instances versions download <model_instance_version> -p <path>
    """
    command = ['kaggle', 'models', 'instances', 'versions', 'download', model_instance_version, '-p', path]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

# 将新工具函数包装为工具
download_model_instance_version_tool = FunctionTool(download_kaggle_model_instance_version)
kaggleApiTools.append(download_model_instance_version_tool)

# 定义函数以删除模型实例版本
def delete_kaggle_model_instance_version(model_instance_version: str) -> str:
    """删除模型实例版本。

    Args:
        model_instance_version (str): 模型实例版本名称。

    Returns:
        str: 删除结果的输出。

    工具名称: delete_model_instance_version_tool
    命令: kaggle models instances versions delete <model_instance_version>
    """
    command = ['kaggle', 'models', 'instances', 'versions', 'delete', model_instance_version]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

# 将新工具函数包装为工具
delete_model_instance_version_tool = FunctionTool(delete_kaggle_model_instance_version)
kaggleApiTools.append(delete_model_instance_version_tool)

# 定义函数以查看当前配置值
def view_kaggle_config() -> str:
    """查看当前配置值。

    Returns:
        str: 配置值的输出。

    工具名称: view_config_tool
    命令: kaggle config view
    """
    command = ['kaggle', 'config', 'view']
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

# 将新工具函数包装为工具
view_config_tool = FunctionTool(view_kaggle_config)
kaggleApiTools.append(view_config_tool)

# 定义函数以设置配置值
def set_kaggle_config(name: str, value: str) -> str:
    """设置配置值。

    Args:
        name (str): 配置参数名称。
        value (str): 配置参数值。

    Returns:
        str: 设置结果的输出。

    工具名称: set_config_tool
    命令: kaggle config set -n <name> -v <value>
    """
    command = ['kaggle', 'config', 'set', '-n', name, '-v', value]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

# 将新工具函数包装为工具
set_config_tool = FunctionTool(set_kaggle_config)
kaggleApiTools.append(set_config_tool)

# 定义函数以清除配置值
def unset_kaggle_config(name: str) -> str:
    """清除配置值。

    Args:
        name (str): 配置参数名称。

    Returns:
        str: 清除结果的输出。

    工具名称: unset_config_tool
    命令: kaggle config unset -n <name>
    """
    command = ['kaggle', 'config', 'unset', '-n', name]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

# 将新工具函数包装为工具
unset_config_tool = FunctionTool(unset_kaggle_config)
kaggleApiTools.append(unset_config_tool)
