from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import create_sql_agent
from langchain.memory import ConversationBufferMemory
from db import get_database
from config import OPENAI_API_KEY, MODEL_NAME
from prompt_template import custom_sql_prompt

def get_agent():
    db = get_database()

    llm = ChatOpenAI(
        model=MODEL_NAME,
        temperature=0,
        openai_api_key=OPENAI_API_KEY,
    )

    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    toolkit = SQLDatabaseToolkit(db=db, llm=llm)

    agent_executor = create_sql_agent(
        llm=llm,
        toolkit=toolkit,
        verbose=True,
        memory=memory,
        prompt=custom_sql_prompt,
        handle_parsing_errors=True,
    )

    return agent_executor
