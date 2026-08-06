import gradio as gr
import ollama
import asyncio
from agent_shopping import get_shopping_agent

async def main():
    global shopping_agent, config
    config = {"configurable": {"thread_id": "shopping_user"}}
    shopping_agent = await get_shopping_agent()

async def chat(message, history):
    """
    Sends the user message to Ollama and returns the model's response.
    """
    try:
        # Send the message to the shopping agent and get the response
        response = await shopping_agent.ainvoke(
            {"messages": [{"role": "user", "content": message}]},
            {"configurable": {"thread_id": "shopping_user"}}
        )
        print(response)
        result = response["messages"][-1].content
        print(result)
        return [{"role": "assistant", "content": result}]

    except Exception as e:
        return [("Error", f"Unexpected error: {e}")]



# Create Gradio Chat Interface
with gr.Blocks() as demo:
    gr.Markdown("## 💬 Chat with Ollama Model")
    chatbot = gr.Chatbot()
    msg = gr.Textbox(placeholder="Type your message here...")
    clear = gr.Button("Clear Chat")

    msg.submit(chat, [msg, chatbot], chatbot)
    clear.click(lambda: None, None, chatbot, queue=False)

# Run the Gradio app
if __name__ == "__main__":
    asyncio.run(main())
    demo.launch(server_name="0.0.0.0", server_port=7860)