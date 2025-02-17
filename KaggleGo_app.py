import streamlit as st
from camel.toolkits import SearchToolkit, MathToolkit
from camel.models import ModelFactory
from camel.types import ModelPlatformType
from camel.societies import RolePlaying
from camel.agents.chat_agent import FunctionCallingMessage
from camel.utils import print_text_animated
from colorama import Fore
from kaggleAPI_tool import kaggleApiTools
import os
from dotenv import load_dotenv


# 加载环境变量
load_dotenv(dotenv_path='.env')
QWEN_API_KEY = os.getenv('QWEN_API_KEY')
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")


# Set page configuration
st.set_page_config(page_title="KaggleGo Baseline Generater", layout="wide")
st.title("KaggleGo!")
st.subheader("CAMEL-AI RolePlaying Society Session with DeepSeek/Qwen & AIML API,Kaggle API")
st.markdown("""
This interactive AI demo simulates a **role-playing conversation** between two AI agents. 
_demo version_
**How it works:**
1. Configure the session by providing roles and a task.
2. Run multiple rounds of conversation between the AI agents.
3. Get a final consolidated strategy using **DeepSeek using AIML API** .
""")

# # Streamlit界面设置
# st.title("KaggleGo!") 
# st.write("_demo version_")
# st.subheader("RolePlaying() & KaggleAPI")

# Sidebar: API Key Setup
st.sidebar.header("🔑 API Key Setup")
st.sidebar.markdown("Provide the necessary API keys:")
# 一键填入API密钥
if st.sidebar.button("一键填入试用密钥 / Fill Trial Keys"):
    qwen_api_key = QWEN_API_KEY
    google_api_key = GOOGLE_API_KEY
    search_engine_id = SEARCH_ENGINE_ID
else:
    qwen_api_key = st.sidebar.text_input("Qwen API Key", type="password")
    google_api_key = st.sidebar.text_input("Google API Key", type="password")
    search_engine_id = st.sidebar.text_input("Search Engine ID", type="password")

# 设置环境变量
if google_api_key:
    os.environ["GOOGLE_API_KEY"] = google_api_key
if qwen_api_key:
    os.environ["QWEN_API_KEY"] = qwen_api_key
if search_engine_id:
    os.environ["SEARCH_ENGINE_ID"] = search_engine_id

# 检查 API 密钥是否设置
if not google_api_key or not qwen_api_key or not search_engine_id:
    st.sidebar.error("⚠️ All API keys are required to proceed.")
    st.stop()
st.sidebar.success("✅ API keys set successfully!")

# 重置密钥功能
if st.sidebar.button("重置密钥Reset Keys"):
    qwen_api_key = ""
    google_api_key = ""
    search_engine_id = ""
    os.environ["GOOGLE_API_KEY"] = ""
    os.environ["QWEN_API_KEY"] = ""
    os.environ["SEARCH_ENGINE_ID"] = ""
    st.sidebar.success("✅ API keys have been reset!")


# 定义工具包
tools_list = [
    *SearchToolkit().get_tools(),
    *MathToolkit().get_tools()
] + kaggleApiTools

# 设置任务
task_prompt = ("kaggle public api 测试，"
               "根据最新的api版本测试每个命令能否执行，根据执行情况介绍可能的条件"
               "按照一般参赛的顺序执行一遍，包括列出比赛，选择一个最近要截止的比赛，与指定比赛相关的文件。"
               "使用kaggleapi工具执行命令行操作，当本地有文件时，使用本地文件，当本地没有文件时，使用api下载文件。"
               "只运行给定可用的工具，不运行其他工具。完成后输出执行过的命令")

# 创建模型
model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI_COMPATIBLE_MODEL,
    model_type="Qwen/Qwen2.5-72B-Instruct",
    url='https://api-inference.modelscope.cn/v1/',
    api_key=os.getenv('QWEN_API_KEY')
)
# # 创建模型
# model = ModelFactory.create(
#     model_platform=ModelPlatformType.AIML,
#     model_type="Qwen/Qwen2.5-72B-Instruct",
#     url='https://api-inference.modelscope.cn/v1/',
#     api_key=api_key
# )

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


# 初始化消息列表
messages = []

# # 输入框
# input_task = st.text_input("输入您的消息:")
# # input_msg = st.button('KaggleGo')

st.write("task_prompt：Kaggle public API testing, "
         "testing whether each command can be executed based on the latest API version, introducing possible conditions based on execution results. "
         "Executing in the order generally followed in competitions, including listing competitions, selecting a competition that is about to close, and files related to the specified competition. "
         "Using Kaggle API tools to execute command line operations, using local files when available, and downloading files via API when local files are not available. "
         "Only running the given available tools and not running any other tools. Completing the task and outputting the executed commands.\n"
)
st.write("task_prompt：kaggle public api 测试，"
         "根据最新的api版本测试每个命令能否执行，根据执行情况介绍可能的条件"
         "按照一般参赛的顺序执行一遍，包括列出比赛，选择一个最近要截止的比赛，与指定比赛相关的文件。"
         "使用kaggleapi工具执行命令行操作，当本地有文件时，使用本地文件，当本地没有文件时，使用api下载文件。"
         "只运行给定可用的工具，不运行其他工具。完成后输出执行过的命令")
# 发送按钮
if st.button("KaggleGo!"):
    n = 0
    input_msg = role_play_session.init_chat()
    chat_turn_limit = 10
    while n < chat_turn_limit:
        n += 1
        assistant_response, user_response = role_play_session.step(input_msg)

        if assistant_response.terminated:
            st.write(Fore.GREEN + "AI助手终止。原因: " + f"{assistant_response.info['termination_reasons']}.")
            break
        if user_response.terminated:
            st.write(Fore.GREEN + "AI用户终止。原因: " + f"{user_response.info['termination_reasons']}.")
            break

        # 添加用户和助手的消息到消息列表
        messages.append({"role": "用户", "content": user_response.msg.content})
        messages.append({"role": "助手", "content": assistant_response.msg.content})

        st.empty()
        # 打印用户和助手的输出
        for message in messages:
            st.write(f"**{message['role']}**: {message['content']}")

        input_msg = assistant_response.msg
