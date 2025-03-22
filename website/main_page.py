import json
from pathlib import Path

from nicegui import ui
from nicegui.element import Element

from . import documentation, example_card, svg
from .examples import examples
from .header import add_head_html, add_header
from .style import example_link, features, heading, link_target, section_heading, subtitle, title
from typing import Optional

SPONSORS = json.loads((Path(__file__).parent / 'sponsors.json').read_text(encoding='utf-8'))

def tips(
    icon: str = 'info',
    content: str = '', 
    element_classes: Optional[str] = 'p-2 bg-blue-100 w-full',
    element_style: Optional[str] = None,
    icon_classes: Optional[str] = 'text-blue-500 text-2xl',
    content_classes: Optional[str] = 'text-black',
    text_center: Optional[bool] = False
    ) -> Element:
    '''
    提示框
    
    :param icon: 图标名称
    :param content: 提示内容
    :param type: 提示类型
    :param icon_classes: 图标的Class (TailwindCSS)
    :param content_classes: 内容样式 (TailwindCSS)
    '''
    with ui.element('div').classes(element_classes).style(element_style) as tips:
        with ui.row(align_items='center'):
            ui.icon(name=icon).classes(icon_classes)
            if text_center: ui.space()
            ui.html(content='<p>' + content + '</p>').classes(content_classes)
            if text_center: ui.space()
    return tips

