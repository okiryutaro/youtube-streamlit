import streamlit as st
import time
from PIL import Image

st.title('Streamlit 超入門')

st.write('プログレスバー')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.01)

'Done!!'

left_column,right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の解答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の解答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の解答')

if st.checkbox('Show Image'):
    img = Image.open('IMG_3461.PNG')
    st.image(img,caption='Moriya sisters',use_column_width=True)
text = st.sidebar.text_input('あなたの趣味を教えてください')
condition = st.sidebar.slider('あなたの調子を教えてください',0,100,50)

'あなたの趣味は',text,'です。'
'あなたのコンディションは',condition,'です。'


