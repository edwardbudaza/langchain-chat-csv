# Using Docker to Containerize Your Streamlit App 🐳

Follow these steps to containerize your Streamlit app using Docker:

1. Place the Dockerfile in the same directory as your `app.py` file.

2. Create a `requirements.txt` file listing all the dependencies required by your application. Include all the libraries and packages necessary for your Streamlit app to run.

3. Build the Docker image using the following command in the terminal:
    ```
    docker build -t myapp .
    ```
   Replace `myapp` with your preferred image name. The `.` at the end denotes the current directory as the build context.

4. Run the Docker container using the following command:
    ```
    docker run -p 8501:8501 myapp
    ```
   Replace `myapp` with the image name you used in the previous step. This command runs the container and maps the default port `8501` used by Streamlit to the host machines port `8501`.

5. Access your Streamlit application in your browser by navigating to `http://localhost:8501`.

By containerizing your Streamlit app, you can easily distribute and deploy it on different environments without worrying about dependencies and configurations. Docker provides a consistent and isolated environment, ensuring that your app runs reliably across different systems.

Enjoy the seamless deployment of your Streamlit app with Docker! 🚀
