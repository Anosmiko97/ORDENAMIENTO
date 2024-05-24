from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

# Crear un documento PDF
pdf = SimpleDocTemplate(".\\pdf\\tabla.pdf", pagesize=letter)

# Datos para la tabla
data = [
    ["ID", "Nombre", "Edad", "Ciudad"],
    [1, "Juan", 28, "Madrid"],
    [2, "Ana", 22, "Barcelona"],
    [3, "Pedro", 35, "Valencia"],
    [4, "Lucía", 30, "Sevilla"]
]

# Crear una tabla
table = Table(data)

# Estilo para la tabla
style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 14),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black)
])

# Aplicar el estilo a la tabla
table.setStyle(style)

# Construir el PDF
elements = [table]
pdf.build(elements)

print("PDF creado con éxito.")
