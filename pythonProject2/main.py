import flet as ft

path = ''


def main(page: ft.Page):
    page.title = 'Текстовый редактор'
    page.theme_mode = 'dark'
    page.window.width = 230
    page.window.height = 350
    page.window.resizable = False
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    text_field = ft.TextField(label='Текст файла', width=180, multiline=True)

    def pick_result(e: ft.FilePickerResultEvent):
        if not e.files:
            selected_files.value = 'Ничего невыбрано'
        else:
            selected_files.value = ''
            global path
            for el in e.files:
                path = el.path

            f = open(path, 'r')
            text_field.value = f.read()
            f.close()

        page.update()

    def save_file(e):
        global path
        f = open(path, 'w')
        f.write(text_field.value)
        f.close()

        text_field.value = ''
        save_btn.text = 'Готово'
        page.update()

    pick_dialog = ft.FilePicker(on_result=pick_result)
    page.overlay.append(pick_dialog)
    selected_files = ft.Text()

    save_btn = ft.FilledButton('Сохранить', on_click=save_file)

    page.add(
        ft.Row([ft.Text('Выбор файлов', size=25, weight=500)], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(
            [
                ft.ElevatedButton(
                    'Выбрать файл',
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: pick_dialog.pick_files(allow_multiple=False)
                )
            ]
        ),
        ft.Row([text_field]),
        ft.Row([save_btn]),
        ft.Row([selected_files])
    )


ft.app(target=main)
