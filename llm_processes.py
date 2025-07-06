from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain.prompts import PromptTemplate
from langchain_huggingface import HuggingFacePipeline
import torch

BASE_MODEL = "meta-llama/Llama-3.2-1B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL)
model = AutoModelForCausalLM.from_pretrained(BASE_MODEL)

if torch.cuda.is_available():
    device = "cuda:0"
else:
    device = "cpu"

# Text generation Pipeling.
text_generation_pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    device=device,  # Use 0 for GPU, -1 for CPU
    model_kwargs={"temperature": 0.2, "top_p": 0.7, "max_new_tokens": 5000},
    return_full_text=False,
)

llm = HuggingFacePipeline(pipeline=text_generation_pipeline)

generic_prompt = """
<s><<SYS>>
List the key points with details from the context: 
[INST] The context : {context} [/INST] 
<</SYS>>
"""

pt = PromptTemplate(
    input_variables=["context"],
    template=generic_prompt,
)

# Chaining prompt Template and LLM using LangChain Expression Language(LCEL).
global chain
chain = pt | llm


def generate_summary(prompt):
    result = chain.invoke(input=prompt)
    return result


# text = generate_summary(
#     "The weekly team sync was held on Monday to align everyone on project timelines and blockers. Rahul confirmed that the frontend module for the user dashboard will be completed by Thursday, while Priya raised a concern regarding delays in the data pipeline due to a dependency on the vendor. The team decided to prioritize the API integration tasks in parallel to avoid further bottlenecks. An additional design review was scheduled for Wednesday to finalize the new UI components. It was also suggested that the sprint retro be shifted to Friday to accommodate the product owner's availability."
# )  # Example usage

# print(text)  # Output the generated text
