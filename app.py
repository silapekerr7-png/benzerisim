import streamlit as st
import pandas as pd
import pickle

st.title("Benzer İsim Öneri Sistemi :sparkles:")
nn=pickle.load(open('isim_nn.pkl','rb'))
oran=pickle.load(open('isim_oran.pkl','rb'))

isim=st.selectbox('Beğendiğiniz isim',sorted(oran.index.tolist()))
n=st.slider('Kaç öneri?',1,10,5)
if st.button('Öner'):
    idx=list(oran.index).index(isim)
    uzaklik,indeks=nn.kneighbors(oran.iloc[[idx]].values,n_neighbors=int(n)+1)
    sonuc=pd.DataFrame({'isim':oran.index[indeks[0][1:]],'benzerlik':(1-uzaklik[0][1:]).round(3)})
    st.write(sonuc)
    st.line_chart(oran.loc[[isim]+sonuc['isim'].tolist()].T)
