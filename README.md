# HR AI Agent System

An AI-powered HR assistant built using LangChain and OpenAI.

## Features

- Resume parsing
- Candidate screening
- HR chatbot
- Leave management
- Interview scheduling
- HR analytics
- Employee management

## Installation

Clone the repository

git clone https://github.com/yourusername/hr-ai-agent

cd hr-ai-agent

Install dependencies

pip install -r requirements.txt

Create .env file

OPENAI_API_KEY=your_openai_api_key_here

Initialize database

python database_setup.py

Run the agent

python agent.py


## Docker Deployment

Build Docker image

docker build -t hr-ai-agent .

Run container

docker run -it -e OPENAI_API_KEY=your_openai_api_key hr-ai-agent