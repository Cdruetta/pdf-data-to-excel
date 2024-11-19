import pdfplumber
import pandas as pd
import re

def pdf_to_excel(pdf_path, excel_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            all_data = []

            # Extraer texto de cada página
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    # Dividir el texto en líneas
                    lines = text.split("\n")
                    for line in lines:
                        # Buscar el precio con una expresión regular
                        match = re.search(r'(\$\d+(?:,\d{3})*(?:\.\d{2})?)', line)
                        if match:
                            # Si se encuentra un precio, separarlo
                            description = line[:match.start()].strip()
                            price = match.group(0).strip()
                            all_data.append({"Descripción": description, "Precio": price})
                        else:
                            # Si no hay precio, solo agregar la descripción
                            all_data.append({"Descripción": line, "Precio": None})

        # Crear un DataFrame con las líneas extraídas
        df = pd.DataFrame(all_data)

        # Guardar el DataFrame en un archivo Excel
        df.to_excel(excel_path, index=False)
        print(f"Conversión completada. Archivo guardado en: {excel_path}")

    except Exception as e:
        print(f"Error al convertir el archivo: {e}")

# Ruta del archivo PDF y Excel
pdf_path = "PRECIOS SEPTIEMBRE 2024.pdf"  # Cambia por la ruta completa si es necesario
excel_path = "PRECIOS_SEPTIEMBRE_2024.xlsx" # Cambia por la ruta completa si es necesarioS
pdf_to_excel(pdf_path, excel_path)
