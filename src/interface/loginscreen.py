# -*- coding: utf-8 -*-

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

class LoginScreen(BoxLayout):

    root_self = ObjectProperty()
    username = ObjectProperty()
    password = ObjectProperty()

    ###
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        '''self.orientation = 'vertical'
        ###
        self.grid = GridLayout()
        self.grid.cols = 2
        self.grid.add_widget(Label(text='User Name'))
        self.grid.username = TextInput(multiline=False)
        self.grid.add_widget(self.grid.username)
        self.grid.add_widget(Label(text='password'))
        self.grid.password = TextInput(multiline=False)
        self.grid.add_widget(self.grid.password)
        ###
        self.options = BoxLayout()
        self.options.size_hint_y = 0.5
        self.options.bt_cancel = Button(text='Cancel')
        self.options.add_widget(self.options.bt_cancel)
        self.options.bt_login = Button(text='Login')
        self.options.bt_login.bind(on_press=self.bt_login_clicked)
        self.options.add_widget(self.options.bt_login)
        ###
        self.add_widget(self.grid)
        self.add_widget(self.options)'''

    ###
    def bt_login(self):

        row = self.root_self.database.isValidLogin(self.username.text, self.password.text)

        if(row == None):
            content = Label(text = 'Username or Password incorrect!')
            popup = Popup(
                        title           = 'User Login',
                        content         = content,
                        size_hint       = (None, None),
                        size            = (400, 100)
                    )

            # open the popup
            popup.open()
            return
        #
        self.root_self.pos_system.setUserName(self.username.text)
        self.root_self.pos_system.setUserID(row[0])
        self.root_self.database.registerLogs(self.root_self.pos_system.getUserID(), 0)
        #
        self.root_self.loadBarOptions()
        self.root_self.loadMainWindow()
        #
        self.root_self.a_price.label_price = Label(text = '0€')
        self.root_self.a_price.add_widget(self.root_self.a_price.label_price)
        #
        self.root_self.popup.dismiss()

    ###
    def bt_cancel(self):
        #
        self.root_self.popup.dismiss()
