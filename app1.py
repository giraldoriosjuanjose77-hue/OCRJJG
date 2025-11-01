import streamlit as st
import cv2
import numpy as np
import pytesseract
from PIL import Image

st.title("🔠 Reconocimiento Óptico de Caracteres (OCR)")

# --- Selección del método de entrada ---
opcion = st.radio("Selecciona una fuente de imagen:", ("📸 Cámara", "🖼️ Subir imagen"))

# --- Sidebar: filtro ---
with st.sidebar:
    filtro = st.radio("Aplicar filtro", ('Con Filtro', 'Sin Filtro'))

# --- Captura o carga de imagen ---
img_file_buffer = None

if opcion == "📸 Cámara":
    img_file_buffer = st.camera_input("Toma una foto")
elif opcion == "🖼️ Subir imagen":
    img_file_buffer = st.file_uploader("Sube una imagen", type=["jpg", "jpeg", "png"])

# --- Procesamiento de imagen ---
if img_file_buffer is not None:
    # Leer la imagen como arreglo de OpenCV
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    # Aplicar filtro si se selecciona
    if filtro == 'Con Filtro':
        cv2_img = cv2.bitwise_not(cv2_img)

    # Convertir a RGB para mostrar y procesar con pytesseract
    img_rgb = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)

    # Mostrar imagen en pantalla
    st.image(img_rgb, caption="Imagen procesada", use_container_width=True)

    # Extraer texto
    text = pytesseract.image_to_string(img_rgb)

    st.subheader("🧾 Texto Detectado:")
    st.write(text)



