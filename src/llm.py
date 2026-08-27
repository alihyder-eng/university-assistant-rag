import os

from dotenv import load_dotenv

load_dotenv()


def load_llm():

    provider = os.getenv("LLM_PROVIDER", "ollama").lower()

    if provider == "ollama":

        from langchain_ollama import ChatOllama

        model = os.getenv(
            "OLLAMA_MODEL",
            "llama3.2:3b"
        )

        llm = ChatOllama(
            model=model,
            temperature=0,
        )

        return llm

    elif provider == "openai":

        from langchain_openai import ChatOpenAI

        llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0,
        )

        return llm

    elif provider == "gemini":

        from langchain_google_genai import ChatGoogleGenerativeAI

        llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0,
        )

        return llm

    else:

        raise ValueError(
            "Unsupported LLM_PROVIDER."
        )


if __name__ == "__main__":

    llm = load_llm()

    response = llm.invoke(
        "Introduce yourself in one sentence."
    )

    print(response.content)