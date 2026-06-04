import os
from openai import OpenAI
import streamlit as st
import datetime
import json
import pandas as pd
st.set_page_config(#页面配置项
    page_title="BWM introduction",#网站域名
    page_icon="❄️",#网站图标
    layout="centered",#布局(wide占满,centered居中,None不设置默认剧中)
    initial_sidebar_state="expanded",#侧边栏默认展开(可手动收起,auto默认,collapsed默认收起)
    menu_items={#右上角三个点中选项及展示的内容
        "Get Help":"https://www.bmwusa.com/home.html",
        "About":"This is a website introducing BMW."})
st.title("BMW 宝马")#标题
st.header("'have your friends arrange one for you!'")#二级标题
#st.subheader("三级标题")
st.write("Are there any friends willing to arrange it for you?:")#加入文字
#a=st.radio("是否有朋友愿意给你安排一辆",["是","否"])#按钮,index=1索引为1的位置默认勾选
if st.checkbox("Yes"):#选择了这项才会有if下面语句的显示
    st.text_input("The friend's name is:",type="password")#让用户输入的内容,类型为密码
    st.write("Congratulations! You has a very good friend")
elif st.checkbox("No"):
    st.write("Relying on others is not as good as relying on yourself. Keep it up!")
st.image("resource/picture.jpg")#加入图片
#st.audio("resource/audio.mp3")#加入音频
st.video("resource/video.mp4")#加入视频
df=pd.read_csv("resource/excel.csv",encoding="utf-8")
#st.table(df)#加入静态表格
st.dataframe(df)#加入动态表格
st.logo("resource/logo.png")#加入logo
prompt=st.chat_input("What do you want to consult?")#消息输入框(提示信息)
if "DEEPSEEK_API_KEY" not in os.environ:
    if prompt is not None:
        @st.dialog("tips",width="large")#全屏显示
        def full_screen_tip():
            st.write("To use AI,first add deepseek's API key to the environment variables.The steps are as follows")
            st.write("First,deposit 1 yuan on deepseek's API open platform and create an API key")
            st.write("Press the Win key on your keyboard (or click the bottom left corner) to search for 'Edit System Environment Variables',"
                     "then click 'Environment Variables' in the bottom right,"
                     "and finally click 'New'")
            st.write("variable name:DEEPSEEK_API_KEY")
            st.write("variable value:your own API key")
            st.write("Please restart your computer for the environment variable to take effect")
            if st.button("OK"):
                st.rerun()
        full_screen_tip()
