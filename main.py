import streamlit as st
from langchain.agents import create_pandas_dataframe_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv
import pandas as pd
import os

def main():
    load_dotenv()

    # Load the OpenAI key from the environment variable
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print("OPENAI_API_KEY is not set")
        exit(1)
    else:
        print("OPENAI_API_KEY is set")

    st.set_page_config(page_title="Ask your CSV ")
    st.header("Ask your CSV")

    csv_file = st.file_uploader("Upload your CSV file", type="csv")
     
    if csv_file is not None:
        df = pd.read_csv(csv_file)
        
        # Create the agent using the pandas dataframe toolkit
        agent = create_pandas_dataframe_agent(OpenAI(temperature=0), df, verbose=True)

        # Ask a question about the CSV
        user_question = st.text_input("Ask a question about your CSV: ")

        if user_question is not None and user_question != "":
            with st.spinner(text="In progress..."):
                # Run the agent on the user's question
                st.write(agent.run(user_question))

if __name__ == "__main__":
    main()
