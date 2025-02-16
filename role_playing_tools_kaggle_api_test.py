# 2.7.3 进阶案例 google搜索
# https://fmhw1n4zpn.feishu.cn/docx/AF4XdOZpIo6TOaxzDK8cxInNnCe

from camel.toolkits import SearchToolkit,MathToolkit
from camel.models import ModelFactory
from camel.types import ModelPlatformType
from camel.societies import RolePlaying
from camel.agents.chat_agent import FunctionCallingMessage
from camel.utils import print_text_animated
from colorama import Fore
from kaggleAPI_tool import kaggleApiTools

import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')
api_key = os.getenv('QWEN_API_KEY')
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
os.environ["SEARCH_ENGINE_ID"] = os.getenv("SEARCH_ENGINE_ID")

# 设置代理
#os.environ["http_proxy"] = "http://127.0.0.1:7897"
#os.environ["https_proxy"] = "http://127.0.0.1:7897"
# os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
# os.environ["SEARCH_ENGINE_ID"] = os.getenv("SEARCH_ENGINE_ID")

#定义工具包
tools_list = [
    *SearchToolkit().get_tools(),
    *MathToolkit().get_tools()
]+kaggleApiTools


# 设置任务
# task_prompt = ("有一个很想参加kaggle比赛的人，"
#         "最新的kaggle比赛信息，通过kaggleapi工具查询赛题"
#         "选择推荐一个合适的比赛，并解答提供能够提交比赛的baseline。")
task_prompt = ("kaggle public api 测试，"
        "根据最新的api版本测试每个命令能否执行，根据执行情况介绍可能的条件"
        "按照一般参赛的顺序执行一遍，包括列出比赛，选择一个最近要截止的比赛，与指定比赛相关的文件。"
        "使用kaggleapi工具执行命令行操作，当本地有文件时，使用本地文件，当本地没有文件时，使用api下载文件。"
        "只运行给定可用的工具，不运行其他工具。完成后输出执行过的命令")
        
#如果没有谷歌搜索API，可以使用duckduckgo工具，无需设置api即可使用        
# task_prompt = ("假设现在是2024年，"
#         "牛津大学的成立年份，并计算出其当前年龄。"
#         "然后再将这个年龄加上10年。使用duckduckgo搜索工具。")

# 创建模型
model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI_COMPATIBLE_MODEL,
    model_type="Qwen/Qwen2.5-72B-Instruct",
    url='https://api-inference.modelscope.cn/v1/',
    api_key=api_key
)

# 设置角色扮演
role_play_session = RolePlaying(
    assistant_role_name="api测试员",
    user_role_name="kaggle爱好者",
    assistant_agent_kwargs=dict(
        model=model,
        tools=tools_list,
    ),
    user_agent_kwargs=dict(
        model=model,
    ),
    task_prompt=task_prompt,
    with_task_specify=False,
    output_language='中文'
)

# 设置聊天轮次限制
chat_turn_limit=10

print(
    Fore.GREEN
    + f"AI助手系统消息:\n{role_play_session.assistant_sys_msg}\n"
)
print(
    Fore.BLUE + f"AI用户系统消息:\n{role_play_session.user_sys_msg}\n"
)

print(Fore.YELLOW + f"原始任务提示:\n{task_prompt}\n")
print(
    Fore.CYAN
    + "指定的任务提示:"
    + f"\n{role_play_session.specified_task_prompt}\n"
)
print(Fore.RED + f"最终任务提示:\n{role_play_session.task_prompt}\n")

n = 0
input_msg = role_play_session.init_chat()
while n < chat_turn_limit:
    n += 1
    assistant_response, user_response = role_play_session.step(input_msg)

    if assistant_response.terminated:
        print(
            Fore.GREEN
            + (
                "AI助手终止。原因: "
                f"{assistant_response.info['termination_reasons']}."
            )
        )
        break
    if user_response.terminated:
        print(
            Fore.GREEN
            + (
                "AI用户终止。"
                f"原因: {user_response.info['termination_reasons']}."
            )
        )
        break

    # 打印用户的输出
    print_text_animated(
        Fore.BLUE + f"AI用户:\n\n{user_response.msg.content}\n"
    )

    if "CAMEL_TASK_DONE" in user_response.msg.content:
        break

    # 打印助手的输出，包括任何函数执行信息
    print_text_animated(Fore.GREEN + "AI助手:")
    tool_calls: list[FunctionCallingMessage] = assistant_response.info[
        'tool_calls'
    ]
    for func_record in tool_calls:
        print_text_animated(f"{func_record}")
    print_text_animated(f"{assistant_response.msg.content}\n")

    input_msg = assistant_response.msg