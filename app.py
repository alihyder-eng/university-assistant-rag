import streamlit as st

from src.vector_store import load_vector_db
from src.rag_chain import create_rag_chain

st.set_page_config(
    page_title="University Assistant",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 University Assistant")
st.write("Ask questions about university rules, admissions, fees, courses, policies and more.")

if "messages" not in st.session_state:
    st.session_state.messages = []

vector_db = load_vector_db()
qa_chain = create_rag_chain(vector_db)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Ask a question...")

if question:

    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.spinner("Thinking..."):

        result = qa_chain.invoke(
            {
                "query": question
            }
        )

        answer = result["result"]

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

    with st.chat_message("assistant"):
        st.markdown(answer)

        if "source_documents" in result:

            st.markdown("---")
            st.subheader("Sources")

            for doc in result["source_documents"]:

                source = doc.metadata.get("source", "Unknown")

                st.write(source)