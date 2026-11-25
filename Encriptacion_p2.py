from simplecrypt import encrypt, decrypt
from tkinter import *
from firebase import firebase

firebase = firebase.FirebaseApplication("https://dese-c2712-default-rtdb.firebaseio.com",None)

login_windows = Tk()
login_windows.geometry("400x400")
login_windows.config(bg='#AB92BF')


username = ""
message_entry= ""
your_code = ""
your_friends_code= ""
message_text= ""
last_value = {}

def getData():
    global message_text
    global your_code
    global your_friends_code
    global last_value

    # Obtener tus mensajes
    get_your_data = firebase.get('/' + your_code, None)

    print("\n====== TUS MENSAJES ======")

    if get_your_data:

        for message_id, data in get_your_data.items():

            if message_id not in last_value:

                encrypted_message = data['message']

                print("ID:", message_id)
                print("Codigo encriptado:", encrypted_message)

                byte_str = bytes.fromhex(encrypted_message)
                original = decrypt('AIM', byte_str)

                final_message = original.decode('utf-8')

                print("Mensaje original:", final_message)

                message_text.insert(END, final_message + "\n")

                last_value[message_id] = True

    # Obtener mensajes de tu amigo
    get_friends_data = firebase.get('/' + your_friends_code, None)

    print("\n====== MENSAJES DE TU AMIGO ======")

    if get_friends_data:

        for message_id, data in get_friends_data.items():

            if message_id not in last_value:

                encrypted_message = data['message']

                print("ID:", message_id)
                print("Codigo encriptado:", encrypted_message)

                byte_str = bytes.fromhex(encrypted_message)
                original = decrypt('AIM', byte_str)

                final_message = original.decode('utf-8')

                print("Mensaje original:", final_message)

                message_text.insert(END, final_message + "\n")

                last_value[message_id] = True



def sendData():
    global username
    global message_entry
    global your_code

    message = username + ": " + message_entry.get()

    ciphercode = encrypt('AIM', message)
    hex_string = ciphercode.hex()

    # Guardar mensaje sin reemplazar los anteriores
    put_date = firebase.post(
        '/' + your_code,
        {'message': hex_string}
    )

    print("Mensaje guardado:", put_date)

    message_entry.delete(0, END)

    getData()

def enterRoom():
    global username
    global message_entry
    global your_code
    global your_friends_code
    global message_text

    your_code = your_code_entry.get()
    your_friends_code = friend_code_Entry.get()
    username = username_entry.get()
    login_windows.destroy()
    
    message_windows = Tk()
    message_windows.config(bg="#AFC1D6")
    message_windows.geometry("600x500")

    message_text = Text(message_windows, height=20, width=72)
    message_text.place(relx=0.5 ,rely=0.35, anchor= CENTER)

    message_label = Label(message_windows, text='Mensaje ', font=' arial 13', bg="#AFC1D6",fg="white")
    message_label.place(relx=0.3 ,rely=0.8, anchor= CENTER)

    message_entry = Entry(message_windows, font= "arial 15")
    message_entry.place(relx=0.6 ,rely=0.8, anchor= CENTER)

    btn_send= Button(message_windows, text="Enviar", font=' arial 13', bg="#D6CA98",fg="black", padx=10, relief=FLAT,command=sendData)
    btn_send.place(relx=0.5 ,rely=0.9, anchor= CENTER)  
    message_windows.mainloop()


username_label = Label(login_windows, text='Nombre de usuario:  ', font = 'arial 13', bg= '#AB92BF', fg='white')
username_label.place(relx=0.2, rely=0.3, anchor= CENTER)

username_entry = Entry(login_windows)
username_entry.place(relx=0.6,rely=0.3,anchor= CENTER)

your_code_label = Label(login_windows, text='Tu codigo:  ', font = 'arial 13', bg= '#AB92BF', fg='white')
your_code_label.place(relx=0.3,rely= 0.4,anchor= CENTER)

your_code_entry = Entry(login_windows)
your_code_entry.place(relx=0.6,rely=0.4,anchor= CENTER)

friend_code_label = Label(login_windows, text='Codigo de tu amigo: ', font='arial 13', bg= '#AB92BF',fg="white")
friend_code_label.place(relx=0.22,rely=0.5, anchor=CENTER)

friend_code_Entry = Entry(login_windows)
friend_code_Entry.place(relx=0.6,rely=0.5,anchor=CENTER)

btn_start =Button(login_windows, text="Iniciar", font="arial 13", bg="#CEF9F2", fg="black", command=enterRoom, relief= FLAT, padx=10)
btn_start.place(relx=0.5, rely=0.65, anchor=CENTER)


login_windows.mainloop()