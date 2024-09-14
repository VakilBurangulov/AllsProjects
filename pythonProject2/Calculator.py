import numexpr as ne
import flet as ft

example = ''



def main(page: ft.Page):
    global example
    global answer
    page.title = 'Калькулятор'
    page.theme_mode = 'dark'
    page.window.width = 600
    page.window.height = 300

    example_print = ft.Text(f'Example: ')
    answer_print = ft.Text(f'Answer: ')

    answer = ''

    def add_1(e):
        global example
        example += '1'
        example_print.value = f'Example: {example}'
        page.update()

    def add_2(e):
        global example
        example += '2'
        example_print.value = f'Example: {example}'
        page.update()

    def add_3(e):
        global example
        example += '3'
        
        example_print.value = f'Example: {example}'
        page.update()

    def add_4(e):
        global example
        example += '4'
        
        example_print.value = f'Example: {example}'
        page.update()

    def add_5(e):
        global example
        example += '5'
        
        example_print.value = f'Example: {example}'
        page.update()

    def add_6(e):
        global example
        example += '6'
        
        example_print.value = f'Example: {example}'
        page.update()

    def add_7(e):
        global example
        example += '7'
        
        example_print.value = f'Example: {example}'
        page.update()

    def add_8(e):
        global example
        example += '8'
        
        example_print.value = f'Example: {example}'
        page.update()

    def add_9(e):
        global example
        example += '9'
        
        example_print.value = f'Example: {example}'
        page.update()

    def add_0(e):
        global example
        example += '0'
        
        example_print.value = f'Example: {example}'
        page.update()

    def add_sum(e):
        global example
        example += '+'
        
        example_print.value = f'Example: {example}'
        page.update()

    def add_vich(e):
        global example
        example += '-'
        
        example_print.value = f'Example: {example}'
        page.update()

    def add_umno(e):
        global example
        example += '*'
        
        example_print.value = f'Example: {example}'
        page.update()

    def add_del(e):
        global example
        example += '/'
        
        example_print.value = f'Example: {example}'
        page.update()

    def add_otkr(e):
        global example
        example += '('
        
        example_print.value = f'Example: {example}'
        page.update()

    def add_zakr(e):
        global example
        example += ')'
        
        example_print.value = f'Example: {example}'
        page.update()

    def add_rav(e):
        global example
        try:
            answer = ne.evaluate(example)
            answer_print.value = f'Answer: {answer}'
            example = ''
            example_print.value = f'Example: {example}'
            page.update()
        except Exception:
            example = ''
            example_print.value = f'Example: {example}'
            answer_print.value = f'Answer: Ошибка'
            page.update()

    def add_clear(e):
        global example
        example = ''
        example_print.value = f'Example: {example}'
        page.update()

    def add_back(e):
        global example
        example = example[:-1]
        example_print.value = f'Example: {example}'
        page.update()

    page.add(
        ft.Row(
            [
                ft.ElevatedButton(text='1', on_click=add_1),
                ft.ElevatedButton(text='2', on_click=add_2),
                ft.ElevatedButton(text='3', on_click=add_3),
                ft.ElevatedButton(text='+', on_click=add_sum),
                ft.ElevatedButton(text='-', on_click=add_vich),
                example_print

            ]
        ),
        ft.Row(
            [
                ft.ElevatedButton(text='4', on_click=add_4),
                ft.ElevatedButton(text='5', on_click=add_5),
                ft.ElevatedButton(text='6', on_click=add_6),
                ft.ElevatedButton(text='*', on_click=add_umno),
                ft.ElevatedButton(text='/', on_click=add_del),
                answer_print
            ]
        ),
        ft.Row(
            [
                ft.ElevatedButton(text='7', on_click=add_7),
                ft.ElevatedButton(text='8', on_click=add_8),
                ft.ElevatedButton(text='9', on_click=add_9),
                ft.ElevatedButton(text='(', on_click=add_otkr),
                ft.ElevatedButton(text=')', on_click=add_zakr),
            ]
        ),
        ft.Row(
            [
                ft.ElevatedButton(text='0', on_click=add_0),
                ft.ElevatedButton(text='=', on_click=add_rav),
                ft.ElevatedButton(text='C', on_click=add_clear),
                ft.ElevatedButton(text='<--', on_click=add_back),
            ],
        ),
    )


ft.app(target=main)
