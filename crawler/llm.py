from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
import os

class ChatTranslateLLM(ChatOpenAI):
    """
    基于 LangChain OpenAI 接口的翻译与关键词抽取类。
    支持中文翻译与关键词提取任务。
    """

    def __init__(
        self,
        model_name: str = "deepseek-v3:671b",
        openai_api_base: str = "https://uni-api.cstcloud.cn/v1",
        **kwargs
    ):
        openai_api_key = os.getenv("OPENAI_API_KEY")
        if not openai_api_key:
            raise ValueError("Environment variable OPENAI_API_KEY is not set.")
        super().__init__(
            model_name=model_name,
            openai_api_base=openai_api_base,
            openai_api_key=openai_api_key,
            **kwargs
        )

    def translate(self, content: str) -> str:
        prompt = "请只翻译下面的英文为中文，不要添加任何解释或注释：\n"
        response = self.invoke([HumanMessage(content=prompt + content)])
        return response.content.strip()

    def extract_key_words(self, content: str) -> str:
        prompt = (
            "从文本中提取关键词，要求返回关键词列表（用逗号分隔），不附带多余说明。"
        )
        response = self.invoke([HumanMessage(content=prompt + content)])
        return response.content.strip()
    
    def extract_key_words(self, content: str) -> str:
        prompt = (
            "从文本中提取关键词，要求返回关键词列表（用逗号分隔），不附带多余说明。"
        )
        response = self.invoke([HumanMessage(content=prompt + content)])
        return response.content.strip()
    
    def interpretation(self, title: str, content: str) -> str:
        prompt = (
            f"请对以下论文进行深入解读，包括但不限于：研究目的、研究方法、核心观点、创新点和潜在影响。"
            f"要求语言简洁、逻辑清晰、条理明确，不添加与内容无关的评价。\n\n"
            f"【论文标题】\n{title}\n\n"
            f"【论文内容】\n{content}\n"
        )
        response = self.invoke([HumanMessage(content=prompt)])
        return response.content.strip()
    

def main():
    # 实例化模型
    llm = ChatTranslateLLM()

    # 测试英文翻译
    english_text = "Large language models are transforming the way we interact with knowledge."
    translated = llm.translate(english_text)
    print("🔁 翻译结果:")
    print(translated)
    print("\n")

    # 测试关键词提取
    abstract_text = (
        "This paper proposes a new multi-agent reinforcement learning algorithm "
        "that achieves higher sample efficiency in dynamic environments."
    )
    keywords = llm.extract_key_words(abstract_text)
    print("🔍 关键词提取结果:")
    print(keywords)

if __name__ == "__main__":
    main()