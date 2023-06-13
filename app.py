import streamlit as st
from langchain.agents import create_pandas_dataframe_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv
import pandas as pd
import os

def load_openai_key():
    # Load the OpenAI key from the environment variable
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if openai_api_key is None or openai_api_key == "":
        print("OPENAI_API_KEY is not set")
        exit(1)
    else:
        print("OPENAI_API_KEY is set")
    return openai_api_key

def configure_streamlit():
    st.set_page_config(page_title="Ask your CSV", page_icon=":chart_with_upwards_trend:")
    st.header("Ask your CSV :chart_with_upwards_trend:")

def upload_csv_file():
    csv_file = st.file_uploader("Upload your CSV file", type="csv")
    return csv_file

def process_csv_file(csv_file):
    if csv_file is not None:
        df = pd.read_csv(csv_file)
        return df
    return pd.DataFrame()  # Return an empty DataFrame if no CSV file is uploaded

def run_agent(df):
    if not df.empty:
        # Create the agent using the pandas dataframe toolkit
        agent = create_pandas_dataframe_agent(OpenAI(temperature=0), df, verbose=True)

        # Ask a question about the CSV
        user_question = st.text_input("Ask a question about your CSV: ")

        if user_question is not None and user_question != "":
            with st.spinner(text="In progress..."):
                # Run the agent on the user's question
                st.write(agent.run(user_question))
    else:
        st.write("No CSV file uploaded.")

def main():
    load_dotenv()
    openai_api_key = load_openai_key()
    configure_streamlit()
    csv_file = upload_csv_file()
    df = process_csv_file(csv_file)
    run_agent(df)

if __name__ == "__main__":
    main()
