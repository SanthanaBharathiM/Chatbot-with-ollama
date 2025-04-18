from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

def main():
    template = """
    Answer the question below.
     
    Here is the conversation history: {context}
     
    Question: {question}
     
    Answer:
    """
    model = OllamaLLM(model='llama3.1')
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model 
    context = ""
    print("Welcome to conversation! Type 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        result = chain.invoke({'context': context, 'question': user_input})
        print('AI:', result)
        context += f'\nUser: {user_input}\nAI: {result}'

if __name__ == "__main__":
    main()
