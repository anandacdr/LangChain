from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# Create a chat template with message placeholder for chat history
chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful customer support agent"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{query}"),
])

# Load chat history from file
chat_history = []
try:
    with open("chat_history.txt", "r") as file:
        chat_history = file.readlines()
    print("Loaded chat history:")
    for i, msg in enumerate(chat_history):
        print(f"  {i+1}. {msg.strip()}")
except FileNotFoundError:
    print("No chat history file found, starting fresh")

# Example usage of the chat template
print("\n Chat Template Example:")
print("=" * 50)

# Sample chat history messages
sample_history = [
    HumanMessage(content="I want to request a refund for my order #1234567890."),
    AIMessage(content="Your refund request for order #1234567890 has been initiated. Please wait 3-5 business days for the refund to be processed.")
]

# Format the template with sample data
formatted_messages = chat_template.format_messages(
    chat_history=sample_history,
    query="What's the status of my refund?"
)

print("Formatted messages:")
for i, msg in enumerate(formatted_messages):
    print(f"  {i+1}. {type(msg).__name__}: {msg.content}")

print("\n Message placeholder example completed successfully!")
