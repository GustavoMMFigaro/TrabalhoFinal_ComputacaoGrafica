import numpy as np
import streamlit as st
from PIL import Image

st.title("Trabalho Final - Computação Gráfica")
img = np.array(Image.open("Imagem/Monarca.png").convert("RGB"))
h, w, _ = img.shape
st.image(img, caption="Original")

st.header("5 - Canais")
canal = st.selectbox("Canal colorido", ["R", "G", "B"])
i = "RGB".index(canal)
cor = np.zeros_like(img)
cor[:, :, i] = img[:, :, i]
c1, c2, c3, c4 = st.columns(4)
c1.image(img[:, :, 0], caption="R")
c2.image(img[:, :, 1], caption="G")
c3.image(img[:, :, 2], caption="B")
c4.image(cor, caption=canal)

st.header("6 - Troca de canais")
r = st.selectbox("Canal para o R", ["R", "G", "B"], index=0)
g = st.selectbox("Canal para o G", ["R", "G", "B"], index=1)
b = st.selectbox("Canal para o B", ["R", "G", "B"], index=2)
troca = img[:, :, ["RGB".index(r), "RGB".index(g), "RGB".index(b)]]
st.image(troca)

st.header("10 - Negativo numa região")
lado = st.slider("Lado do quadrado", 1, min(w, h), min(w, h) // 3)
x = st.slider("X do quadrado", 0, w - lado, 0)
y = st.slider("Y do quadrado", 0, h - lado, 0)
neg = img.copy()
neg[y:y + lado, x:x + lado] = 255 - neg[y:y + lado, x:x + lado]
st.image(neg)

st.header("17 - Selo em pixels")
cores = np.array([[255, 0, 0], [255, 255, 0], [0, 0, 255]], dtype=np.uint8)
mapa = np.array([
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 2, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
])
escala = st.slider("Escala do selo", 1, min(w, h) // 5 - 1, 20)
selo = np.repeat(np.repeat(cores[mapa], escala, axis=0), escala, axis=1)
sh, sw, _ = selo.shape
sx = st.slider("X do selo", 0, w - sw, 0)
sy = st.slider("Y do selo", 0, h - sh, 0)
foto = img.copy()
foto[sy:sy + sh, sx:sx + sw] = selo
st.image(foto)

st.header("20 - Pixel art")
passo = st.slider("Passo", 1, 50, 10)
pequena = img[::passo, ::passo]
arte = np.repeat(np.repeat(pequena, passo, axis=0), passo, axis=1)[:h, :w]
st.image(arte)
