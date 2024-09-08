# Required Libraries:llama-index,  openai, streamlit, config, wikipedia
# https://medium.com/towards-data-science/how-i-built-a-custom-gpt-based-chatbot-in-under-10-minutes-with-llamaindex-2102f0173420

import os


#os.environ['OPENAI_API_KEY'] = ''
from llama_index.core import GPTVectorStoreIndex
from llama_index.core import SimpleDirectoryReader

# load the .txt data and convert it into an index
documents_txt = SimpleDirectoryReader('data').load_data()

from llama_index.core import download_loader

# create a wikipedia download loader object
WikipediaReader = download_loader("WikipediaReader")

# # load the wikipedia reader object
# loader = WikipediaReader()
# documents = loader.load_data(pages=['Strawberry'])

# from llama_index import download_loader

# # create a youtube download loader object
YoutubeTranscriptReader = download_loader("YoutubeTranscriptReader")

# # load the youtube_transcript reader
loader = YoutubeTranscriptReader() 

# # generate the index with the data in the youtube video
documents_youtube = loader.load_data(ytlinks=['https://www.youtube.com/watch?v=EYXQmbZNhy8'])

#from llama_index import GPTSimpleVectorIndex

# # construct the index with the txt document
index_txt = GPTVectorStoreIndex.from_documents(documents_txt)

# # construct the index with the Wikipedia document
# index_wiki = GPTSimpleVectorIndex.from_documents(documents)

# # construct the index with the Youtube document
# index_youtube = GPTSimpleVectorIndex.from_documents(documents_youtube)


# # query the .txt index
# index_txt.query("Which fruit is the best?").response

# # query the Wikipedia index
# index_wiki.query('Which countries produce strawberries?').response

# # query the Youtube index
# index_youtube.query('how should I measure the flour?').response

# # irrelevant query
# index_youtube.query('Who is going to win the NBA playoffs?').response


# # save files to disk
# index_wiki.save_to_disk('index_wikepedia.json')
# index_youtube.save_to_disk('index_video.json')
# index_txt.save_to_disk('index_txt.json')

# import streamlit as st
# from llama_index import GPTSimpleVectorIndex
# import os
# import config

# @st.cache_resource
# def load_indexes():
#     """load the pipeline object for preprocessing and the ml model"""

#     # load index files 
#     index_document = GPTSimpleVectorIndex.load_from_disk('index_txt.json')
#     index_video = GPTSimpleVectorIndex.load_from_disk('index_video.json')
#     index_wikepedia = GPTSimpleVectorIndex.load_from_disk('index_wikepedia.json')
#     return index_document, index_video, index_wikepedia

# def main():

#     # api key
#     os.environ['OPENAI_API_KEY'] = 'API_KEY'

#     # load indices
#     index_document, index_video, index_wikepedia = load_indexes()

#     st.header('Custom-Made Chatbots')

#     # select the data to write queries for
#     st.write("Select the data that your chatbot should be trained with:")
#     data = st.selectbox('Data', ('.txt file (My favorite fruits)', 'Youtube Video (Vanilla Cake Recipe)', 'Wikipedia Article (Apple)'))

#     # use the index based on the selected data
#     if data == '.txt file (My favorite fruits)':
#         st.image('fruit.png')
#         index = index_document
#     elif data == 'Youtube Video (Vanilla Cake Recipe)':
#         st.image('cake.png')
#         index = index_video
#     elif data == 'Wikipedia Article (Apple)':
#         st.image('apple.jpeg')
#         index = index_wikepedia

#     # query the selected index
#     query = st.text_input('Enter Your Query')
#     button = st.button(f'Response')
#     if button:
#         st.write(index.query(query))

# if __name__ == '__main__':
#     main()

# #streamlit run app.py