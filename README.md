# Agent One Crew
![image](https://github.com/user-attachments/assets/c2de62f5-ebe4-4bda-a6cb-815cd6679a74)

![image](https://github.com/user-attachments/assets/42365b7e-095d-41b2-bed3-789c9bda00e2)

Welcome to the AgentOne Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities. 

Agent One Crew Runner is a lightweight Flask-based web application that allows you to run an AI agent (referred to as "crew") by providing a topic via an HTTP POST request. The backend logic leverages the AgentOne class from the agent_one module, which processes the input and generates an output.

## Prerequisites
Before running the application, ensure you have the following installed:

- Python 3.10 or higher
- Pip (Python package manager)
- Flask (pip install flask)
- Other dependencies listed in requirements.txt

## Installation
Clone this repository:
- git clone
- cd agent_one
- Install the required dependencies:
- pip install -r requirements.txt
- Ensure the agent_one module is correctly set up in the parent directory or adjust the import path accordingly.

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/agent_one/config/agents.yaml` to define your agents
- Modify `src/agent_one/config/tasks.yaml` to define your tasks
- Modify `src/agent_one/crew.py` to add your own logic, tools and specific args
- Modify `src/agent_one/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the agent-one Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The agent-one Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Features
HTTP API : Exposes an endpoint /run to trigger the execution of the crew.
Frontend : Provides a basic HTML frontend for user interaction.
Error Handling : Gracefully handles errors and returns appropriate error messages.
Dynamic Year Input : Automatically injects the current year into the crew's input parameters.

## Usage
Running the Application
To start the Flask server, execute the following command:

python app.py

By default, the application will run on http://0.0.0.0:5000.

## Accessing the Frontend
Navigate to http://localhost:5000 in your browser to access the frontend interface.
