## streamlit 
# Webpages for ml and data science projects
# python lib
# no requirements of html and css
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st  
import altair as alt
#page configuration
st.set_page_config(page_title='Streamlit function demo',
                     page_icon='😁',
                     layout='centered',)


## title and  text elements
st.title('Hello World')
st.header('1. Text elements')
st.subheader('markdown,code,latex')
st.markdown('**bold text**,*italic tect*,`code`text')
st.code("print('Hello everyone')",language="python")
st.latex(r"a^2+b^2=c^2")

st.divider()

##metrics and messages
st.header("2. Metrics and messages")
st.metric(label="Revenue", value=1234, delta="10%",delta_color="inverse")
st.error("This is an error message")
st.warning("This is a warning message")
st.info("This is an info message")
st.success("This is a success message")
st.exception(ValueError("This is an exception message"))

st.divider()

##data display

st.header("3. Data display")
df =pd.DataFrame(np.random.randn(10, 2), columns=["a", "b"])
st.dataframe(df)
st.table(df.head(3))
st.json(df.to_dict())

st.divider()

##chart
st.header("4. Chart")
#df = pd.DataFrame(np.random.randn(10, 2), columns=["a", "b"])
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)
chart = alt.Chart(df.reset_index()).mark_line().encode(x='index', y='a')
st.altair_chart(chart, use_container_width=True)
fig , ax = plt.subplots()
ax.plot(df.index,df.a)
st.pyplot(fig)
st.divider()

#widgets
st.header("5. Widgets")
with st.form("Input Form"):
    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age") 
    mood = st.radio("Select your mood",("happy","sad","angry"))
    languages = st.multiselect("Select your languages",("English","French","Spanish"))
    submit = st.form_submit_button("submit")
    if submit :
        st.success(f"Name :{name}, Age :{int(age)}, Mood : {mood}, Languages : {languages}" )


col1 , col2 , col3 = st.columns([4,1,1])
with col1:
    st.text_input("Enter your name")
    st.number_input("Enter your age")
with col2:
    st.radio("Select your mood",("happy","sad","angry"))
    st.multiselect("Select your languages",("English","French","Spanish"))
with col3:
    st.title("Output")    


## we can divide from multiple columns
# for that first define form then define columns
# with st.form("input form")
#    col1 , col2 , col3 = st.columns([4,1,1])
#    with col1:
#     name = st.text_input("Enter your name")
#     age = st.number_input("Enter your age") 
#     mood = st.radio("Select your mood",("happy","sad","angry"))
#     languages = st.multiselect("Select your languages",("English","French","Spanish"))
#     submit = st.form_submit_button("submit")
#     if submit :
#         st.success(f"Name :{name}, Age :{int(age)}, Mood : {mood}, Languages : {languages}" )



col1, col2 = st.columns(2)
with col1:
    number = st.slider("Select a number ",0,100)
with col2:
    colour = st.color_picker("Select a color", "#DC8080")  


st.text_area("Enter your text here")
st.date_input("Select a date")
st.time_input("Select a time")
st.file_uploader("Upload a file")

## Media Related
st.header("6. Media Related")
st.image("https://picsum.photos/400",caption="random image")
st.video("https://www.youtube.com/watch?v=9bZkp7q19f0")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

## Sidebar  and layout
st.sidebar.header("Sidebar")
st.sidebar.write("Enter your name")
st.sidebar.button("click me")
option = st.sidebar.selectbox("select an option",("option 1","option 2","option 3"))














## file handling
## generator and deco
## multithreading and multiprocessing
## method overloading and overriding
## debug and unit testing



