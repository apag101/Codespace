import tiktoken
#Write function to take string input and return number of tokens 
def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens
prompt = []
data = """number of tokens in a text string"""
for i in data:
    prompt.append((num_tokens_from_string(i[0], "davinci")))
    
completion = []
for j in data:
    completion.append((num_tokens_from_string(j[0], "davinci")))
    
res_list = []
for i in range(0, len(prompt)):
    res_list.append(prompt[i] + completion[i])
    
no_of_final_token = 0
for i in res_list:
    no_of_final_token+=i
print("Number of final token",no_of_final_token)