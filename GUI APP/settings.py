from header import *

class Settings(Screen):
    def __init__(self, **kwargs):
        super(Settings, self).__init__(**kwargs)
        background_image = Image(source='under.png', allow_stretch=True, keep_ratio=False)
        self.add_widget(background_image)
        main_layout = BoxLayout(orientation='vertical', size_hint =(1,1),pos_hint={'center_x': 0.5, 'center_y': 0.5})
        #header how l "div" li 3amlin fih les buttons dial shutdown w dakchi
        header = BoxLayout(orientation='vertical', size_hint=(None, .1))

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

