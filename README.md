# PDF to Excel Converter

Este proyecto permite convertir un archivo PDF que contiene descripciones de productos y sus precios a un archivo Excel organizado. Utiliza la librería `pdfplumber` para extraer texto del PDF y `pandas` para estructurarlo en un formato tabular.

---

## Descripción

Este script extrae el texto de un archivo PDF que contiene listas de precios, separando la descripción de los productos y sus respectivos precios. Luego, guarda los datos en un archivo Excel, con cada producto en una fila y dos columnas: una para la descripción y otra para el precio.

El precio se identifica automáticamente mediante una expresión regular que busca valores que comienzan con el signo `$`. Si no se encuentra un precio en la línea, la columna de precio se deja vacía.

---

## Requisitos

Asegúrate de tener las siguientes librerías instaladas:

- `pdfplumber`: Para extraer el texto de los archivos PDF.
- `pandas`: Para estructurar y guardar los datos en un archivo Excel.
- `openpyxl`: Para leer/escribir archivos Excel en formato `.xlsx`.

Puedes instalar estas dependencias utilizando `pip`:

```bash
pip install pdfplumber pandas openpyxl
```

Uso
Paso 1: Clona el repositorio o descarga el script
Si aún no has clonado el repositorio, puedes hacerlo con el siguiente comando:

```bash
git clone <URL-del-repositorio>
cd <nombre-del-repositorio>
```

Paso 2: Coloca tu archivo PDF en la misma carpeta
Asegúrate de que el archivo PDF que quieres procesar esté accesible, y que el nombre del archivo esté correctamente indicado en el script. Cambia la ruta del archivo PDF y el nombre del archivo Excel de salida en las variables pdf_path y excel_path.

Paso 3: Ejecuta el script
Ejecuta el script de la siguiente manera:

```bash
python pdf_to_excel.py
```

El script abrirá el archivo PDF, extraerá el texto y generará un archivo Excel con las columnas "Descripción" y "Precio". El archivo de salida se guardará con el nombre especificado en excel_path.

Ejemplo de Uso
Si tienes un archivo PDF llamado PRECIOS SEPTIEMBRE 2024.pdf, el script lo procesará y generará un archivo PRECIOS_SEPTIEMBRE_2024.xlsx.

```bash
# Ruta del archivo PDF y Excel
pdf_path = "PRECIOS SEPTIEMBRE 2024.pdf"  # Cambia por la ruta completa si es necesario
excel_path = "PRECIOS_SEPTIEMBRE_2024.xlsx"  # Cambia por la ruta completa si es necesario

# Llamada a la función para convertir el PDF a Excel
pdf_to_excel(pdf_path, excel_path)

```

Explicación del Código
pdfplumber: Se utiliza para abrir y extraer el texto de cada página del PDF.
Expresión regular: Se usa para identificar precios que comienzan con el símbolo $.
pandas: Crea un DataFrame con las descripciones y precios, y guarda los resultados en un archivo Excel.
Contribuciones
Si deseas mejorar este proyecto, puedes enviar un pull request con tus cambios. Asegúrate de describir tus modificaciones y pruebas realizadas.

Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
