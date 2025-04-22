import streamlit as st, datetime 
def form_base():
    myDict={}
    with st.expander('病人基本資料'):
        col1, col2 = st.columns(2)
        with col1:
            myDate=st.date_input('日期',datetime.date.today().strftime('%Y-%m-%d'))
            ptName=st.text_input('姓名','王小明') 
            ptSex=st.pills('性別',['男','女'],selection_mode='single',default='男')
        with col2:
            ptAge=st.number_input('年齡',min_value=1,max_value=100,step=1,value=40)
            ptNo=st.text_input('病歷號',value='6578910')
    if myDate: myDict.update({"日期":myDate})
    if ptName: myDict.update({"姓名":ptName})
    if ptSex: myDict.update({"性別":ptSex})
    if ptAge: myDict.update({"年齡":ptAge})
    if ptNo: myDict.update({"病歷號":ptNo})
    return myDict

def form_physic():
    myDict={}
    with st.expander('病人生理狀況'):
        col1, col2 = st.columns(2)
        with col1:
            ptTemp=st.number_input('體溫',min_value=35.0,max_value=42.0,step=1.0,value=37.5)
            ptPulse=st.number_input('脈搏',min_value=30,max_value=200,step=1,value=80)
            ptResp=st.number_input('呼吸',min_value=10,max_value=40,step=1,value=16)
            ptBP=st.number_input('血壓',min_value=60,max_value=200,step=1,value=120)
        with col2:
            ptHeight=st.number_input('身高',min_value=50,max_value=250,step=1,value=170)
            ptWeight=st.number_input('體重',min_value=10,max_value=200,step=1,value=70)
            ptBMI=st.number_input('BMI',min_value=10.0,max_value=50.0,step=0.1,value=24.2)
            ptPain=st.number_input('疼痛',min_value=0,max_value=10,step=1,value=0)
    if ptTemp: myDict.update({"體溫":ptTemp})
    if ptPulse: myDict.update({"脈搏":ptPulse})
    if ptResp: myDict.update({"呼吸":ptResp})
    if ptBP: myDict.update({"血壓":ptBP})
    if ptHeight: myDict.update({"身高":ptHeight})
    if ptWeight: myDict.update({"體重":ptWeight})
    if ptBMI: myDict.update({"BMI":ptBMI})
    if ptPain: myDict.update({"疼痛":ptPain})
    return myDict  

def form_emotion():
    myDict={}
    with st.expander('病人情緒狀況'):
        ptEmotion=st.pills('情緒種類',['喜悅','憂鬱','焦慮','緊張','恐懼','恐慌','生氣','矛盾','淡漠'],
                           selection_mode='multi',default='憂鬱')
        ptExpress=st.pills('情緒表達',['適當','不適當','混亂'],selection_mode='single',default='適當')
        ptBehavior=st.pills('行為表現',['適當','不適當','畏縮','口語攻擊','肢體攻擊','自我傷害','多疑'],
                            selection_mode='multi',default='適當')
    if ptEmotion: myDict.update({'情緒種類':ptEmotion})
    if ptExpress: myDict.update({'情緒表達':ptExpress})  
    if ptBehavior:myDict.update({'行為表現':ptBehavior})
    return myDict

def form_cognitive():
    myDict={}
    with st.expander('病人認知狀況'):
        ptDelusion=st.pills('妄想',['有','無','不確定'],selection_mode='single',default='無',key='delusion')
        ptDelusions=st.text_input('妄想內容','被害妄想',key='delusions')
        ptHallucination=st.pills('幻覺',['有','無','不確定'],selection_mode='single',default='無', key='hallucination')
        ptHallucinations=st.text_input('幻覺內容','聽到有人叫名字')
        ptThought=st.pills('思維',['正常','混亂','不確定'],selection_mode='single',default='正常')    
        ptConscious=st.pills('意識狀態',['清醒','嗜睡','昏迷'],selection_mode='single',default='清醒')
        ptAttention=st.pills('注意力',['正常','混亂','不確定'],selection_mode='single',default='正常',key='attention') 
        ptJudgement=st.pills('判斷力',['正常','混亂','不確定'],selection_mode='single',default='正常',key='judgement')  
        ptOrientation=st.pills('時間空間定向',['正常','混亂','不確定'],selection_mode='single',default='正常',key='orientation')
        ptMemory=st.pills('記憶力',['正常','混亂','缺失'],selection_mode='single',default='正常')
        ptAbstraction=st.pills('抽象思維',['正常','混亂','不確定'],selection_mode='single',default='正常',key='abstraction')
        ptCalculation=st.pills('計算能力',['正常','混亂','不確定'],selection_mode='single',default='正常',key='calculation')
        ptInsight=st.pills('病識感',['正常','混亂','不確定'],selection_mode='single',default='正常',key='insight')
    if ptDelusion: myDict.update({'妄想':ptDelusion})   
    if ptDelusions: myDict.update({'妄想內容':ptDelusions})
    if ptHallucination: myDict.update({'幻覺':ptHallucination})
    if ptHallucinations: myDict.update({'幻覺內容':ptHallucinations})
    if ptThought: myDict.update({'思維':ptThought}) 
    if ptConscious: myDict.update({'意識狀態':ptConscious})
    if ptAttention: myDict.update({'注意力':ptAttention})
    if ptJudgement: myDict.update({'判斷力':ptJudgement})
    if ptOrientation: myDict.update({'時間空間定向':ptOrientation})
    if ptMemory: myDict.update({'記憶力':ptMemory})
    if ptAbstraction: myDict.update({'抽象思維':ptAbstraction})
    if ptCalculation: myDict.update({'計算能力':ptCalculation})
    if ptInsight: myDict.update({'病識感':ptInsight})
    return myDict

def form_note():
    myDict={}
    with st.expander('病人特別記錄'):
        ptNote=st.text_area('特別記錄','主治醫師指示:靜脈注射生理食鹽水1000cc,每日三次,每次滴注30分鐘。')
    if ptNote: myDict.update({'特別記錄':ptNote})
    return myDict

