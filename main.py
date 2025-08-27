from agents import Agent , Runner , AsyncOpenAI , OpenAIChatCompletionsModel , set_tracing_disabled
from dotenv import load_dotenv
import os

set_tracing_disabled(True)
load_dotenv()


my_key = os.getenv("GEMINI_API_KEY")
base_url = os.getenv("GEMINI_BASE_URL")
model_name = os.getenv("GEMINI_MODEL_NAME")

client = AsyncOpenAI(
    api_key = my_key,base_url = base_url
)

Model = OpenAIChatCompletionsModel(
    openai_client = client, model = str(model_name)
)

agent:Agent = Agent(
    name = "Helpful Agent",
    instructions = "You are a helpful assistant",
    model = Model 
)

# prompt = input("Enter your question : ")
# result = Runner.run_sync(starting_agent=agent , input=prompt)
# print(result.final_output)

