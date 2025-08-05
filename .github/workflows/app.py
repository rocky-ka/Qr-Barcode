import streamlit as st
import qrcode
from io import BytesIO
from barcode import Code128
from barcode.writer import ImageWriter
from PIL import Image

st.set_page_config(page_title="QR & Barcode Generator", layout="centered")
st.title("📦 QR Code & Barcode Generator")

Input form
data = st.text_input("Enter the text/data:")

if st.button("Generate"):
    if data:
        # Generate QR Code
        qr_img = qrcode.make(data)
        qr_buf = BytesIO()
        qr_img.save(qr_buf, format="PNG")
        st.subheader("🔳 QR Code")
        st.image(qr_buf.getvalue())

        # Generate Barcode
        barcode_img = Code128(data, writer=ImageWriter())
        barcode_buf = BytesIO()
        barcode_img.write(barcode_buf)
        st.subheader("📊 Barcode")
        st.image(barcode_buf.getvalue())

        st.success("QR Code and Barcode generated successfully!")
    else:
        st.warning("Please enter some data to generate.")
