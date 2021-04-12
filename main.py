from kivy.lang.builder import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
#from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRoundFlatIconButton
from kivymd.uix.behaviors import FocusBehavior


#Window.size = (300, 500)
screen_helper = '''

MDBoxLayout:
    orientation: "vertical"
    MDToolbar:
        title: "É Palindrome?"
        elevation: 8
        right_action_items: [['lightbulb-outline', lambda x: app.color()]]
    ScreenManager:
        InicialScreen:
        PrincipalScreen:
 
    
<InicialScreen>:
    name: 'inicial'
    MDIconButton:
        pos_hint: {'center_x':0.5, 'center_y':0.6}
        user_font_size: '90sp'
        icon: "alphabetical"
        
    
        
    MDRectangleFlatButton:
        text: 'Começar'
        pos_hint: {'center_x':0.5, 'center_y':0.3}
        md_bg_color: 1, 1, 1, 1
        theme_text_color: "Custom"
        color_mode: 'accent'
        text_color: 0, 0, 0, 1
        line_color: 0, 0, 0, 1
        icon_color: 0, 0, 0, 1
        on_press:  root.manager.current = 'principal'      
        

<PrincipalScreen>:
    name: 'principal'         
    MDIconButton:
        pos_hint: {"center_x": .23, "center_y": 0.75}
        user_font_size: '50sp'
        icon: "format-letter-starts-with"
    MDLabel:
        
        halign: 'center'
        pos_hint: {"center_x": .6, 'center_y':0.75}
        text: "Digite a palavra"  
        font_style: 'H5'
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        
    MDTextField:
        id: palindrome
        md_bg_color: 1, 1, 1, 1
        theme_text_color: "Custom"
        required: True
        hint_text: "Digite aqui"
        helper_text: "Ex. Omissíssimo"
        helper_text_mode: "on_focus"
        size_hint_x: .7
        size_hint_y: .1
        max_text_length: 40
        color_mode: 'accent'
        line_color_normal: 0, 0, 0, 1
        mode: "rectangle"
        pos_hint: {"center_x": .5, "center_y": .55}
        icon: 'scoreboard'
    
    MDIconButton:
        id: icone
        pos_hint: {"center_x": .20, "center_y": .4}
        size_hint_x: .5
        size_hint_y: .1
        user_font_size: '40sp'
        icon: ""
        
    MDLabel:
        id: resultado
        halign: 'center'
        pos_hint: {"center_x": .5, 'center_y':0.4}
        text: ""  
        font_style: 'H5'
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1

    
    MDRoundFlatIconButton:
        size_hint_x: .35
        size_hint_y: .1
        md_bg_color: 1, 1, 1, 1
        icon: "arrow-left"
        text: 'Voltar'
        theme_text_color: "Custom"
        color_mode: 'accent'
        text_color: 0, 0, 0, 1
        line_color: 0, 0, 0, 1
        icon_color: 0, 0, 0, 1
        pos_hint: {'center_x': 0.3, 'center_y': 0.2}
        on_press:  root.manager.current = 'inicial'   
            
    MDRoundFlatIconButton:
        size_hint_x: .35
        size_hint_y: .1
        md_bg_color: 1, 1, 1, 1
        icon: "sync-circle"
        text: 'Verificar'
        theme_text_color: "Custom"
        color_mode: 'accent'
        text_color: 0, 0, 0, 1
        line_color: 0, 0, 0, 1
        icon_color: 0, 0, 0, 1
        pos_hint: {'center_x': 0.7, 'center_y': 0.2}
        on_release: root.Palidromo()    
    
'''


class InicialScreen(MDScreen):
    pass


class PrincipalScreen(MDScreen):

    def Palidromo(self):
        s = self.ids.palindrome.text
        if s == '':
            self.ids.icone.icon = 'not-equal-variant'
            self.ids.resultado.text = 'NULL'
        else:
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    self.ids.icone.icon = 'not-equal'
                    self.ids.resultado.text = 'Falso'
                    print('não e palidrome')
                    return False
                l += 1
                r -= 1
            self.ids.icone.icon = 'equal'
            self.ids.resultado.text = 'Verdadeiro'
            print('palidrome')
            return True


sm = ScreenManager()
sm.add_widget(InicialScreen(name='inicial'))
sm.add_widget(PrincipalScreen(name='principal'))


class PalidromeApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Yellow'
        self.theme_cls.accent_palette = 'Blue'
        self.theme_cls.theme_style = 'Dark'
        return Builder.load_string(screen_helper)

    def color(self):
        style = self.theme_cls.theme_style
        if style == 'Light':
            self.theme_cls.theme_style = 'Dark'
        else:
            self.theme_cls.theme_style = 'Light'


if __name__ == '__main__':
    PalidromeApp().run()
