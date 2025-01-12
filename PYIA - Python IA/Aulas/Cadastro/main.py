import flet as ft

def main(page: ft.Page):
    db = []
    def cadastrarUsuario(e):
        db.append({
            "nome":cadastro.controls[0].value,
        })
        print(db)
    cadastro = ft.Row(controls=[
        ft.TextField(label="Nome"),
        ft.TextField(label="Sobrenome"),
        ft.TextField(label="Idade"),
        ft.ElevatedButton(text="cadastrar", on_click=cadastrarUsuario),
    ])
        
    data = [
        ["João", "Silva", 25],
        ["Maria", "Santos", 30],
        ["Pedro", "Oliveira", 22],
        ["Ana", "Costa", 28]
    ]
    
    table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("First name")),
            ft.DataColumn(ft.Text("Last name")),
            ft.DataColumn(ft.Text("Age")),
        ],
        rows=[
            ft.DataRow(cells=[ft.DataCell(ft.Text(str(cell))) for cell in row])
            for row in data
        ],
    )
    
    page.add(cadastro, table)

ft.app(target=main)