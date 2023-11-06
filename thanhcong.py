import PySimpleGUI as pg

layout = [

        [pg.Text('CHÚC MỪNG BẠN ĐÃ ĐĂNG NHẬP THÀNH CÔNG', font= "Arial", size= 50, text_color= "white", background_color="black", border_width=10)],
        
]
window= pg.Window('Đăng nhập thành công', layout=layout, margins=(100,100),background_color= 'black')

def run():
    running = True
    while running:
        event, value = window.read()
        if event == pg.WINDOW_CLOSED:
            break

if __name__=='__main__':
    run()