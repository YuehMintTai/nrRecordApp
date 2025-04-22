import streamlit as st, time, json,pandas as pd
from accessments import form_base,form_cognitive,form_emotion,form_note,form_physic
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

st.title('🤖 AI護理記錄生成系統05-JSON篇')
#建立session_state
if "t1Text" not in st.session_state: st.session_state.t1Text={}
if "t2Text" not in st.session_state: st.session_state.t2Text='🍀 JSON編輯'
if "t3Text" not in st.session_state: st.session_state.t3Text='💎 AI生成'
if "t4Text" not in st.session_state: st.session_state.t4Text='📌 資料管理'
if "t5Text" not in st.session_state: st.session_state.t5Text='🚩 風險評估'
if "model" not in st.session_state: st.session_state.model='mistral:latest'
@st.cache_resource 
def AI_generate(text):
    llmModel=ChatOllama(model=st.session_state.model)
    myParser=StrOutputParser()
    myPrompt=ChatPromptTemplate(messages=[
        ('system','根劇提供資料生成一份描述性的護理記錄,不要使用表列,請使用完整的句子描述,限定使用繁體中文和台灣用語。'),
        ('user',text)]
        )
    myChain=myPrompt|llmModel|myParser
    beginTime=time.time()
    myResponse=myChain.invoke({'user':text})
    return myResponse+'(耗時'+str(round(time.time()-beginTime,2))+'秒)'

#建立tabs
t1,t2,t3,t4,t5=st.tabs(['🐮 快速選單','🍀 JSON編輯','💎 AI生成','📌 AI對話','🚩 風險評估'])
with t1:
    myDict={}
    myDict.update(form_base())
    myDict.update(form_cognitive())
    myDict.update(form_emotion())
    myDict.update(form_physic())
    myDict.update(form_note())
    st.session_state.t1Text.update(myDict)  
    st.session_state.t2Text=st.session_state.t1Text
with t2:
    t2TextArea=st.text_area('入JSON格式資料',value=st.session_state.t2Text)
    t2Button=st.button('儲存此JSON格式資料')
    if t2Button:
        st.session_state.t2Text=t2TextArea
        # with open('myPatient.json','a+',encoding='utf-8') as f:
        #     f.write(json.dumps(st.session_state.t2Text,ensure_ascii=False))
        #     f.write(',')
        #     f.close()
        st.session_state.t3Text=st.session_state.t2Text
        st.success('儲存成功')
    #st.write(st.session_state.t2Text)
with t3: ## AI生成
    with st.sidebar.container():
        values=['mistral:latest','gemma2:latest','deepseek-r1:8b','phi4:latest','lamma3.2:latest','mistral-small:24b']
        default_index=values.index('mistral:latest')
        model=st.selectbox('選擇模型',values,index=default_index)
        st.session_state.model=model
    myString=st.session_state.t3Text.replace('{','').replace('}','').replace('\"','').replace(':','').replace(',','').replace('\'','')
    myString=AI_generate(myString)
    st.write(myString)
   
    t3Button=st.button('碓定修改')
    if t3Button:
        t3TextArea=st.text_area('AI生成',value=AI_generate(myString),height=400)
        st.session_state.t3Text=t3TextArea
        st.session_state.t4Text=t3TextArea
with t4: ## AI對話
    from langchain.chains import ConversationChain
    from langchain.memory import ConversationBufferWindowMemory
    myMemory=ConversationBufferWindowMemory(k=7)
    myConversation=ConversationChain(memory=myMemory,llm=ChatOllama(model=st.session_state.model),verbose=False)
    systemPrompt=(
        "針對以下的護理記錄進行對話，請依照使用者的問題進行修改。"
        "內容必需符合護理記錄的事實內容，並且使用繁體中文和台灣用語。"
        "不可以使用表列，請使用完整的句子描述。"
        "不知道的內容可以詢問,但不可以隨意編造內容。"
        "內容少於1000字元:\n\n`"
        f"{st.session_state.t4Text}"
    )
    print(systemPrompt)
    myConversation.memory.save_context({'role':'system'},{'content':systemPrompt})
    with st.chat_message('ai'):
        st.write(f'🤖 AI: {systemPrompt}')
    # for message in myMemory:
    #     with st.chat_message(message.role):
    #         st.write(f'{message.role}: {message.content}')

    userPrompt=st.chat_input('請幫我摘要成500個字元')
    if userPrompt:
        myConversation.memory.save_context({'role':'user'},{'content':userPrompt})
        beginTime=time.time()
        myResponse=myConversation.invoke(userPrompt)
        endTime=time.time() 
        st.write(f'👩‍⚕️ 你: {userPrompt}')
        st.write(f'🤖 AI: {myResponse} 耗時: {round(endTime-beginTime,2)}秒')
with t5:
    from langchain_community.document_loaders import PyPDFLoader 
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    from langchain_community.embeddings import OllamaEmbeddings
    from langchain_community.vectorstores import Chroma
    myLlm=ChatOllama(model=st.session_state.model)  
    myLoader=PyPDFLoader('預防病人跌倒.pdf')###,encoding='utf-8')
    page=myLoader.load_page(0)
    text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=100,
        chunk_overlap=10,
        separators=['。','?','!','\n']
    )
    docs=[]
    for page in page:
        splits=text_splitter.split(page.page_content)
        for chunk in splits:
            docs.append(chunk)
    embeddings=OllamaEmbeddings(llm=myLlm)
    db=Chroma.from_texts(texts=docs,embeddings=embeddings,persist_directory='db_chroma')
    st.session_state.t5Text=f'共有{len(docs)}筆資料'
    st.write(st.session_state.t5Text)
    st.write('風險評估')
    st.write('風險評估')