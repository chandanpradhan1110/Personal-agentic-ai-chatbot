from pydantic import BaseModel
from typing import List,Optional
from fastapi import FastAPI

from ai_agents import get_response_from_ai_agent
import uvicorn 
 
class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: Optional[str] = None
    messages: List[str]
    allow_search: bool
    

ALLOWED_MODEL_NAMES = ["llama3-70b-8192","mixtral-8x7b-32768","llama-3.3-70b-versatile","gpt-40-mini"]
    
app=FastAPI(title="Langgraph AI agent")



@app.post("/chat")
def chat_endpoint(request: RequestState):
    
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error":"Invalid model name. Kindly select a valid AI model"}
    
    llm_id = request.model_name
    query = " ".join(request.messages) 
    allow_search = request.allow_search
    provider = request.model_provider
    system_prompt = request.system_prompt
    
    response=get_response_from_ai_agent(llm_id,query,allow_search,provider,system_prompt)
    return response

    

if __name__=="__main__":
    uvicorn.run(app, host="127.0.0.1", port=9999)