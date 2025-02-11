# import PyMuPDF  # PyMuPDF
import pandas as pd
import matplotlib.pyplot as plt
import cv2

# Open the PDF file
pdf_document = "PR157.pdf"
doc = fitz.open(pdf_document)

# Iterate through each page
for page_num in range(len(doc)):
    page = doc.load_page(page_num)
    text = page.get_text("text")
    
    # Extract tables (assuming tables are in a structured text format)
    tables = pd.read_html(text)
    
    for i, table in enumerate(tables):
        # Save each table as an image
        fig, ax = plt.subplots()
        ax.axis('tight')
        ax.axis('off')
        ax.table(cellText=table.values, colLabels=table.columns, loc='center')
        plt.savefig(f"table_page{page_num+1}_table{i+1}.png")
        plt.close(fig)
