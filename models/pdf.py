from typing import List
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Reporte de Pruebas de Métodos de Ordenamiento', 0, 1, 'C')
        self.ln(10)

    def create_table(self, data: List[List[str]], col_widths: List[int], row_height: int, title=""):
        if title:
            self.set_font('Arial', 'B', 12)
            self.cell(0, 10, title, 0, 1, 'C')
            self.ln(4)
        self.set_font('Arial', '', 8)
        for row in data:
            for datum, width in zip(row, col_widths):
                self.cell(width, row_height, str(datum), border=1, align='C')
            self.ln(row_height)

    def add_section_title(self, title):
        self.set_font('Arial', 'B', 10)
        self.cell(0, 10, title, 0, 1, 'C')
        self.ln(4)
        
    def add_to_row(self, table_data: List[List[str]], row_index: int, col_index: int, value: str):
        if row_index < len(table_data) and col_index < len(table_data[row_index]):
            table_data[row_index][col_index] = value
        else:
            print("Índice fuera de rango.")     

    def generalResults(self, list_methods):
        # Datos para la tabla de resultados generales
        header = ["", "", "10 datos", "", "", "100 datos", "", "", "1000 datos", ""]
        sub_header = ["Método de Ordenación", "Mejor Caso", "Caso Promedio", "Peor Caso", "Mejor Caso", "Caso Promedio", "Peor Caso", "Mejor Caso", "Caso Promedio", "Peor Caso"]
        methods = [
            "Burbuja",
            "Insercion",
            "Selección",
            "Vibración",
            "Shell Sort",
            "Quick Sort"
        ]
        empty_rows = [["" for _ in range(len(sub_header))] for _ in methods]

        # Añadiendo los métodos a la primera columna
        for i, method in enumerate(methods):
            empty_rows[i][0] = method

        # Usar un bucle para insertar los datos desde list_methods
        for i, method in enumerate(list_methods):
            self.add_to_row(empty_rows, i, 1, method.getData10().getBetterCase())
            self.add_to_row(empty_rows, i, 2, method.getData10().getAverageCase())
            self.add_to_row(empty_rows, i, 3, method.getData10().getWorseCase())
            self.add_to_row(empty_rows, i, 4, method.getData100().getBetterCase())
            self.add_to_row(empty_rows, i, 5, method.getData100().getAverageCase())
            self.add_to_row(empty_rows, i, 6, method.getData100().getWorseCase())
            self.add_to_row(empty_rows, i, 7, method.getData1000().getBetterCase())
            self.add_to_row(empty_rows, i, 8, method.getData1000().getAverageCase())
            self.add_to_row(empty_rows, i, 9, method.getData1000().getWorseCase())

        # Configuración de las anchuras de las columnas
        w2 = 18
        col_widths = [30, w2, w2, w2, w2, w2, w2, w2, w2, w2]
        row_height = 7
        
        # Resultados generales
        self.set_font('Arial', 'B', 8)
        self.create_table([header], col_widths, row_height)
        self.create_table([sub_header], col_widths, row_height)
        self.set_font('Arial', '', 6)
        self.create_table(empty_rows, col_widths, row_height)

    def makePDF(self, list_methods, name, data_sets):
        self.add_page()
        col_widths = [30, 18, 18, 18, 18, 18, 18, 18, 18, 18]
        row_height = 7

        # Tablas de casos
        for idx, data_set in enumerate(data_sets, start=1):
            title = f"Conjunto de {len(data_set[0])} Elementos"
            self.add_section_title(title)
            for case_type, case_data in zip(["Mejor Caso", "Caso Promedio", "Peor Caso"], data_set):
                formatted_data = [case_type] + [str(x) for x in case_data]
                self.create_table([formatted_data], col_widths, row_height)
            self.ln(10)  

        # Resultados generales de todos los métodos
        self.add_section_title("Resultados Generales de Todos los Métodos")
        self.generalResults(list_methods)

        self.output(f".\\pdf\\{name}.pdf")


