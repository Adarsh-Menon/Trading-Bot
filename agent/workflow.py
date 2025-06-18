from langgraph.graph import StateGraph , START
from langgraph.graph.message import add_messages
from langrgaph.prebuilt.too_node import ToolNode , tools_condition
from langchain_core.messages import AIMessage , HumanMessage
from typing_extensions import Annotated , TypedDict
from utils.model_loader import Model_loader
from toolkit.tools import *

class State(TypedDict):
    messages: Annotated[list,add_messages]



class GraphBuilder:
    
    def __init__(self):
        pass
    
    def _chatbot_node(self,state:State):
        pass
    
    def build():
        pass
    
    def get_graph():
        pass