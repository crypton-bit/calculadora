import flet as ft

def main(page:ft.Page):
    page.window.width = 400
    page.window.height = 500
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.spacing = 20

    def btn_login(e):(
                
    )

    texto_login = ft.Text(
        value = 'Login',
        size = 32,
        weight='bold',
        color="white"
    )

    email = ft.TextField(
        hint_text= 'email',
        label= 'email',
        width= 250,
        color='white',
        border_color='white',
        label_style= ft.TextStyle(
            color='White'
        )
    )

    
    senha = ft.TextField(
        hint_text= 'senha',
        label= 'senha',
        width=250,
        color='white',
        border_color='white',
        label_style= ft.TextStyle(
            color='white'
        ),
        password=True,
        can_reveal_password=True
    )
    
    confirmar = ft.ElevatedButton(
        text= 'confirmar',
        color = 'white',
        bgcolor='Black',
        width=200,
        height=50,
        on_click=btn_login
    )

    page.add(texto_login, email, senha, confirmar)

ft.app(target=main)