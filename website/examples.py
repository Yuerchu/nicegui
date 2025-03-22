from dataclasses import dataclass, field
from pathlib import Path
from typing import List

PATH = Path(__file__).parent.parent / 'examples'


@dataclass
class Example:
    title: str
    description: str
    url: str = field(init=False)

    def __post_init__(self) -> None:
        """Post-initialization hook."""
        name = self.title.lower().replace(' ', '_').replace('-', '_')
        content = [p for p in (PATH / name).glob('*') if not p.name.startswith(('__pycache__', '.', 'test_'))]
        filename = 'main.py' if len(content) == 1 else ''
        self.url = f'https://github.com/zauberzeug/nicegui/tree/main/examples/{name}/{filename}'


examples: List[Example] = [
    Example('幻灯片', 'implements a keyboard-controlled image slideshow'),
    Example('单点登录', 'shows how to use sessions to build a login screen'),
    Example('模块化程序', 'provides an example of how to modularize your application into multiple files and reuse code'),
    Example('FastAPI', 'illustrates the integration of NiceGUI with an existing FastAPI application'),
    Example('AI 界面',
            'utilizes the [replicate](https://replicate.com) library to perform voice-to-text transcription and generate images from prompts with Stable Diffusion'),
    Example('3D 场景', 'creates a webGL view and loads an STL mesh illuminated with a spotlight'),
    Example('自定义 Vue 组件', 'shows how to write and integrate a custom Vue component'),
    Example('图像蒙版叠加', 'shows how to overlay an image with a mask'),
    Example('无限滚动', 'presents an infinitely scrolling image gallery'),
    Example('OpenCV 网络摄像头', 'uses OpenCV to capture images from a webcam'),
    Example('SVG 始终', 'displays an analog clock by updating an SVG with `ui.timer`'),
    Example('进度条', 'demonstrates a progress bar for heavy computations'),
    Example('全局 Worker', 'demonstrates a global worker for heavy computations with progress feedback'),
    Example('NGINX 子路由', 'shows the setup to serve an app behind a reverse proxy subpath'),
    Example('脚本执行器', 'executes scripts on selection and displays the output'),
    Example('文件选择器', 'demonstrates a dialog for selecting files locally on the server'),
    Example('键入时搜索',
            'using public API of [thecocktaildb.com](https://www.thecocktaildb.com/) to search for cocktails'),
    Example('菜单与标签', 'uses Quasar to create foldable menu and tabs inside a header bar'),
    Example('代办事项', 'shows a simple todo list with checkboxes and text input'),
    Example('Trello 卡片', 'shows Trello-like cards that can be dragged and dropped into columns'),
    Example('Slots 插槽', 'shows how to use scoped slots to customize Quasar elements'),
    Example('表格与插槽', 'shows how to use component slots in a table'),
    Example('单页应用程序', 'navigate without reloading the page'),
    Example('聊天应用', 'a simple chat app'),
    Example('与 AI 聊天', 'a simple chat app with AI'),
    Example('SQLite 数据库', 'CRUD operations on a SQLite database with async-support through Tortoise ORM'),
    Example('Pandas DataFrame', 'displays an editable [pandas](https://pandas.pydata.org) DataFrame'),
    Example('灯箱', 'a thumbnail gallery where each image can be clicked to enlarge'),
    Example('ROS2', 'Using NiceGUI as web interface for a ROS2 robot'),
    Example('Docker 镜像',
            'use the official [zauberzeug/nicegui](https://hub.docker.com/r/zauberzeug/nicegui) docker image'),
    Example('将文本下载为文件', 'providing in-memory data like strings as file download'),
    Example('生成 PDF', 'create an SVG preview and PDF download from input form elements'),
    Example('自定义绑定', 'create a custom binding for a label with a bindable background color'),
    Example('Descope 单点登录', 'login form and user profile using [Descope](https://descope.com)'),
    Example('可编辑的表格', 'editable table allowing to add, edit, delete rows'),
    Example('可编辑的 AG 网格', 'editable AG Grid allowing to add, edit, delete rows'),
    Example('FullCalendar 全日历', 'show an interactive calendar using the [FullCalendar library](https://fullcalendar.io/)'),
    Example('Pytests 测试', 'test a NiceGUI app with pytest'),
    Example('Pyserial', 'communicate with a serial device'),
    Example('Webserial', 'communicate with a serial device using the WebSerial API'),
    Example('Websockets', 'use [websockets library](https://websockets.readthedocs.io/) to start a websocket server'),
    Example('录音机', 'Record audio, play it back or download it'),
    Example('ZeroMQ', 'Simple ZeroMQ PUSH/PULL server and client'),
    Example('NGINX HTTPS', 'Use NGINX to serve a NiceGUI app with HTTPS'),
    Example('Node 模块集成', 'Use NPM to add dependencies to a NiceGUI app'),
    Example('签名板', 'A custom element based on [signature_pad](https://www.npmjs.com/package/signature_pad'),
    Example('OpenAI 助手', "Using OpenAI's Assistant API with async/await"),
    Example('Redis 存储', 'Use Redis storage to share data across multiple instances behind a reverse proxy or load balancer'),
    Example('Google One-Tap 身份验证', 'Authenticate users via Google One-Tap'),
    Example('Google OAuth2', 'Authenticate with Google OAuth2')
]
