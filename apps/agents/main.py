from langchain_openai import ChatOpenAI
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain.schema import SystemMessage
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain.memory import ConversationBufferMemory
from tools.sql import run_query_tool, list_tables, decscribe_tables_tool
from tools.report import write_report_tool
from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI()

tables = list_tables()
prompt = ChatPromptTemplate(
    messages=[
        SystemMessage(content=(
            f"You are an AI assistant that has access to a SQLite database. \n"
            f"The database has tables of: {tables}\n"
            "Do not make any assumptions about what tables exist"
            "or what columns exist. Instead, use the 'describe_tables' function"
        )),
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad")
    ]
)

memory = ConversationBufferMemory(
    memory_key="chat_history", return_messages=True)
tools = [
    run_query_tool,
    decscribe_tables_tool,
    write_report_tool
]

agent = create_openai_functions_agent(
    llm=chat,
    prompt=prompt,
    tools=tools
)
agent_executor = AgentExecutor(
    agent=agent,
    verbose=True,
    tools=tools,
    memory=memory
)

agent_executor.invoke({
    "input": "How many orders are there? Write the result to an html report."
})

agent_executor.invoke({
    "input": "Repeat the exact same process for users."
})
