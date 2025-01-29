from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

def generate_pet_names(animal, color):
    llms = OpenAI(temperature=0.7)

    Prompt_Template = PromptTemplate(
        input_variables=["animal","color"],
        template = "i have a {animal}. it is {color} in color. i want to name it. suggest 5 names for it.") 

    name_chain = LLMChain(llm = llms, prompt = Prompt_Template )

    response = name_chain({'animal': animal, 'color':color})
    return response

if __name__=="__main__":
    print(generate_pet_names("cat",'black'))