def create() -> None:
    """Create the content of the main page."""
    ui.context.client.content.classes('p-0 gap-0')
    add_head_html()
    add_header()

    with ui.row().classes('w-full h-screen items-center gap-8 pr-4 no-wrap into-section'):
        svg.face(half=True).classes('stroke-black dark:stroke-white w-[200px] md:w-[230px] lg:w-[300px]')
        with ui.column().classes('gap-4 md:gap-8 pt-32'):
            title('欢迎使用 *NiceGUI* 。')
            subtitle('让任意浏览器即刻成为您Python代码的前端交互界面。') \
                .classes('max-w-[20rem] sm:max-w-[24rem] md:max-w-[30rem]')

            tips(
                icon='info', 
                content='NiceGUI 的非官方中文文档，由 <a href="https://github.com/Yuerchu" target="_blank">@于小丘</a> 发起。如需提交issue、pr，请<a href="https://github.com/Yuerchu/nicegui" target="_blank">点击此处查看</a>', 
                element_classes='p-2 bg-orange-100 w-full', element_style='border-radius: 7px;', icon_classes='text-orange-500 text-2xl', content_classes='text-orange-500', text_center=False)
            
            ui.link(target='#about').classes('scroll-indicator')

    with ui.row().classes('''
            dark-box min-h-screen no-wrap
            justify-center items-center flex-col md:flex-row
            py-20 px-8 lg:px-16
            gap-8 sm:gap-16 md:gap-8 lg:gap-16
        '''):
        link_target('about')
        with ui.column().classes('text-white max-w-4xl'):
            heading('通过按钮、对话框、3D场景及可视化图表等丰富组件 —— 实现与Python代码的实时双向交互操作。')
            with ui.column().classes('gap-2 bold-links arrow-links text-lg'):
                ui.markdown('''
                    NiceGUI 为您封装底层Web开发细节，助您专注核心业务逻辑的Python实现，完美适配：

                    - 机器人控制系统开发
                    - 物联网(IoT)设备管理平台
                    - 智能家居中控系统
                    - 机器学习可视化界面
                    
                    凭借原生硬件兼容特性（支持摄像头/GPIO接口等物联网外设），实现统一代码管理的高效开发范式。
                    <br><br>
                    NiceGUI 提供平滑的学习曲线 —— 新手可快速实现基础功能原型，资深开发者则能通过高阶API进行深度定制。这种双模开发范式实现：简单需求开箱即用，复杂场景灵活扩展。
                    <br><br><br>
                    您可在这些地方获得 NiceGUI ：
                    [PyPI 包](https://pypi.org/project/nicegui/),
                    [Docker 镜像](https://hub.docker.com/r/zauberzeug/nicegui) and on
                    [GitHub](https://github.com/zauberzeug/nicegui).
                ''')
        example_card.create()

    with ui.column().classes('w-full text-lg p-8 lg:p-16 max-w-[1600px] mx-auto'):
        link_target('installation', '-50px')
        section_heading('安装', '快速 *开始*')
        with ui.row().classes('w-full text-lg leading-tight grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-3 gap-8'):
            with ui.column().classes('w-full max-w-md gap-2'):
                ui.html('<em>1.</em>').classes('text-3xl font-bold fancy-em')
                ui.markdown('创建 __main.py__').classes('text-lg')
                with documentation.python_window(classes='w-full h-52'):
                    ui.markdown('''
                        ```python\n
                        from nicegui import ui

                        ui.label('你好 NiceGUI!')

                        ui.run()
                        ```
                    ''')
            with ui.column().classes('w-full max-w-md gap-2'):
                ui.html('<em>2.</em>').classes('text-3xl font-bold fancy-em')
                ui.markdown('安装 与 启动').classes('text-lg')
                with documentation.bash_window(classes='w-full h-52'):
                    ui.markdown('''
                        ```bash
                        pip3 install nicegui
                        python3 main.py
                        ```
                    ''')
            with ui.column().classes('w-full max-w-md gap-2'):
                ui.html('<em>3.</em>').classes('text-3xl font-bold fancy-em')
                ui.markdown('开始享受吧!').classes('text-lg')
                with documentation.browser_window(classes='w-full h-52'):
                    ui.label('你好 NiceGUI!')
        with ui.expansion('或者在 Docker 中运行 main.py ->').classes('w-full gap-2 bold-links arrow-links'):
            with ui.row().classes('mt-8 w-full justify-center items-center gap-8'):
                ui.markdown('''
                    使用我们的 [预构建 Docker 镜像](https://hub.docker.com/repository/docker/zauberzeug/nicegui)
                    您可以在不安装任何包的前提下运行服务。

                    The command searches for `main.py` in in your current directory and makes the app available at http://localhost:8888.
                ''').classes('max-w-xl')
                with documentation.bash_window(classes='max-w-lg w-full h-52'):
                    ui.markdown('''
                        ```bash
                        docker run -it --rm -p 8888:8080 \\
                            -v "$PWD":/app zauberzeug/nicegui
                        ```
                    ''')

    with ui.column().classes('w-full p-8 lg:p-16 bold-links arrow-links max-w-[1600px] mx-auto'):
        link_target('features', '-50px')
        section_heading('特性', '*更精致的* 编程')
        with ui.row().classes('w-full text-lg leading-tight grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-3 gap-8'):
            features('swap_horiz', '交互组件', [
                '[按钮、开关、滑块、输入框等](/documentation/section_controls)',
                '[通知弹窗、对话框及菜单栏](/documentation/section_page_layout)',
                '[支持SVG叠加的交互式图片](/documentation/interactive_image)',
                '网页应用与[原生窗口应用](/documentation/section_configuration_deployment#native_mode)',
            ])
            features('space_dashboard', '布局系统', [
                '[导航栏、选项卡、面板组件](/documentation/section_page_layout)',
                '行列布局/栅格系统/卡片容器',
                '[HTML元素](/documentation/html)与[Markdown渲染](/documentation/markdown)',
                '默认弹性布局',
            ])
            features('insights', '数据可视化', [
                '[图表、流程图、数据表格](/documentation/section_data_elements)，[音视频组件](/documentation/section_audiovisual_elements)',
                '[三维场景渲染](/documentation/scene)',
                '[数据绑定](/documentation/section_binding_properties)直通机制',
                '内置[数据刷新计时器](/documentation/timer)',
            ])
            features('brush', '样式定制', [
                '可配置的[色彩主题系统](/documentation/section_styling_appearance#color_theming)',
                '自定义CSS样式与类名',
                '现代质感设计风格',
                '[Tailwind CSS](https://tailwindcss.com/)智能补全',
            ])
            features('source', '开发支持', [
                '多[页面路由](/documentation/page)管理',
                '代码热重载机制',
                '持久化[用户会话](/documentation/storage)',
                '卓越的[测试框架](/documentation/section_testing)',
            ])
            features('anchor', '技术栈', [
                '通用[Vue](https://vuejs.org/)到Python桥接',
                '基于[Quasar](https://quasar.dev/)的动态GUI',
                '[FastAPI](https://fastapi.tiangolo.com/)服务端架构',
                'Python 3.8+ 环境支持',
            ])
    with ui.column().classes('w-full p-8 lg:p-16 max-w-[1600px] mx-auto'):
        link_target('demos', '-50px')
        section_heading('演示', '试试 *这个*')
        with ui.column().classes('w-full'):
            documentation.create_intro()

    with ui.column().classes('dark-box p-8 lg:p-16 my-16'):
        with ui.column().classes('mx-auto items-center gap-y-8 gap-x-32 lg:flex-row'):
            with ui.column().classes('gap-1 max-lg:items-center max-lg:text-center'):
                ui.markdown('探索丰富的在线演示实例') \
                    .classes('text-white text-2xl md:text-3xl font-medium')
                ui.html('一个有趣的事实：本站点完全由 NiceGUI 构建') \
                    .classes('text-white text-lg md:text-xl')
            ui.link('文档', '/documentation').style('color: black !important') \
                .classes('rounded-full mx-auto px-12 py-2 bg-white font-medium text-lg md:text-xl')

    with ui.column().classes('w-full p-8 lg:p-16 max-w-[1600px] mx-auto'):
        link_target('examples', '-50px')
        section_heading('In-depth examples', 'Pick your *solution*')
        with ui.row().classes('w-full text-lg leading-tight grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-3 gap-4'):
            for example in examples:
                example_link(example)

    with ui.column().classes('dark-box p-8 lg:p-16 my-16 bg-transparent border-y-2'):
        with ui.column().classes('mx-auto items-center gap-y-8 gap-x-32 lg:flex-row'):
            with ui.column().classes('max-lg:items-center max-lg:text-center'):
                link_target('sponsors')
                ui.markdown('NiceGUI is supported by') \
                    .classes('text-2xl md:text-3xl font-medium')
                if SPONSORS['top']:
                    with ui.row(align_items='center'):
                        assert SPONSORS['total'] > 0
                        ui.markdown(f'''
                            our top {'sponsor' if len(SPONSORS['top']) == 1 else 'sponsors'}
                        ''')
                        for sponsor in SPONSORS['top']:
                            with ui.link(target=f'https://github.com/{sponsor}').classes('row items-center gap-2'):
                                ui.image(f'https://github.com/{sponsor}.png').classes('w-12 h-12 border')
                                ui.label(f'@{sponsor}')
                    ui.markdown(f'''
                        as well as {SPONSORS['total'] - len(SPONSORS['top'])} other [sponsors](https://github.com/sponsors/zauberzeug)
                        and {SPONSORS['contributors']} [contributors](https://github.com/zauberzeug/nicegui/graphs/contributors).
                    ''').classes('bold-links arrow-links')
                else:
                    ui.markdown(f'''
                        {SPONSORS['total']} [sponsors](https://github.com/sponsors/zauberzeug)
                        and {SPONSORS['contributors']} [contributors](https://github.com/zauberzeug/nicegui/graphs/contributors).
                    ''').classes('bold-links arrow-links')
            with ui.link(target='https://github.com/sponsors/zauberzeug').style('color: black !important') \
                    .classes('rounded-full mx-auto px-12 py-2 border-2 border-[#3e6a94] font-medium text-lg md:text-xl'):
                with ui.row().classes('items-center gap-4'):
                    ui.icon('sym_o_favorite', color='#3e6a94')
                    ui.label('Become a sponsor').classes('text-[#3e6a94]')

    with ui.row().classes('dark-box min-h-screen mt-16'):
        link_target('why')
        with ui.column().classes('''
                max-w-[1600px] m-auto
                py-20 px-8 lg:px-16
                items-center justify-center no-wrap flex-col md:flex-row gap-16
            '''):
            with ui.column().classes('gap-8'):
                heading('Why?')
                with ui.column().classes('gap-2 text-xl text-white bold-links arrow-links'):
                    ui.markdown('''
                        我们[Zauberzeug](https://zauberzeug.com)团队认可
                        [Streamlit](https://streamlit.io/)
                        的价值，但发现其在
                        [状态管理方面存在过多隐式操作](https://github.com/zauberzeug/nicegui/issues/1#issuecomment-847413651)。
                        在寻求Python图形界面开发的替代方案时，我们发现了
                        [JustPy](https://justpy.io/)。
                        虽然认同其设计理念，但其"底层HTML操作"特性不符合日常开发需求。
                        该框架启发了我们采用
                        [Vue](https://vuejs.org/)
                        与
                        [Quasar](https://quasar.dev/)
                        构建前端体系。
                    ''')
                    ui.markdown('''
                        本框架技术架构基于
                        [FastAPI](https://fastapi.tiangolo.com/)，其底层整合：
                        - ASGI框架[Starlette](https://www.starlette.io/)
                        - 高性能ASGI服务器[Uvicorn](https://www.uvicorn.org/)
                        该组合在保证卓越性能的同时，显著提升开发效率。
                    ''')
            svg.face().classes('stroke-white shrink-0 w-[200px] md:w-[300px] lg:w-[450px]')