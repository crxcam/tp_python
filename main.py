
#   models
from src.models.app_actions import AppActions
#   services
import src.tools.user_service as user_srv

#   graphic
from tkinter import Button, Entry, Label, Tk, ttk

response: tuple[bool, str] = ()
user_email: str = ''
user_first_name: str = ''
user_last_name: str = ''


def btn_create_user():
    label_response_operation.config(text="")
    user_create_one(entry_first_name.get(), entry_last_name.get(),
                    entry_email.get(), entry_password.get())


def btn_login_user():
    label_response_operation.config(text="")
    user_login(entry_email.get(), entry_password.get())

def build_response(msg: str = ''):
    label_response_operation.config(text=msg)
    label_response_operation.grid(column=1, row=7)

try:
    def user_create_one(first_name: str = '',
                        last_name: str = '',
                        email: str = '',
                        clear_password: str = '') -> str:
        response: tuple[bool, str] = user_srv.user_create_one(
            first_name, last_name, email, clear_password
        )
        build_response(response[1])
except Exception as e:
    response = user_srv.build_response_and_log(
        True, user_srv.generic_error_response, None, AppActions.USER_CREATE_ACCOUNT, str(e))

try:
    def user_login(email: str, password: str) -> str:
        response: tuple[bool, str,str] = user_srv.user_login(
            email, password)
        build_response(response[1])
except Exception as e:
    response = user_srv.build_response_and_log(
        True, user_srv.generic_error_response, None, AppActions.USER_LOGIN, str(e))

try:
    def replace_password(current_password: str, new_password: str, email: str) -> str:
        response: tuple[bool, str] = user_srv.replace_password(
            current_password, new_password, email)
        build_response(response[1])
except Exception as e:
    response = user_srv.build_response_and_log(
        True, user_srv.generic_error_response, None, AppActions.USER_CHANGE_PASSWORD, str(e))


try:
    def user_delete(email: str) -> str:
        response: tuple[bool, str] = user_srv.user_delete(email)
        build_response(response[0], response[1])
except Exception as e:
    response = user_srv.build_response_and_log(
        True, user_srv.generic_error_response, None, AppActions.USER_DELETE_ACCOUNT, str(e))





frame = Tk()
width = 600
height = 500
frame.geometry(f"{width}x{height}")
frame.title("Gestion utilisateur")

# first_name
label_first_name = Label(frame, text="Nom : ")
label_first_name.grid(column=0, row=0)
entry_first_name = Entry(frame)
entry_first_name.grid(column=1, row=0)

# last_name
label_last_name = Label(frame, text="Prénom : ")
label_last_name.grid(column=0, row=1)
entry_last_name = Entry(frame)
entry_last_name.grid(column=1, row=1)

# email
label_email = Label(frame, text="Email : ")
label_email.grid(column=0, row=2)
entry_email = Entry(frame)
entry_email.grid(column=1, row=2)

# password
label_password = Label(frame, text="Mot de passe : ")
label_password.grid(column=0, row=3)
entry_password = Entry(frame)
entry_password.grid(column=1, row=3)

# new_password
label_new_password = Label(frame, text="Nouveau mot de passe : ")
label_new_password.grid(column=0, row=4)
entry_new_password = Entry(frame)
entry_new_password.grid(column=1, row=4)

# btn
button_create_compte = Button(
    frame, text="Crée un compte", command=btn_create_user)
button_create_compte.grid(column=0, row=5)

button_login = Button(frame, text="Connexion", command=btn_login_user)
button_login.grid(column=1, row=5)


label_response_operation = Label(frame, text="")


frame.mainloop()


# user_create_one('jonh', 'wick', 'toto2@gmail.com', 'password')
# user_login('toto2@gmail.com', 'password')
# replace_password('passwordk','password','toto2@gmail.com')
# user_delete('toto2@gmail.com')

# log_srv.save_log(False, "test", "id user")
