from nicegui import ui

from . import (
    doc,
    section_action_events,
    section_audiovisual_elements,
    section_binding_properties,
    section_configuration_deployment,
    section_controls,
    section_data_elements,
    section_page_layout,
    section_pages_routing,
    section_styling_appearance,
    section_testing,
    section_text_elements,
)
from ...style import subheading

doc.title('*NiceGUI* 文档', '特性, 演示 以及 其他')

doc.text('概览', '''
    NiceGUI 是一款开源的Python图形界面库，支持在浏览器中运行交互界面。其学习曲线平缓，同时提供高级定制选项。采用后端优先设计理念，封装所有Web开发细节，开发者可专注Python代码编写。适用于多种项目类型：

    - 轻量脚本开发
    - 数据可视化仪表盘
    - 机器人控制系统
    - 物联网(IoT)解决方案
    - 智能家居中控平台
    - 机器学习交互界面
''')

doc.text('使用指南', '''
    本文档系统阐述NiceGUI使用方法，各功能模块独立成章。建议阅读顺序：
    
    1. 通读本导言章节
    2. 按需查阅具体功能模块
    3. 实践时参考API文档
''')

doc.text('核心概念', '''
    NiceGUI 提供标准化UI组件生态：

    - **基础控件**：按钮/滑块/文本/图像等
    - **数据可视化**：图表/流程图/3D场景
    - **页面架构**：通过代码声明式构建布局
    
    交互机制实现：

    - **事件驱动模型**：用户操作触发事件响应
    - **数据绑定系统**：模型变更自动更新UI
    - **异步任务处理**：保持界面响应流畅
    
    布局构建特色：
    ```python
    with ui.card():  # 声明式布局构造器
        ui.label('卡片内容')
        with ui.row():  # 行式布局容器
            ui.button('确认')
            ui.button('取消')
    ```
    该语法源自Flutter/SwiftUI范式，通过Python上下文管理器实现代码与UI的视觉对应。
''')

doc.text('事件与异步', '''
    NiceGUI采用异步事件循环架构：
    - 单线程事件驱动，确保线程安全
    - 支持定时任务/键盘事件等并发处理
    - 提供异步任务封装器保持UI响应
    
    重要原则：
    - 所有UI更新必须在主线程执行
    - 长时间任务需使用`async`函数处理
''')

doc.text('技术实现', '''
    架构分层：
    1. **前端渲染**：基于Vue/Quasar组件库
    2. **通信协议**：WebSocket双向数据绑定
    3. **服务引擎**：FastAPI + Starlette + Uvicorn
    4. **部署模式**：支持浏览器/原生窗口/服务器多形态
    
    开发者无需掌握HTML即可构建现代Web应用，框架自动处理：
    - DOM操作优化
    - 浏览器兼容性
    - 响应式布局适配
''')

doc.text('应用部署', '''
    部署方案选择：

    - 🖥️ 本地开发模式：`ui.run(local=True)`
    - 🪟 原生窗口模式：`ui.run(native=True)`
    - 🌐 服务器部署：`ui.run(host='0.0.0.0')`
    
    关键配置参数：

    ```python
    ui.run(
        port=8080,           # 服务端口
        reload=True,         # 热重载开关
        window_size=(1024,768),  # 初始窗口尺寸
        uvicorn_log_level='info'  # 日志级别
    )
    ```

    详见《配置与部署》章节。
''')

doc.text('深度定制', '''
    扩展能力三层次：

    1. **样式定制**：
       - Tailwind原子类 `.classes('bg-blue-500')`
       - Quasar属性 `.props('dense outlined')`
       - 自定义CSS注入
    2. **组件扩展**：
       - 继承现有组件实现定制逻辑
       - 导入Quasar原生组件
    3. **架构整合**：
       - 与FastAPI中间件深度集成
       - 支持WebSocket自定义路由
''')

doc.text('测试体系', '''
    双模测试方案：
    - 🚀 **高效单元测试**（user fixture）：
      ```python
      def test_login(user: User):
          user.click(login_button)
          assert user.find('欢迎管理员')
      ```
      执行速度：毫秒级/用例
    
    - 🌐 **端到端测试**（screen fixture）：
      ```python
      def test_browser_compatibility(screen: Screen):
          screen.open('/')
          screen.assert_contains('初始化完成')
      ```
      覆盖真实浏览器行为
''')

