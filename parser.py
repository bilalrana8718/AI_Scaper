from langchain.chains import ConversationChain, LLMChain
from langchain_core.prompts import ChatPromptTemplate
from groq import Groq
import random
from config import Groq_api_key
# from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain_core.messages import SystemMessage
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
import streamlit as st
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()
groq_api_key = Groq_api_key

system_prompt = (
    "You are an information extraction assistant. Your role is to carefully read provided text content and extract only the specific information as instructed."
    "If no information matches the instructions, return an empty response.")

dom_content = ""
parse_description1 = ""


model='llama-3.1-70b-versatile'


def parse_with_groq(dom_chunks, parse_description):
    
    groq_chat = ChatGroq(
        groq_api_key=groq_api_key,
        model_name=model
    )
   
    prompt = ChatPromptTemplate.from_messages(
        [
            SystemMessage(
                content=system_prompt
            ),
            HumanMessagePromptTemplate.from_template(
                "{human_input}"
            ),
        ]
    )

    conversation = LLMChain(
        llm=groq_chat,
        prompt=prompt,
        verbose=True,
    )

    parsed_results = []
    parsed_results1 = []

    for i, chunks in enumerate(dom_chunks, start=1):
        parse_description1=parse_description
        dom_content=chunks
        template_str = (
            f"You are required to extract specific information from the following content: {dom_content}. "
            "Please follow the instructions below precisely:\n\n"
            f"1. **Extract Only the Specified Information:** Only extract information that matches the exact details provided: {parse_description1}.\n"
            "2. **No Additional Content:** Avoid adding any extra text, commentary, or explanations in your response.\n"
            "3. **Return an Empty Response if No Match:** If no information aligns with the description, return an empty string ('') and nothing else.\n"
            "4. **Output Only the Requested Data:** Your output should contain only the directly requested data, without any additional words or formatting."
        )

        response = conversation.predict(human_input=template_str)
        print(f"Parsed batch {i} of {len(dom_chunks)} with the {response}")
        parsed_results.append(response)

    game = "\n".join(parsed_results)
    template_str1 = (
    "You are tasked with combining the extracted information from multiple content chunks into a single, consolidated response. "
    f"The extracted data from each chunk is provided in {game}, and your job is to merge this data clearly and cohesively, acccording to the prompt {parse_description1}.\n\n"
    
    )
    response = conversation.predict(human_input=template_str1)
    parsed_results1.append(response)

    return "\n".join(parsed_results1)