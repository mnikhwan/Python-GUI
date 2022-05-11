from PySimpleGUI import *
darkbg = "#121212"  
reds = "#F05454"
darkblue = "#30475E"
whites = "#F5F5F5"
yellows = "#FFC107"

layout = [[Text('Keuntungan             : $', background_color=darkbg), InputText("20", size=(6,1))],
          [Txt('NOTE: Default Keuntungan adalah $20, Anda bisa merubahnya jika mau',  font = ('Helvetica', 7), background_color=darkbg, text_color=yellows)],
          [Txt('================[MES-BOD]================', background_color=darkbg, text_color=reds)],
          [Text('Jmlh Mesin Compo   :   ', background_color=darkbg), InputText(size=(6,1))],
          [Text('Jmlh Body Compo    :   ', background_color=darkbg), InputText(size=(6,1))],
          [ReadFormButton('Submit', button_color=reds), Text('Harga     : $', background_color=darkbg), Text('', background_color=darkbg, font = ('Helvetica'), key = 'hasilmesbod')],
          [Txt('=========================================', background_color=darkbg, text_color=reds)],
          # [Txt('=======[Component]=======', background_color=darkbg, text_color=reds)],
          # [Text('Jmlh Compo : ', background_color=darkbg)],
          [Txt('',background_color=darkbg)],
          [Txt('',background_color=darkbg)],
          [Txt('',background_color=darkbg)],
          [Txt('',background_color=darkbg)],
          [Txt(' - Version 1.0 | @mn.ikhwan ', font = ('Helvetica', 7), background_color=darkbg, text_color=yellows)],
          #[Txt(' - https://linktr.ee/mn.ikhwan ', font = ('Helvetica', 7), background_color=darkbg, text_color=yellows)],
          ]
          
form = FlexForm('Samp Mech Compo Calc', background_color=darkbg, size=(350, 350), default_button_element_size = (6, 1),
                auto_size_buttons = False, grab_anywhere = False)
form.Layout(layout)
  

while True:
    
    button, value = form.Read()
    v1 = int(value[0])
    v2 = int(value[1])
    v3 = int(value[2])
    
    def countmesbod(v1, v2, v3):
        mesbod = (v2 + v3) / 2 + v1
        return mesbod
        
    if button == 'Submit':     
        form.FindElement('hasilmesbod').Update(countmesbod(v1, v2, v3))
    elif button == 'Quit'  or button == None:
      Window.close()
      
      
#konversi ke .exe
#python -m pysimplegui-exemaker.pysimplegui-exemaker
    