else:
    client=OpenAI(
        api_key=os.environ.get("DEEPSEEK_API_KEY"),
        base_url="https://api.deepseek.com")
    def save_session():#定义函数,保存数据至文件夹中
        if st.session_state.current_session:#是否存在该时间
            session_data={
                "messages":st.session_state.messages,
                "nick_name":st.session_state.nick_name,
                "nature":st.session_state.nature,
                "current_session":st.session_state.current_session}#保存所有数据
            if not os.path.exists("sessions"):
                os.mkdir("sessions")#判断sessions是否存在,不存在则创建
            with open(f"sessions/{st.session_state.current_session}.json","w",encoding="utf-8") as t:
                json.dump(session_data,t,ensure_ascii=False,indent=4)#数据保存至sessions文件夹中
    def get_session():#定义函数,展示会话
        session_list=[]
        if os.path.exists("sessions"):#判断是否存在该文件夹
            file_list=os.listdir("sessions")#获取sessions文件夹下的所有文件名
            for filename in file_list:
                if filename.endswith(".json"):#判断是否是json后缀文件
                    session_list.append(filename[:-5])
        session_list.sort(reverse=True)#降序排序
        return session_list
    def load_session(session_name):#定义函数,加载会话
        try:
            if os.path.exists(f"sessions/{session_name}.json"):
                with open(f"sessions/{session_name}.json", "r", encoding="utf-8") as f:
                    session_data=json.load(f)
                    st.session_state.messages=session_data["messages"]
                    st.session_state.nick_name=session_data["nick_name"]
                    st.session_state.nature=session_data["nature"]
                    st.session_state.current_session=session_data["current_session"]
        except Exception:
            st.error("Session load failed;the session file does not exist or is corrupted")
    def delete_session(session_name):#定义函数,删除会话
        try:
            if os.path.exists(f"sessions/{session_name}.json"):
                os.remove(f"sessions/{session_name}.json")#删除会话
                if session_name==st.session_state.current_session:
                    st.session_state.messages=[]
                    st.session_state.current_session=datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        except Exception:
            st.error("the session does not exist and the deletion fails")
    if "messages" not in st.session_state:
        st.session_state.messages=[]#初始化(默认)
    if "nick_name" not in st.session_state:
        st.session_state.nick_name="BrotherMa"#默认名字
    if "nature" not in st.session_state:
        st.session_state.nature="A salesperson involved in every aspect but focused on BMW's various parameters"#默认性格
    if "current_session" not in st.session_state:
        now=datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")#格式化时间
        st.session_state.current_session=now
    with st.sidebar:#左侧边栏
        if st.button("create a new conversation",width="stretch",icon="✏️"):#判断是否点击按钮(按钮内容,布局("stretch"占满),内容前的符号)
            save_session()
            if st.session_state.messages:#如果消息非空,则创建新会话
                st.session_state.messages=[]
                st.session_state.current_session=datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
                save_session()
                st.rerun()#重新加载当前页面
        st.text("conversation history")
        session_list=get_session()
        for session in session_list:
            col1,col2=st.columns([4,1])#将一行进行分割(4、1分)
            with col1:
                if st.button(session,width="stretch",icon="📄",type="primary" if session==st.session_state.current_session else "secondary"):#加载会话(type显示的类型(primary高亮,secondary普通))
                    load_session(session)
                    st.rerun()
            with col2:
                if st.button("",width="stretch",icon="❌",key=f"delete_{session}"):#删除会话(key为设置唯一标识,，欸个按钮的内容不能相同)
                    delete_session(session)
                    st.rerun()
        st.divider()#分割线
        st.subheader("AI information")
        nick_name=st.text_input("name",placeholder="please enter the nickname of the AI intelligence",value=st.session_state.nick_name)#AI昵称(名字,提示信息,填充的内容)
        if nick_name:
            st.session_state.nick_name=nick_name
        nature=st.text_area("system prompt",placeholder="please enter the personality of the AI intelligence",value=st.session_state.nature)#AI性格
        if nature:
            st.session_state.nature=nature
    st.text(f"conversation information:{st.session_state.current_session}")
    for message in st.session_state.messages:
        st.chat_message(message["role"]).write(message["content"])#展示聊天信息(信息来源名称,展示的信息)
    if prompt:
        st.chat_message("user").write(prompt)#展示提示词
        print("提示词",prompt)
        st.session_state.messages.append({"role":"user","content":prompt})#保存提示词
        response = client.chat.completions.create(
            model="deepseek-v4-pro",
            messages=[
                {"role": "system", "content":f"you are {st.session_state.nick_name},your role is {st.session_state.nature}"},
                *st.session_state.messages],
            stream=True,
            reasoning_effort = "high",
            extra_body = {"thinking": {"type": "enabled"}})
        response_message=st.empty()#建造空容器(流式输出)
        full_response=""
        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                content=chunk.choices[0].delta.content
                full_response+=content
                response_message.chat_message("assistant").write(full_response)#展示大模型返回的信息
        #print("大模型返回的结果",response.choices[0].message.content)
        #st.chat_message("assistant").write(response.choices[0].message.content)#非流式输出
        st.session_state.messages.append({"role": "assistant", "content":full_response})#保存大模型返回的信息
        save_session()