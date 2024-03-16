import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar

class AgendaApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Agenda Personal")

        # Frame para la lista de eventos
        self.event_frame = tk.Frame(self.master)
        self.event_frame.pack(pady=10)

        self.event_label = tk.Label(self.event_frame, text="Eventos Programados:")
        self.event_label.pack()

        self.event_treeview = ttk.Treeview(self.event_frame, columns=("Fecha", "Hora", "Descripción"), selectmode="extended")
        self.event_treeview.heading("#0", text="ID")
        self.event_treeview.heading("Fecha", text="Fecha")
        self.event_treeview.heading("Hora", text="Hora")
        self.event_treeview.heading("Descripción", text="Descripción")
        self.event_treeview.pack()

        # Frame para la entrada de datos
        self.input_frame = tk.Frame(self.master)
        self.input_frame.pack(pady=10)

        self.date_label = tk.Label(self.input_frame, text="Fecha:")
        self.date_label.grid(row=0, column=0, padx=5)

        self.date_entry = Calendar(self.input_frame, selectmode="day", date_pattern="y-mm-dd")
        self.date_entry.grid(row=0, column=1, padx=5)

        self.time_label = tk.Label(self.input_frame, text="Hora:")
        self.time_label.grid(row=0, column=2, padx=5)

        self.time_entry = tk.Entry(self.input_frame, width=10)
        self.time_entry.grid(row=0, column=3, padx=5)

        self.description_label = tk.Label(self.input_frame, text="Descripción:")
        self.description_label.grid(row=1, column=0, padx=5)

        self.description_entry = tk.Entry(self.input_frame, width=50)
        self.description_entry.grid(row=1, column=1, columnspan=3, padx=5)

        # Botones de acción
        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack(pady=10)

        self.add_button = tk.Button(self.button_frame, text="Agregar Evento", command=self.add_event)
        self.add_button.grid(row=0, column=0, padx=5)

        self.delete_button = tk.Button(self.button_frame, text="Eliminar Evento Seleccionado", command=self.delete_event)
        self.delete_button.grid(row=0, column=1, padx=5)

        self.quit_button = tk.Button(self.button_frame, text="Salir", command=self.master.quit)
        self.quit_button.grid(row=0, column=2, padx=5)

    def add_event(self):
        date = self.date_entry.get_date()
        time = self.time_entry.get()
        description = self.description_entry.get()

        if date and time and description:
            self.event_treeview.insert("", "end", text="ID", values=(date, time, description))
            self.clear_entries()
        else:
            messagebox.showwarning("Error", "Por favor completa todos los campos.")

    def delete_event(self):
        try:
            selected_item = self.event_treeview.selection()[0]
            self.event_treeview.delete(selected_item)
        except IndexError:
            messagebox.showinfo("Error", "Por favor selecciona un evento para eliminar.")

    def clear_entries(self):
        self.date_entry.set_date("")
        self.time_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
