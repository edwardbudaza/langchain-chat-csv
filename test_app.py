import unittest
from unittest.mock import patch
from io import StringIO
import streamlit as st
import pandas as pd

# Import functions from app.py
from app import load_openai_key, configure_streamlit, upload_csv_file, process_csv_file, run_agent

class AppTestCase(unittest.TestCase):
    @patch("os.getenv")
    def test_load_openai_key(self, mock_getenv):
        mock_getenv.return_value = "test_api_key"
        openai_api_key = load_openai_key()
        self.assertEqual(openai_api_key, "test_api_key")
    
    def test_configure_streamlit(self):
        with patch("streamlit.set_page_config") as mock_set_page_config:
            configure_streamlit()
            mock_set_page_config.assert_called_with(page_title="Ask your CSV", page_icon=":chart_with_upwards_trend:")
    
    @patch("streamlit.file_uploader")
    def test_upload_csv_file(self, mock_file_uploader):
        mock_file_uploader.return_value = "test_csv_file"
        csv_file = upload_csv_file()
        self.assertEqual(csv_file, "test_csv_file")
    
    def test_process_csv_file(self):
        csv_data = "col1,col2\n1,2\n3,4"
        csv_file = StringIO(csv_data)
        df = process_csv_file(csv_file)
        self.assertEqual(df.shape, (2, 2))
    
    @unittest.skip("Skipping test_run_agent_with_csv_file")
    def test_run_agent_with_csv_file(self):
        df = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
        user_question = "What is the sum of col1?"
        with patch("streamlit.text_input") as mock_text_input, \
             patch("streamlit.spinner"), \
             patch("streamlit.write") as mock_write:
            mock_text_input.return_value = user_question
            run_agent(df)
            mock_write.assert_called_with(6)  # Check if the result is correctly displayed
    
    def test_run_agent_without_csv_file(self):
        df = pd.DataFrame()
        with patch("streamlit.write") as mock_write:
            run_agent(df)
            mock_write.assert_called_with("No CSV file uploaded.")

if __name__ == "__main__":
    unittest.main()
