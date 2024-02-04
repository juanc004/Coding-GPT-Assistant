# OpenAI GPT4 Assistant Intergration

GPT-4 OpenAI Assistant for React Hooks Examples

## Overview

This project leverages the power of OpenAI's GPT-4 to generate React hook examples for web development, focusing on creating functional components like buttons and theme toggles. It's designed to simplify learning React hooks through practical, commented code examples.

## Prerequisites

- Python 3.6+
- OpenAI API Key: You'll need an API key from OpenAI. You can obtain one by signing up at [OpenAI](https://openai.com/).

## Installation

### 1. Clone Repo

```
git clone https://github.com/juanc004/Coding-GPT-Assistant.git
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Enviroment Variables

Use the .env file to store your OpenAI API key securely. If you don't have a .env file, create one and add the following line:

```
OPENAI_API_KEY='Your-OpenAI-API-Key-Here'
```

## Usage

```
python your_script_name.py
```

### Features

- Interacts with OpenAI's GPT-4 model to generate code examples.
- Focuses on beginner-friendly React hook implementations.
- Utilizes environmental variables for secure API key management.

## How it works

The project is structured around interacting with the OpenAI API to create an AI assistant that provides coding help. Here's a brief overview:

- Initialization: Sets up the OpenAI client and loads necessary configurations.
- Assistant Creation: Although commented out, the code includes a template for creating a new assistant tailored for coding help.
- Message and Run Creation: Sends a specific request to the assistant and initiates the run to generate the response.
- Wait for Completion: A utility function waits for the assistant's response and outputs the result.

## Customization

Feel free to uncomment and modify the assistant creation part to fit your needs. You can adjust the assistant's instructions, name, or even the type of examples you're looking for.