tiles = [
    (section_text_elements, '''
        类似 `ui.label`, `ui.markdown`, `ui.restructured_text` 以及 `ui.html` 等可以被用来显示文字的元素。
    '''),
    (section_controls, '''
        NiceGUI 为用户交互提供了多种元素，比如 `ui.button`, `ui.slider`, `ui.inputs` 等等。
    '''),
    (section_audiovisual_elements, '''
        您可以使用诸如 `ui.image`, `ui.audio`, `ui.video`, 之类的元素来展示视听内容。
    '''),
    (section_data_elements, '''
        有些元素用来展示数据，例如 `ui.table`, `ui.aggrid`, `ui.highchart`, `ui.echart` 等等。
    '''),
    (section_binding_properties, '''
        为了自动更新 UI 元素, 您可以把他们绑定到其他任何元素或者您的数据模型上。
    '''),
    (section_page_layout, '''
        本节介绍基本技术以及构建 UI 的几个元素。
    '''),
    (section_styling_appearance, '''
        NiceGUI 允许以各种方式自定义 UI 元素的外观，包括 CSS、Tailwind CSS 和 Quasar 属性。
    '''),
    (section_action_events, '''
        本节介绍计时器、UI 事件和 NiceGUI 应用程序的生命周期。
    '''),
    (section_pages_routing, '''
        一个 NiceGUI 应用程序可以由多个页面和其他 FastAPI 端点组成。
    '''),
    (section_configuration_deployment, '''
        无论您是想在本地还是在服务器上运行应用程序，在本地还是在浏览器中运行应用程序，我们都能满足您的需求。
    '''),
    (section_testing, '''
        编写自动化 UI 测试，这些测试在无头浏览器中运行（慢速）或在 Python 中完全模拟（快速）。
     '''),
]


@doc.extra_column
def create_tiles():
    with ui.row(align_items='center').classes('items-center content-between'):
        ui.label('如果你喜欢 NiceGUI ，欢迎前往并成为')
        ui.button(text='赞助者', on_click=lambda: ui.navigate('https://github.com/sponsors/zauberzeug')).props('flat')
    for documentation, description in tiles:
        page = doc.get_page(documentation)
        with ui.link(target=f'/documentation/{page.name}') \
                .classes('bg-[#5898d420] p-4 self-stretch rounded flex flex-col gap-2') \
                .style('box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1)'):
            if page.title:
                ui.label(page.title.replace('*', '')).classes(replace='text-2xl')
            ui.markdown(description).classes(replace='bold-links arrow-links')


