from ollama import generate

# https://medium.com/learnwithrahul/running-ollama-remotely-in-a-secure-way-d14ba13c8d77

# Regular response
# client = Client(host='http://<your-remote-ip>:11434')
response = generate('gemma3:latest', 'Why is the sky blue?')
print(response['response'])
