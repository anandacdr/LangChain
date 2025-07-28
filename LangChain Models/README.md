# LangChain Models Project

This project demonstrates the use of LangChain with OpenAI models for building AI applications.

## Setup

1. **Activate the virtual environment:**
   ```bash
   source venv/bin/activate
   ```

2. **Install dependencies (already done):**
   ```bash
   pip install langchain langchain-openai python-dotenv
   ```

3. **Set up your OpenAI API key:**
   - Copy `env_example.txt` to `.env`
   - Add your OpenAI API key to the `.env` file
   - Get your API key from: https://platform.openai.com/api-keys

   ```bash
   cp env_example.txt .env
   # Edit .env and add your API key
   ```

## Usage

Run the simple example:
```bash
python simple_langchain_example.py
```

## Project Structure

- `simple_langchain_example.py` - Basic LangChain example with OpenAI
- `venv/` - Python virtual environment
- `env_example.txt` - Environment variables template
- `README.md` - This file

## Next Steps

You can extend this project by:
- Adding more complex LangChain chains
- Implementing memory and conversation history
- Adding document loading and processing
- Creating custom tools and agents

## Troubleshooting

If you encounter issues:
1. Make sure the virtual environment is activated (you should see `(venv)` in your prompt)
2. Verify your OpenAI API key is set correctly in the `.env` file
3. Check that you have sufficient OpenAI API credits 