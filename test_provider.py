import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model=os.environ["FEATHERLESS_MODEL"],
    api_key=os.environ["FEATHERLESS_API_KEY"],
    base_url=os.environ["FEATHERLESS_BASE_URL"],
    temperature=0,
)

response = llm.invoke("Reply with exactly: FEATHERLESS_OK")
print(response.content)