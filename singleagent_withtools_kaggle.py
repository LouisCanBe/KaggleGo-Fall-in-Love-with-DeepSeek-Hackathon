# kaggleTool
from camel.agents import ChatAgent
from camel.models import ModelFactory
from camel.types import ModelPlatformType
from camel.messages import BaseMessage

from dotenv import load_dotenv

import os

load_dotenv(dotenv_path='.env')

api_key = os.getenv('QWEN_API_KEY')

model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI_COMPATIBLE_MODEL,
    model_type="Qwen/Qwen2.5-72B-Instruct",
    url='https://api-inference.modelscope.cn/v1/',
    api_key=api_key
)

# # 使用deepseek的模型 AI/ML
# model = ModelFactory.create(
#     model_platform=ModelPlatformType.OPENAI_COMPATIBLE_MODEL,
#     # model_type="deepseek-ai/deepseek-coder-33b-instruct",
#     # model_type="claude-3-5-sonnet-20240620",
#     # model_type="deepseek/deepseek-r1",
#     model_type="gemini-2.0-flash-exp",
#     # model_type="gpt-4o-mini-2024-07-18",#x
#     # model_type="qwen-max-2025-01-25",
#     url='https://api.aimlapi.com/v1',
#     api_key='AI/ML key',
#     # model_config_dict={"temperature": 0.6, "max_tokens": 32000}
# )

# 定义系统消息
sys_msg = "你是Kaggle比赛爱好者，随时查看最新比赛情况"


agent = ChatAgent(system_message=sys_msg, model=model,output_language='中文')


# 定义用户消息
usr_msg = "最近有什么kaggle比赛？列出来看看，然后再给我看看离截止时间最近的比赛的相关数据集，如果下载不了也先列举出来"

# 发送消息给agent
# response = agent.step(usr_msg)
# print(response.msgs[0].content)

# 增加工具
from camel.toolkits import FunctionTool
import subprocess

def list_kaggle_competitions() -> str:
    """列出当前活动的Kaggle比赛。

    Returns:
        str: 比赛列表的输出。
    """
    result = subprocess.run(['kaggle', 'competitions', 'list'], capture_output=True, text=True)
    return result.stdout

def download_kaggle_competition(competition: str) -> str:
    """下载与指定比赛相关的文件。

    Args:
        competition (str): 比赛名称。

    Returns:
        str: 下载结果的输出。
    """
    result = subprocess.run(['kaggle', 'competitions', 'download', '-c', competition], capture_output=True, text=True)
    return result.stdout

def submit_kaggle_competition(competition: str, file_path: str, message: str) -> str:
    """提交到指定的Kaggle比赛。

    Args:
        competition (str): 比赛名称。
        file_path (str): 提交的文件路径。
        message (str): 提交消息。

    Returns:
        str: 提交结果的输出。
    """
    result = subprocess.run(['kaggle', 'competitions', 'submit', '-c', competition, '-f', file_path, '-m', message], capture_output=True, text=True)
    return result.stdout

def list_kaggle_datasets(keyword: str) -> str:
    """列出与搜索关键词匹配的数据集。

    Args:
        keyword (str): 搜索关键词。

    Returns:
        str: 数据集列表的输出。
    """
    result = subprocess.run(['kaggle', 'datasets', 'list', '-s', keyword], capture_output=True, text=True)
    return result.stdout

def download_kaggle_dataset(dataset: str) -> str:
    """下载与指定数据集相关的文件。

    Args:
        dataset (str): 数据集名称。

    Returns:
        str: 下载结果的输出。
    """
    result = subprocess.run(['kaggle', 'datasets', 'download', '-d', dataset], capture_output=True, text=True)
    return result.stdout

def create_kaggle_dataset(path: str) -> str:
    """创建新的Kaggle数据集。

    Args:
        path (str): 数据集文件夹路径。

    Returns:
        str: 创建结果的输出。
    """
    result = subprocess.run(['kaggle', 'datasets', 'create', '-p', path], capture_output=True, text=True)
    return result.stdout

def version_kaggle_dataset(path: str, message: str) -> str:
    """创建现有数据集的新版本。

    Args:
        path (str): 数据集文件夹路径。
        message (str): 版本消息。

    Returns:
        str: 创建版本结果的输出。
    """
    result = subprocess.run(['kaggle', 'datasets', 'version', '-p', path, '-m', message], capture_output=True, text=True)
    return result.stdout

def list_kaggle_kernels(keyword: str) -> str:
    """列出与搜索关键词匹配的笔记本。

    Args:
        keyword (str): 搜索关键词。

    Returns:
        str: 笔记本列表的输出。
    """
    result = subprocess.run(['kaggle', 'kernels', 'list', '-s', keyword], capture_output=True, text=True)
    return result.stdout

def push_kaggle_kernel(path: str) -> str:
    """推送笔记本到Kaggle。

    Args:
        path (str): 笔记本文件夹路径。

    Returns:
        str: 推送结果的输出。
    """
    result = subprocess.run(['kaggle', 'kernels', 'push', '-p', path], capture_output=True, text=True)
    return result.stdout

def pull_kaggle_kernel(kernel: str, path: str) -> str:
    """拉取指定的Kaggle笔记本。

    Args:
        kernel (str): 笔记本名称。
        path (str): 下载路径。

    Returns:
        str: 拉取结果的输出。
    """
    result = subprocess.run(['kaggle', 'kernels', 'pull', kernel, '-p', path, '-m'], capture_output=True, text=True)
    return result.stdout

# 将新工具函数包装为工具
list_competitions_tool = FunctionTool(list_kaggle_competitions)
download_competition_tool = FunctionTool(download_kaggle_competition)
submit_competition_tool = FunctionTool(submit_kaggle_competition)
list_datasets_tool = FunctionTool(list_kaggle_datasets)
download_dataset_tool = FunctionTool(download_kaggle_dataset)
create_dataset_tool = FunctionTool(create_kaggle_dataset)
version_dataset_tool = FunctionTool(version_kaggle_dataset)
list_kernels_tool = FunctionTool(list_kaggle_kernels)
push_kernel_tool = FunctionTool(push_kaggle_kernel)
pull_kernel_tool = FunctionTool(pull_kaggle_kernel)

tools=[
    list_competitions_tool,
    download_competition_tool,
    submit_competition_tool,
    list_datasets_tool,
    download_dataset_tool,
    create_dataset_tool,
    version_dataset_tool,
    list_kernels_tool,
    push_kernel_tool,
    pull_kernel_tool
]

# for tool in tools:
#     if hasattr(tool, 'function') and isinstance(tool.function, dict) and 'strict' in tool.function:
#         del tool.function['strict']

# 更新工具列表
tool_agent = ChatAgent(
    tools=tools,
    system_message=sys_msg,
    model=model,
    output_language="中文"
)

# 重新发送消息给toolagent
response = tool_agent.step(usr_msg)
print(response.msgs[0].content)