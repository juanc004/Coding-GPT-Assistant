# Import necessary libraries and modules.
import openai
from dotenv import find_dotenv, load_dotenv
import time
import logging
from datetime import datetime

# Load the OpenAI API key.
load_dotenv()

# Initialize the OpenAI client 
client = openai.OpenAI()

# Set the model to use for the assistant
model="gpt-4-turbo-preview"

# Create the Assistant 
# IMPORTANT! (Uncomment this to create your assistant) 

# coding_assistant = client.beta.assistants.create(
#     name="Full-Stack Engineer Tutor",
#     instructions="You are a full-stack software engineer with over 20 plus years of experience working with front-end and backend technologies. Explain, write and teach me about how to programming.",
#     tools=[{"type": "code_interpreter"}],
#     model=model
# )
# assistant_id = coding_assistant.id
# print(assistant_id)


# === Create the Thread ===
# thread = client.beta.threads.create(
#   messages=[
#       {
#         "role": "user",
#         "content": "How can I get started building a basic personal portfolio website using React.ts?"
#       }
#     ]
# )

# thread_id = thread.id
# print(thread_id)



# Hardcoded IDs for demonstration purposes. Replace these with dynamic IDs in a production environment.
assistant_id = "asst_y0ruNMOSs8HeNq8ilWvgN1qO" # Update with you unique assistant_id
thread_id= "thread_geGmUW0FPUMRyAMD4Bvu4bVC" # Update with you unique thread id

# Create the Message 
message = """
Can you provide commented React hook examples for implementing common website components? Specifically, I'm looking for a button component that performs an action when clicked, and a way to toggle a website's theme between light and dark modes. The comments should explain what each part of the code is doing, making it easy to understand for someone new to React."
"""

message = client.beta.threads.messages.create(
  thread_id=thread_id,
  role="user",
  content=message
)

#  Run Assistant 
instructions= """
Generate React hook examples for a button component and a theme toggle feature. The code should be fully commented to explain the functionality and usage of hooks in these contexts. Focus on beginner-friendly explanations and include:
- A simple button component that uses the useState hook to count clicks.
- A theme toggle component that uses the useContext hook to switch between light and dark themes.
Ensure that the examples are concise and clear, suitable for incorporation into a React-based website.
"""

run = client.beta.threads.runs.create(
  assistant_id=assistant_id,
  thread_id=thread_id,
  instructions=instructions
)

def wait_for_run_completion(client, thread_id, run_id, sleep_interval=5):
    """

    Waits for a run to complete and prints the elapsed time.:param client: The OpenAI client object.
    :param thread_id: The ID of the thread.
    :param run_id: The ID of the run.
    :param sleep_interval: Time in seconds to wait between checks.
    """
    while True:
        try:
            run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id)
            if run.completed_at:
                elapsed_time = run.completed_at - run.created_at
                formatted_elapsed_time = time.strftime(
                    "%H:%M:%S", time.gmtime(elapsed_time)
                )
                print(f"Run completed in {formatted_elapsed_time}")
                logging.info(f"Run completed in {formatted_elapsed_time}")

                messages = client.beta.threads.messages.list(thread_id=thread_id)
                last_message = messages.data[0]
                response = last_message.content[0].text.value
                print(f"Assistant Response: {response}")
                break
        except Exception as e:
            logging.error(f"An error occurred while retrieving the run: {e}")
            break
        logging.info("Waiting for run to complete...")
        time.sleep(sleep_interval)


# Retrieve and print steps and logs after the run completes
wait_for_run_completion(client=client, thread_id=thread_id, run_id=run.id)

run_steps = client.beta.threads.runs.steps.list(
    thread_id=thread_id,
    run_id=run.id
)
print(f"Steps---> {run_steps.data[0]}")
