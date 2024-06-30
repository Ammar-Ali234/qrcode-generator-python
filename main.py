import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image

# Set up the Streamlit interface
st.title("QR Code Generator")
st.write("Enter a link to generate a QR code")

# Input for the link
link = st.text_input("Link:")

# Button to generate QR code
if st.button("Generate QR Code"):
    if link:
        # Generate the QR code
        qr_img = qrcode.make(link)
        
        # Convert to PIL image
        qr_img = qr_img.convert("RGB")
        
        # Save the image to a BytesIO object
        img_byte_arr = BytesIO()
        qr_img.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)

        # Display the QR code
        st.image(qr_img, caption="Generated QR Code")
        
        # Add a download button
        st.download_button(
            label="Download QR Code",
            data=img_byte_arr,
            file_name="qr_code.png",
            mime="image/png"
        )
    else:
        st.write("Please enter a link to generate a QR code.")
