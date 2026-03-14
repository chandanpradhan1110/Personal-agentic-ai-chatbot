import os 
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langchain.agents import create_agent
from langchain_core.messages.ai import AIMessage

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
OPENAI_API = os.getenv("OPENAI_API_KEY")

openai_llm = ChatOpenAI(model="gpt-4o-mini")
groq_llm = ChatGroq(model="llama-3.3-70b-versatile")

# search_tool = TavilySearch(max_results=2)

# system_prompt = "Act as an AI chatbot who is smart and friendly"

def get_response_from_ai_agent(llm_id,query,allow_search,provider,system_prompt=None):
    if provider=="Groq":
        llm=ChatGroq(model=llm_id)
    elif provider=="OpenAI":
        llm=ChatOpenAI(model=llm_id)
    
    tools = [TavilySearch(max_results=2)] if allow_search else []
    agent = create_agent(
        model=llm,
        tools=tools
    )
# Convert messages into correct format
    formatted_messages = []
    if system_prompt:
        formatted_messages.append(("system", system_prompt))
    formatted_messages.extend(("user", query))

    state = {"messages": formatted_messages}
    response = agent.invoke(state)
    messages=response.get("messages")
    ai_messages = [message.content for message in messages if isinstance(message, AIMessage)]
    return ai_messages[-1]


