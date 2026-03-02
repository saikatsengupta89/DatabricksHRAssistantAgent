import gradio as gr
import os
from mlflow.deployments import get_deploy_client

# Databricks Apps injects the serving endpoint name via environment variable
SERVING_ENDPOINT = os.environ.get("SERVING_ENDPOINT", "hr-policy-agent-endpoint")
client = get_deploy_client("databricks")

def ask_agent(question: str, history: list) -> str:
    # Databricks Apps automatically injects the logged-in user's email
    user_email = os.environ.get("DATABRICKS_APP_USER", "employee@mssquare.com")

    response = client.predict(
        endpoint=SERVING_ENDPOINT,
        inputs={
            "dataframe_records": [          # ✅ correct wrapper for mlflow langchain serving
                {
                    "input": question,
                    "current_user": user_email,
                    "chat_history": []
                }
            ]
        }
    )
    return response["predictions"][0]["output"]

demo = gr.ChatInterface(
    fn=ask_agent,
    title="MS-Square HR Policy Assistant",
    description="Ask me anything about company HR policies.",
    examples=[
        "How many annual leave days am I entitled to?",
        "What is the code of conduct policy?",
        "I want to speak to someone in HR"
    ]
)

demo.launch(server_name="0.0.0.0")