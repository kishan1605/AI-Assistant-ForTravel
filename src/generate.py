from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from src.config import OPENAI_API_KEY
from src.retrive import get_response

prompt_template = PromptTemplate(
    input_variables = ["context", "query"],
    template = """
        Answer the question using the context when relevant.
        If the context doesn't contain the answer, use your own knowledge.
        Don't invent facts. If you don't know, say so.
        Only answer travel-related questions.

        Context:
        {context}

        Query:
        {query}

        Answer:
    """
)
try:
    llm = ChatOpenAI(api_key = OPENAI_API_KEY, model = "gpt-3.5-turbo", temperature = 0.7)

except Exception as e:
    print(f"Failed to load LLM : {e}")

qachain = prompt_template | llm 

async def generate_output(query: str) -> str:
        docs = await get_response(query)

        if docs:
            context = "\n".join(docs)
        else:
            context = ""
            
        result = qachain.invoke({"context": context, "query": query})

        return result.content