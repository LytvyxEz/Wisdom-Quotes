from google import genai
from google.genai import types

from dotenv import load_dotenv
import os
from abc import ABC, abstractmethod

from uttils import try_except, logger
from .scrap_service import parser

load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# get_quote_function = {   
#     "name": "get_quote",
#     "description": "getting json/dict with quote, author and explaining of quote.",
#     "parameters": {
#         "type": "object",
#         "properties": {
#             "quote": {
#                 "type": "string",
#                 "description": "quote",
#             },
#             "author": {
#                 "type": "string",
#                 "description": "author of quote",
#             },
#             "explaining": {
#                 "type": "string",
#                 "description": "quote explaining",
#             },
#         },
#         "required": ["quote", "author", "explaining"],
#     },
# }


class LLM(ABC):
    @abstractmethod
    def random_quote(self):
        pass
    
    # @staticmethod
    # def get_config():
    #     return types.GenerateContentConfig(tools=[types.Tool(function_declarations=[get_quote_function])])

class Gemini(LLM):
    def __init__(self):
        self.__client = genai.Client(api_key=GEMINI_API_KEY)
        # self.__config = LLM.get_config()
        self.quotes = parser.parse()
    
    
    
    @try_except
    def random_quote(self) -> str:
        response = self.__client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""Choose a random quote from this dict '{self.quotes}' and explain what does it mean.
            Return ONLY a valid JSON object (no markdown, no code blocks, no backticks), like:
            {{
                "quote": "quote here",
                "author": "author here",
                "explaining": "explanation here"
            }}
            """, #config=self.__config
        )
            
        return response.text
        
        
gemini = Gemini()