# LLM Agents Workshop - TUM, April 27, 2024

Welcome to the LLM Agents Workshop Repository! This workshop is designed to introduce you to the concept of Language Model (LLM) Agents and guide you through creating your own custom agent using a provided template. The session is set for April 27, 2024, at the Technical University of Munich (TUM).

## Workshop Overview

In this workshop, you will:
- Gain a brief introduction to the concept of LLM Agents.
- Learn how to interact with a hosted LLM inference endpoint using Llama3 by Facebook.
- Use a provided template to create a custom LLM Agent that can assist with tasks like booking holidays, organizing emails, creating PowerPoint presentations, and more.

## Prerequisites

Before attending the workshop, please ensure you have:
- Basic knowledge of Python programming.
- An installed version of Python 3.7 or later.
- Git installed on your machine to clone this repository.
- A working code editor

## Setup Instructions

1. **Clone the Repository**
   ```
   git clone https://github.com/JordiSpranger/llm-agents-tum.git
   cd llm-agents-tum
   ```
   
2. **Install Required Libraries**
```
pip install -r requirements.txt
```

3.  **Set Up Your Environment**
Create a .env file in the root of the project directory and add the following line:

```
LLM_ENDPOINT_URL=<Your-Inference-API-URL>
```
