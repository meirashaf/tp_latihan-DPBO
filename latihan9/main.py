from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *

# menambahkan value
hunians = []
hunians.append(Apartemen("Apartemen", "Saul Goodman", 3, 3, 45))
hunians.append(Rumah("Rumah", "Gustavo Fring", 5, 2, 50))
hunians.append(Indekos("Chuck McGill", "Howard Hamlin", 60))
hunians.append(Rumah("Rumah", "Mike Ehrmantraut", 1, 4, 72))

root = Tk()
root.title("Praktikum DPBO Python")

# fungsi untuk detail tiap value class
def details(index):
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())

    # membuat frame baru
    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    # mnampilkan summary + document
    d_summary = Label(d_frame, text=hunians[index].get_summary(), anchor="w").grid(row=0, column=0, sticky="w")
    d_docs = Label(d_frame, text=hunians[index].get_dokumen(), anchor="w").grid(row=1, column=0, sticky="w")

    # button untuk exit
    b_exit = Button(d_frame, text="Exit", command=top.destroy)
    b_exit.grid(row=2, column=0)

# frame utama
frame = LabelFrame(root, text="Data Seluruh Residen", padx=10, pady=10)
frame.pack(padx=10, pady=10)

opts = LabelFrame(root, padx=10, pady=10)
opts.pack(padx=10, pady=10)

# button add data + exit
b_add = Button(opts, text="Add Data", state="disabled")
b_add.grid(row=0, column=0)

b_exit = Button(opts, text="Exit", command=root.quit)
b_exit.grid(row=0, column=1)

# menampilkan tiap value dlm bentuk tabel
for index, h in enumerate(hunians):
    idx = Label(frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
    idx.grid(row=index, column=0)

    type = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
    type.grid(row=index, column=1)

    # percabangan untuk indekos & bukan indekos
    if h.get_jenis() != "Indekos": 
        name = Label(frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
        name.grid(row=index, column=2)
    else:
        name = Label(frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
        name.grid(row=index, column=2)

    b_detail = Button(frame, text="Details ", command=lambda index=index: details(index))
    b_detail.grid(row=index, column=3)

root.mainloop()
