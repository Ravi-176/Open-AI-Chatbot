import streamlit as st
from PyPDF2 import PdfReader
from langchain_classic.chains.question_answering import load_qa_chain
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI
from streamlit import sidebar
OpenAIKey=st.secrets("OPEN_ROUTER_API_KEY")
st.header("NoteBot")
with sidebar:
    st.title("My Notes")
    file=st.file_uploader("Upload notes PDF and start asking questions",type="PDF")
#Extracting text
if file is not None:
    my_pdf=PdfReader(file)
    text=""
    for page in my_pdf.pages:
        text += page.extract_text()
        #st.write(text)
    #Break it into chunks
    splitter = RecursiveCharacterTextSplitter(separators=["\n"],chunk_size=250,chunk_overlap=50)
    chunks=splitter.split_text(text)
    #st.write(chunks)
    #Creating object of OpenAIEmbeddings which lets us connect to embedding models
    embeddings=HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    #generating embeddings,creating a vector database and storing the embeddings
    vector_store=FAISS.from_texts(chunks,embeddings)
    #get user query
    user_query = st.text_input("Type your query here")
    #similarity search(finding chunks which match the user query)
    if user_query:
        matching_chunks=vector_store.similarity_search(user_query)
        #define our LLM
        llm = ChatOpenAI(
            model="openai/gpt-oss-20b",
            openai_api_key=OpenAIKey,
            base_url="https://openrouter.ai/api/v1",
            temperature=0
        )
        #Generating the response
        chain=load_qa_chain(llm,chain_type="stuff")
        output=chain.run(question=user_query,input_documents=matching_chunks)
        st.write(output)
