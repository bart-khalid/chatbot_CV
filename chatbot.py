import streamlit as st
from PIL import Image

# config
st.set_page_config(
     page_title="BARTAOUCH Khalid Chatbot App",
     page_icon=Image.open("robot.png"),
     layout="wide",
     menu_items={
         'About': "# BARTAOUCH KHALID CHATBOT APP. This is a CHATBOT app!"
     }
 )

import time
from functions import Functions as fct

# function 
def sidebar():
        with st.spinner('Wait for it...'):
            time.sleep(0.2)
            l = st.session_state.conversation_rev
            for i,j in enumerate(l):

                if "--- ***** ---" in j:
                    j = j.split("--- ***** ---")
                    st.sidebar.markdown(f'<p style="color:#B85252">{"Khalid (Bot) : "}</p>', unsafe_allow_html=True)
                    for k in j:
                        st.sidebar.write(k)
                    st.sidebar.write(":heavy_minus_sign:" * 15)
                    continue

                if i%2 == 0:
                    st.sidebar.write(int((len(l)-i)/2))
                    st.sidebar.markdown(f'<p style="color:#B85252">{"You : "}</p>', unsafe_allow_html=True)  
                else :
                    st.sidebar.markdown(f'<p style="color:#B85252">{"Khalid (Bot) : "}</p>', unsafe_allow_html=True)
                        
                st.sidebar.write(j)
                if i%2 != 0:
                    st.sidebar.write(":heavy_minus_sign:" * 15)    
                    
                    
def noConYet():
     if len(st.session_state.conversation)==0 :
          st.sidebar.write("*** No conversation yet ***")
      
# start
st.markdown(f'<h1 style="color:#EA5C2B;text-align: center">{"BARTAOUCH KHALID CHATBOT"}</h1>', unsafe_allow_html=True)

col1, col2 = st.columns([8, 8])
if "conversation" not in st.session_state:
    st.session_state.conversation = []
if "conversation_rev" not in st.session_state:
    st.session_state.conversation_rev = []

with col1:
    with st.spinner('Wait for it...'):
        time.sleep(0.2)
        st.markdown(f'<h3 style="color:#D8B6A4">{"This chatbot is made to let you get any information about me !"}</h3>', unsafe_allow_html=True)
        st.subheader("Hope you'll like it 😄😄")
        st.info("Example of questions you could type (click on any button to see the result)")
        exmple_1 = st.button("Who are you ?")
        exmple_2 = st.button("What are you looking for ?")
        exmple_3 = st.button("What are your projects !")

    
        st.sidebar.header("Conversation history")
        
        clear = st.sidebar.button("Clear Conversation")
        
            


with col2:
    with st.spinner('Wait for it...'):
        time.sleep(0.2)
        fct = fct()
        words, labels, training, output = fct.getData()
        model = fct.getModel()

        st.markdown(f'<h3 style="color:#D8B6A4;text-align: center">{"Start talking ..."}</h3>', unsafe_allow_html=True)
        with st.form(key = "myinp", clear_on_submit = True) :
            inp = st.text_input("Your question :", placeholder="How are you doing ?")
            btn = st.form_submit_button("get answer")
        
        
        
        if(clear):
            inp=''
            with st.spinner('Wait for it...'):
                time.sleep(0.2)
                st.session_state.conversation = []
                st.session_state.conversation_rev = []
              
        

        if (exmple_1):
            inp = "Who are you ?"
        elif(exmple_2):
            inp = "What are you looking for ?"  
        elif(exmple_3):
            inp = "What are your projects !"
 
        if inp != "":
            with st.spinner('Wait for it...'): 
                time.sleep(0.2)
                result = fct.getResponse(model, labels, inp, words)
                st.session_state.conversation.append(inp)
                st.session_state.conversation.append(result)           
                #reversed_conve
                st.session_state.conversation_rev.insert(0, inp)
                st.session_state.conversation_rev.insert(1, result)
                
                for i,j in enumerate(st.session_state.conversation[-2:]):

                    if "--- ***** ---" in j:
                        j = j.split("--- ***** ---")
                        st.markdown(f'<p style="color:#B85252">{"Khalid (Bot) : "}</p>', unsafe_allow_html=True)
                        for k in j:
                            st.write(k)
                        continue

                    if i%2 == 0:
                        st.markdown(f'<p style="color:#B85252">{"You : "}</p>', unsafe_allow_html=True)  
                    else :
                        st.markdown(f'<p style="color:#B85252">{"Khalid (Bot) : "}</p>', unsafe_allow_html=True)  
                    st.write(j)
        sidebar()
        noConYet()
     
                
    
