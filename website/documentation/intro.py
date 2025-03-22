from typing import Callable

from nicegui import ui

from ..style import subheading
from .demo import demo


def create_intro() -> None:
    @_main_page_demo('Styling', '''
        While having reasonable defaults, you can still modify the look of your app with CSS as well as Tailwind and Quasar classes.
    ''')
    def formatting_demo():
        ui.icon('thumb_up')
        ui.markdown('这是一段 **Markdown**.')
        ui.html('这是一段 <strong>HTML</strong>.')
        with ui.row():
            ui.label('CSS').style('color: #888; font-weight: bold')
            ui.label('Tailwind').classes('font-serif')
            ui.label('Quasar').classes('q-ml-xl')
        ui.link('Github 上的 NiceGUI', 'https://github.com/zauberzeug/nicegui')

    @_main_page_demo('Common UI Elements', '''
        NiceGUI comes with a collection of commonly used UI elements.
    ''')
    def common_elements_demo():
        from nicegui.events import ValueChangeEventArguments

        def show(event: ValueChangeEventArguments):
            name = type(event.sender).__name__
            ui.notify(f'{name}: {event.value}')

        ui.button('按钮', on_click=lambda: ui.notify('点击了按钮'))
        with ui.row():
            ui.checkbox('选择器', on_change=show)
            ui.switch('开关', on_change=show)
        ui.radio(['A', 'B', 'C'], value='A', on_change=show).props('inline')
        with ui.row():
            ui.input('文本输入框', on_change=show)
            ui.select(['One', 'Two'], value='One', on_change=show)
        ui.link('还有更多...', '/documentation').classes('mt-8')

    @_main_page_demo('Value Binding', '''
        Binding values between UI elements and data models is built into NiceGUI.
    ''')
    def binding_demo():
        class Demo:
            def __init__(self):
                self.number = 1

        demo = Demo()
        v = ui.checkbox('visible', value=True)
        with ui.column().bind_visibility_from(v, 'value'):
            ui.slider(min=1, max=3).bind_value(demo, 'number')
            ui.toggle({1: 'A', 2: 'B', 3: 'C'}).bind_value(demo, 'number')
            ui.number().bind_value(demo, 'number')


def _main_page_demo(title: str, explanation: str) -> Callable:
    def decorator(f: Callable) -> Callable:
        subheading(title)
        ui.markdown(explanation).classes('bold-links arrow-links')
        return demo(f)
    return decorator
