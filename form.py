import PySimpleGUI as pg
import thanhcong


layout = [

        [pg.Text('Tên Đăng Nhập', background_color='green', text_color='yellow')],
        [pg.InputText(key= 'tên đăng nhập', text_color= "blue") ],
        [pg.Text('Mật Khẩu',background_color='green', text_color='yellow')],
        [pg.InputText(key= "mật khẩu", password_char="*")],
        [pg.Button('Đăng Nhập',)],
        [pg.Text('', key="tin nhắn")]




        ]

tai_khoan = "congthanh"
mat_khau = "123456"
window= pg.Window('Đăng nhập tài khoản', layout=layout, background_color='green')
running = True
while running:
    event, value = window.read()
    if event == pg.WINDOW_CLOSED:
        break
    elif event == "Đăng Nhập":
        if value["tên đăng nhập"] == tai_khoan and value["mật khẩu"] == mat_khau:
            window['tin nhắn'].update('đăng nhập thành công')
            running =False
            thanhcong.run()
        else:
            window['tin nhắn'].update('đăng nhập không thành công')