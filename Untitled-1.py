import streamlit as st
import ollama

# 1. Setup the Page UI
st.set_page_config(page_title="My Offline Assistant", page_icon="🤖")
st.title("Offline Chatbot")
st.caption("No Internet Required") 
st.caption("Created by Srijit")

# 2. Initialize Chat History (Memory)
if "messages" not in st.session_state:
    st.session_state.messages = []

# 3. Display past messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Chat Input
if prompt := st.chat_input("Ask me anything..."):
    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # This calls your local Ollama engine
                response = ollama.chat(
                    model='llama3.2:1b', 
                    messages=st.session_state.messages
                )
                answer = response['message']['content']
                st.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
            except Exception as e:
                st.error("Make sure Ollama is running in the background!")