@doc.ui
def map_of_nicegui():
    ui.separator().classes('mt-6')
    subheading('NiceGUI 地图', anchor_name='map-of-nicegui')
    ui.add_css('''
        .map-of-nicegui a code {
            font-weight: bold;
        }
    ''')
    ui.markdown('''
        本概览展示了NiceGUI的结构，
        它是NiceGUI命名空间及其内容的地图。
        虽然并不详尽，但能很好地帮助您了解可用的功能。
        我们持续的目标是使这张地图更加完整，并为文档添加缺失的链接。

        #### `ui`

        运行 NiceGUI 应用所需的 UI 元素及其他基本组件。

        - [`ui.element`](/documentation/element): 所有元素的基类
            - customization:
                - `.props()` 和 [`.default_props()`](/documentation/element#default_props): 添加 Quasar props 以及默认 HTML attributes
                - `.classes()` 和 [`.default_classes()`](/documentation/element#default_classes): 添加 Quasar, Tailwind 和 自定义 HTML 类
                - [`.tailwind`](/documentation/section_styling_appearance#tailwind_css): convenience API for adding Tailwind classes
                - `.style()` 和 [`.default_style()`](/documentation/element#default_style): 添加 CSS 样式定义
                - [`.tooltip()`](/documentation/tooltip): 向元素中添加 Tooltip 提示
                - [`.mark()`](/documentation/element_filter#markers): 标记元素 for querying with an [ElementFilter](/documentation/element_filter)
            - interaction:
                - [`.on()`](/documentation/generic_events): 添加 Python 和 JavaScript 事件钩子
                - `.update()`: 向客户端发送更新元素命令 (在大多数情况下会自动完成)
                - `.run_method()`: 在客户端执行方法
                - `.get_computed_prop()`: get the value of a property that is computed on the client side
            - hierarchy:
                - `with ...:` nesting elements in a declarative way
                - `__iter__`: an iterator over all child elements
                - `ancestors`: an iterator over the element's parent, grandparent, etc.
                - `descendants`: an iterator over all child elements, grandchildren, etc.
                - `slots`: a dictionary of named slots
                - `add_slot`: fill a new slot with NiceGUI elements or a scoped slot with template strings
                - [`clear`](/documentation/section_page_layout#clear_containers): remove all child elements
                - [`move`](/documentation/element#move_elements): move an element to a new parent
                - `remove`: remove a child element
                - `delete`: delete an element and all its children
                - `is_deleted`: whether an element has been deleted
        - 元素:
            - [`ui.aggrid`](/documentation/aggrid)
            - [`ui.audio`](/documentation/audio)
            - [`ui.avatar`](/documentation/avatar)
            - [`ui.badge`](/documentation/badge)
            - [`ui.button`](/documentation/button)
            - [`ui.button_group`](/documentation/button_group)
            - [`ui.card`](/documentation/card), `ui.card_actions`, `ui.card_section`
            - [`ui.carousel`](/documentation/carousel), `ui.carousel_slide`
            - [`ui.chat_message`](/documentation/chat_message)
            - [`ui.checkbox`](/documentation/checkbox)
            - [`ui.chip`](/documentation/chip)
            - [`ui.circular_progress`](/documentation/circular_progress)
            - [`ui.code`](/documentation/code)
            - [`ui.codemirror`](/documentation/codemirror)
            - [`ui.color_input`](/documentation/color_input)
            - [`ui.color_picker`](/documentation/color_picker)
            - [`ui.column`](/documentation/column)
            - [`ui.context_menu`](/documentation/context_menu)
            - [`ui.date`](/documentation/date)
            - [`ui.dialog`](/documentation/dialog)
            - [`ui.dropdown_button`](/documentation/button_dropdown)
            - [`ui.echart`](/documentation/echart)
            - [`ui.editor`](/documentation/editor)
            - [`ui.expansion`](/documentation/expansion)
            - [`ui.grid`](/documentation/grid)
            - [`ui.highchart`](/documentation/highchart)
            - [`ui.html`](/documentation/html)
            - [`ui.icon`](/documentation/icon)
            - [`ui.image`](/documentation/image)
            - [`ui.input`](/documentation/input)
            - [`ui.interactive_image`](/documentation/interactive_image)
            - `ui.item`, `ui.item_label`, `ui.item_section`
            - [`ui.joystick`](/documentation/joystick)
            - [`ui.json_editor`](/documentation/json_editor)
            - [`ui.knob`](/documentation/knob)
            - [`ui.label`](/documentation/label)
            - [`ui.leaflet`](/documentation/leaflet)
            - [`ui.line_plot`](/documentation/line_plot)
            - [`ui.linear_progress`](/documentation/linear_progress)
            - [`ui.link`](/documentation/link), `ui.link_target`
            - [`ui.list`](/documentation/list)
            - [`ui.log`](/documentation/log)
            - [`ui.markdown`](/documentation/markdown)
            - [`ui.matplotlib`](/documentation/matplotlib)
            - [`ui.menu`](/documentation/menu), `ui.menu_item`
            - [`ui.mermaid`](/documentation/mermaid)
            - [`ui.notification`](/documentation/notification)
            - [`ui.number`](/documentation/number)
            - [`ui.pagination`](/documentation/pagination)
            - [`ui.plotly`](/documentation/plotly)
            - [`ui.pyplot`](/documentation/pyplot)
            - [`ui.radio`](/documentation/radio)
            - [`ui.rating`](/documentation/rating)
            - [`ui.range`](/documentation/range)
            - [`ui.restructured_text`](/documentation/restructured_text)
            - [`ui.row`](/documentation/row)
            - [`ui.scene`](/documentation/scene), [`ui.scene_view`](/documentation/scene#scene_view)
            - [`ui.scroll_area`](/documentation/scroll_area)
            - [`ui.select`](/documentation/select)
            - [`ui.separator`](/documentation/separator)
            - [`ui.skeleton`](/documentation/skeleton)
            - [`ui.slide_item`](/documentation/slide_item)
            - [`ui.slider`](/documentation/slider)
            - [`ui.space`](/documentation/space)
            - [`ui.spinner`](/documentation/spinner)
            - [`ui.splitter`](/documentation/splitter)
            - [`ui.stepper`](/documentation/stepper), `ui.step`, `ui.stepper_navigation`
            - [`ui.switch`](/documentation/switch)
            - [`ui.tabs`](/documentation/tabs), `ui.tab`, `ui.tab_panels`, `ui.tab_panel`
            - [`ui.table`](/documentation/table)
            - [`ui.textarea`](/documentation/textarea)
            - [`ui.time`](/documentation/time)
            - [`ui.timeline`](/documentation/timeline), `ui.timeline_entry`
            - [`ui.toggle`](/documentation/toggle)
            - [`ui.tooltip`](/documentation/tooltip)
            - [`ui.tree`](/documentation/tree)
            - [`ui.upload`](/documentation/upload)
            - [`ui.video`](/documentation/video)
        - 特殊布局 [元素](/documentation/page_layout):
            - `ui.header`
            - `ui.footer`
            - `ui.drawer`, `ui.left_drawer`, `ui.right_drawer`
            - `ui.page_sticky`
        - 特殊元素与对象:
            - [`ui.add_body_html`](/documentation/section_pages_routing#add_html_to_the_page) and
                [`ui.add_head_html`](/documentation/section_pages_routing#add_html_to_the_page): add HTML to the body and head of the page
            - [`ui.add_css`](/documentation/add_style#add_css_style_definitions_to_the_page),
                [`ui.add_sass`](/documentation/add_style#add_sass_style_definitions_to_the_page) and
                [`ui.add_scss`](/documentation/add_style#add_scss_style_definitions_to_the_page): add CSS, SASS and SCSS to the page
            - [`ui.clipboard`](/documentation/clipboard): interact with the browser's clipboard
            - [`ui.colors`](/documentation/colors): define the main color theme for a page
            - `ui.context`: get the current UI context including the `client` and `request` objects
            - [`ui.dark_mode`](/documentation/dark_mode): get and set the dark mode on a page
            - [`ui.download`](/documentation/download): download a file to the client
            - [`ui.fullscreen`](/documentation/fullscreen): enter, exit and toggle fullscreen mode
            - [`ui.keyboard`](/documentation/keyboard): define keyboard event handlers
            - [`ui.navigate`](/documentation/navigate): let the browser navigate to another location
            - [`ui.notify`](/documentation/notification): show a notification
            - [`ui.on`](/documentation/generic_events#custom_events): register an event handler
            - [`ui.page_title`](/documentation/page_title): change the current page title
            - [`ui.query`](/documentation/query): query HTML elements on the client side to modify props, classes and style definitions
            - [`ui.run`](/documentation/run) and `ui.run_with`: run the app (standalone or attached to a FastAPI app)
            - [`ui.run_javascript`](/documentation/run#run_custom_javascript_on_the_client_side): run custom JavaScript on the client side (can use `getElement()`, `getHtmlElement()`, and `emitEvent()`)
            - [`ui.teleport`](/documentation/teleport): teleport an element to a different location in the HTML DOM
            - [`ui.timer`](/documentation/timer): run a function periodically or once after a delay
            - `ui.update`: send updates of multiple elements to the client
        - 装饰器:
            - [`ui.page`](/documentation/page): define a page (in contrast to the automatically generated "auto-index page")
            - [`ui.refreshable`](/documentation/refreshable), `ui.refreshable_method`: define refreshable UI containers
                (can use [`ui.state`](/documentation/refreshable#refreshable_ui_with_reactive_state))

        #### `app`

        应用级存储、挂载点和生命周期钩子。（实际上，您可以把它当作 NiceGUI 创建的 FastAPI 实例。）

        - [`app.storage`](/documentation/storage):
            - `app.storage.tab`: stored in memory on the server, unique per tab
            - `app.storage.client`: stored in memory on the server, unique per client connected to a page
            - `app.storage.user`: stored in a file on the server, unique per browser
            - `app.storage.general`: stored in a file on the server, shared across the entire app
            - `app.storage.browser`: stored in the browser's local storage, unique per browser
        - [lifecycle hooks](/documentation/section_action_events#events):
            - `app.on_connect()`: called when a client connects
            - `app.on_disconnect()`: called when a client disconnects
            - `app.on_startup()`: called when the app starts
            - `app.on_shutdown()`: called when the app shuts down
            - `app.on_exception()`: called when an exception occurs
        - [`app.shutdown()`](/documentation/section_action_events#shut_down_nicegui): shut down the app
        - static files:
            - [`app.add_static_files()`](/documentation/section_pages_routing#add_a_directory_of_static_files),
                `app.add_static_file()`: serve static files
            - [`app.add_media_files()`](/documentation/section_pages_routing#add_directory_of_media_files),
                `app.add_media_file()`: serve media files (supports streaming)
        - [`app.native`](/documentation/section_configuration_deployment#native_mode): configure the app when running in native mode

        #### `html`

        [纯 HTML 元素](/documentation/html#other_html_elements):

        `a`,
        `abbr`,
        `acronym`,
        `address`,
        `area`,
        `article`,
        `aside`,
        `audio`,
        `b`,
        `basefont`,
        `bdi`,
        `bdo`,
        `big`,
        `blockquote`,
        `br`,
        `button`,
        `canvas`,
        `caption`,
        `cite`,
        `code`,
        `col`,
        `colgroup`,
        `data`,
        `datalist`,
        `dd`,
        `del_`,
        `details`,
        `dfn`,
        `dialog`,
        `div`,
        `dl`,
        `dt`,
        `em`,
        `embed`,
        `fieldset`,
        `figcaption`,
        `figure`,
        `footer`,
        `form`,
        `h1`,
        `header`,
        `hgroup`,
        `hr`,
        `i`,
        `iframe`,
        `img`,
        `input_`,
        `ins`,
        `kbd`,
        `label`,
        `legend`,
        `li`,
        `main`,
        `map_`,
        `mark`,
        `menu`,
        `meter`,
        `nav`,
        `object_`,
        `ol`,
        `optgroup`,
        `option`,
        `output`,
        `p`,
        `param`,
        `picture`,
        `pre`,
        `progress`,
        `q`,
        `rp`,
        `rt`,
        `ruby`,
        `s`,
        `samp`,
        `search`,
        `section`,
        `select`,
        `small`,
        `source`,
        `span`,
        `strong`,
        `sub`,
        `summary`,
        `sup`,
        `svg`,
        `table`,
        `tbody`,
        `td`,
        `template`,
        `textarea`,
        `tfoot`,
        `th`,
        `thead`,
        `time`,
        `tr`,
        `track`,
        `u`,
        `ul`,
        `var`,
        `video`,
        `wbr`

        #### `后台任务`

        在后台异步执行的函数。

        - `create()`: create a background task
        - `create_lazy()`: prevent two tasks with the same name from running at the same time

        #### `运行`

        Run IO and CPU bound functions in separate threads and processes.

        - [`run.cpu_bound()`](/documentation/section_action_events#running_cpu-bound_tasks): run a CPU-bound function in a separate process
        - [`run.io_bound()`](/documentation/section_action_events#running_i_o-bound_tasks): run an IO-bound function in a separate thread

        #### `绑定`

        [Bind properties of objects to each other](/documentation/section_binding_properties).

        - [`binding.BindableProperty`](/documentation/section_binding_properties#bindable_properties_for_maximum_performance): bindable properties for maximum performance
        - [`binding.bindable_dataclass()`](/documentation/section_binding_properties#bindable_dataclass): create a dataclass with bindable properties
        - `binding.bind()`, `binding.bind_from()`, `binding.bind_to()`: methods to bind two properties

        #### `observables`

        Observable collections that notify observers when their contents change.

        - `ObservableCollection`: base class
        - `ObservableDict`: an observable dictionary
        - `ObservableList`: an observable list
        - `ObservableSet`: an observable set

        #### `测试`

        编写自动 UI 测试， 当运行在无头浏览器 (慢速) 或者在 Python 中完整模拟 (快速).

        - [`Screen`](/documentation/section_testing#screen_fixture) fixture: start a real (headless) browser to interact with your application
        - [`User`](/documentation/section_testing#user_fixture) fixture: simulate user interaction on a Python level (fast)
    ''').classes('map-of-nicegui arrow-links bold-links')
