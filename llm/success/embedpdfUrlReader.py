# Medium article: https://medium.com/thoughts-on-machine-learning/langchain-is-nice-but-have-you-tried-embedchain-215a34421cde

import os
#from mytoken import apikey
import PyPDF2
from embedchain import App

os.environ["OPENAI_API_KEY"] = "apikey"

wikipedia_bot = App()

# Embed Online Resources

wikipedia_bot.add("https://en.wikipedia.org/wiki/Donald_Trump")
wikipedia_bot.add("https://en.wikipedia.org/wiki/Barack_Obama")

while True:
    question = input("Enter your question, or 'quit' to stop the program.\n >>")

    if question == 'quit':
        break

    response = wikipedia_bot.query(question)
    print(f"\n{response}\n")

pdf_bot = App()

# Get pdf text and store it in pdf_text variable
# Initialize the text variable
pdf_text = ""

# Open the PDF file
with open('gpt reasoning paper.pdf', 'rb') as pdf_file:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Get the total number of pages
    num_pages = len(pdf_reader.pages)

    # Loop through all the pages and extract text
    for page_num in range(num_pages):
        # Get a page object
        page = pdf_reader.pages[page_num]

        # Extract text from the page
        page_text = page.extract_text()

        # Append the text to pdf_text variable
        pdf_text += page_text

# Embed content of pdf document

pdf_bot.add(pdf_text, data_type='text')

while True:
    question = input("Enter your question, or 'quit' to stop the program.\n >>")

    if question == 'quit':
        break

    response = pdf_bot.query(question)
    print(f"\n{response}\n")