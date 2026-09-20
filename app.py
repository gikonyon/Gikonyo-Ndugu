import io
from PIL import Image
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image as RLImage, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

# ---------- Contact ----------
elif page == "Contact":
    st.title("📬 Contact & Digital Business Card")
    st.write("I take on consulting retainers, project-based builds, and institutional advisory partnerships.")

    st.markdown("---")

    # On-Screen Card Display
    col_photo, col_details, col_qr = st.columns([1.2, 2.5, 1.3])

    with col_photo:
        st.image("Gikonyo.jfif", use_container_width=True)

    with col_details:
        st.markdown("## **Gikonyo Ndugu**")
        st.markdown("**Solutions Provider — Development Finance, ESG & Digital Tools**")
        st.markdown("📍 Nairobi, Kenya")
        st.markdown("📧 [Ndugu.Gikonyo@hotmail.com](mailto:Ndugu.Gikonyo@hotmail.com)")
        st.markdown("📱 [+254 723 462 232](tel:+254723462232)")
        st.markdown("🔗 [linkedin.com/in/gikonyo-ndugu](https://linkedin.com/in/gikonyo-ndugu)")

    with col_qr:
        st.image("QR CODE GIKONYO.jpg", use_container_width=True, caption="Scan for Live Portfolio")

    st.markdown("---")

    # Function to generate Business Card PDF in memory
    def generate_pdf_card():
        buffer = io.BytesIO()
        
        # Standard card dimensions scaled for high-res PDF display (3.5" x 2" proportions)
        doc = SimpleDocTemplate(
            buffer,
            pagesize=(3.5 * inch, 2.2 * inch),
            rightMargin=0.1 * inch,
            leftMargin=0.1 * inch,
            topMargin=0.1 * inch,
            bottomMargin=0.1 * inch
        )

        styles = getSampleStyleSheet()
        
        name_style = ParagraphStyle(
            'NameStyle',
            parent=styles['Normal'],
            fontName='Helvetica-Bold',
            fontSize=8,
            leading=9,
            textColor=colors.HexColor("#1A1A1A")
        )
        
        title_style = ParagraphStyle(
            'TitleStyle',
            parent=styles['Normal'],
            fontName='Helvetica-Bold',
            fontSize=5.5,
            leading=7,
            textColor=colors.HexColor("#0056B3")
        )
        
        body_style = ParagraphStyle(
            'BodyStyle',
            parent=styles['Normal'],
            fontName='Helvetica',
            fontSize=5,
            leading=6.5,
            textColor=colors.HexColor("#444444")
        )

        # Convert images for ReportLab table layout
        img_photo = RLImage("Gikonyo.jfif", width=0.65 * inch, height=0.65 * inch)
        img_qr = RLImage("QR CODE GIKONYO.jpg", width=0.65 * inch, height=0.65 * inch)

        details_text = [
            Paragraph("<b>GIKONYO NDUGU</b>", name_style),
            Paragraph("Solutions Provider", title_style),
            Paragraph("Dev Finance | ESG | Digital Tools", body_style),
            Spacer(1, 2),
            Paragraph("📍 Nairobi, Kenya", body_style),
            Paragraph("📧 Ndugu.Gikonyo@hotmail.com", body_style),
            Paragraph("📱 +254 723 462 232", body_style),
            Paragraph("🔗 linkedin.com/in/gikonyo-ndugu", body_style)
        ]

        data = [[img_photo, details_text, img_qr]]

        table = Table(data, colWidths=[0.75 * inch, 1.8 * inch, 0.75 * inch])
        table.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('ALIGN', (0, 0), (0, 0), 'CENTER'),
            ('ALIGN', (2, 0), (2, 0), 'CENTER'),
            ('LEFTPADDING', (0, 0), (-1, -1), 2),
            ('RIGHTPADDING', (0, 0), (-1, -1), 2),
            ('TOPPADDING', (0, 0), (-1, -1), 2),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
            ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor("#0056B3")),
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#FAFAFA")),
        ]))

        elements = [table]
        doc.build(elements)
        buffer.seek(0)
        return buffer

    # Download Button
    try:
        pdf_data = generate_pdf_card()
        st.download_button(
            label="📥 Download Business Card (PDF)",
            data=pdf_data,
            file_name="Gikonyo_Ndugu_Business_Card.pdf",
            mime="application/pdf"
        )
    except Exception as e:
        st.info("Make sure 'reportlab' and 'Pillow' are added to your Requirements.txt file.")
