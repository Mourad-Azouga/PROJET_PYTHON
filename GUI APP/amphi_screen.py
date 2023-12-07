# File: Amphi_screen.py
from header import *
from kivy.app import App  
class AmphiScreen(Screen):
    def __init__(self, **kwargs):
        super(AmphiScreen, self).__init__(**kwargs)
        main_layout = BoxLayout(orientation='vertical')

        header = BoxLayout(orientation='vertical')

        quit_ = Button(
            background_normal='3.png',
            background_down='3.png',
            size_hint=(None, None),
            size=(50, 50),
            pos_hint = {'x': 0, 'y':0},
            padding=(10, 0, 10, 0)
        )
        quit_.bind(on_release = self.quit_)

        settings = Button(
            background_normal='4.png',
            background_down='4.png',
            size_hint=(None, None),
            size=(50, 50),
            pos_hint = {'x': 0, 'y': .8},
            padding=(10, 0, 10, 0)
        )
        settings.bind(on_press=self.settings)

        back_to_main = Button(
            background_normal='5.png',
            background_down='5.png',
            size_hint=(None, None),
            size=(50, 50),
            pos_hint = {'x': 0, 'y': .8},
            padding=(10, 0, 10, 0)
        )
        back_to_main.bind(on_press=self.dismiss)
        quit_.bind(on_press=self.quit_)
        header.add_widget(back_to_main)
        header.add_widget(settings)
        header.add_widget(quit_)

        content_layout = GridLayout(cols=2, spacing=30, size_hint_y=None, padding=(150, 30, 30, 30))
        content_layout.bind(minimum_height=content_layout.setter('height'))

        # Create six buttons and add them to the content layout
        for i in range(6):
            amphi_id = i+1 #bach tbda mn 0-6 machi mn 1-5 rah machi ghalat -Mourad
            button = Button(
                text=f"Amphi {amphi_id}",
                size=(600, 300),  # Adjust size as needed
                size_hint=(None, None),
                background_normal='1.png',
                background_down='1.png',
                padding = (30,30,30,30)
            )
            content_layout.add_widget(button)

        # Wrap the content layout in a ScrollView
        scroll_view = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        scroll_view.add_widget(content_layout)

        # Add the ScrollView to the screen
        main_layout.add_widget(scroll_view)
        main_layout.add_widget(header)

        self.add_widget(main_layout)

    def dismiss(self, instance):

        transition = SlideTransition(direction='right')
        self.manager.transition = transition
        self.manager.current = 'main'

    def settings(self, instance):
        self.manager.current = 'settings'

    def quit_(self, instance):
        App.get_running_app().stop()
