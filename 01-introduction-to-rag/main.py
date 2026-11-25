# RETRIEVAL - retreive common words from document matching  user query

documents = [
    "Formula 1 is an international motorsport championship.", #document 1
    "Soft tyres provide high grip but generally degrade faster.",   #document 2
    "Hard tyres generally offer greater durability.",   #document 3
    "A pit stop allows drivers to change tyres during a race.", #document 4
    "DRS reduces aerodynamic drag to improve straight-line speed."  #document 5
]

import re

def tokenize(text):
    return set(re.findall(r"\b\w+\b", text.lower())) #extract individual words and set() removes duplicate words

def retrieve(query,documents,top_k=2):
    query_words=tokenize(query)
    results=[]

    for document in documents:
        document_words=tokenize(document)
        score=len(query_words & document_words) #find common words using '&' and calculate relevance score using len()

        if score>0:
            results.append((score,document))

    results.sort(key=lambda x: x[0], reverse=True) #rank documents by relevance

    return results[:top_k] #limit number of retrieved documents

# AUGMENTATION - enriching user query with retrieved information before sending to LLM

def augment(query,results):
    context="\n".join(document for score, document in results)

    prompt=f"""
        Answer the question using only the provided context.
        If the context does not contain the answer, say you don't know.

        Context: {context}
        Question: {query}
        Answer:
    """

    return prompt

# GENERATION - send our augmented prompt to LLM and receive a natural language answer

import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()


def generate(prompt):
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    response=client.chat.completions.create(
        model=os.environ["GROQ_MODEL"],
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content

def rag(input_query):
    results=retrieve(input_query,documents)

    if not results:
        return "No relevant results found!"

    prompt=augment(input_query,results)
    answer=generate(prompt)

    return answer

if __name__ == "__main__":
    while True:
        query = input("\nAsk a question: ").strip()
        if query.lower() == "exit":
            break
        if query:
            print("\nAnswer:", rag(query))
