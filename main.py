import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Button, filedialog


def show_report(data):
	try:
		data = pd.read_excel(data, engine='openpyxl')
		data.set_index('Päivämäärä', inplace=True)
		data[['Myynti (€)', 'Tulot (€)', 'Menot (€)']].plot()

		plt.title("Sales report 2024")
		plt.ylabel("Eurot (€)")
		plt.xlabel("Päivämäärä")
		plt.xticks(rotation=45)
		plt.tight_layout()
		plt.legend(loc='upper left')
		plt.show()
	except Exception as e:
		print("Error reading file:", e)


def open_file():
	file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
	if file_path:
		show_report(file_path)


def main():
	window = Tk()
	window.title("GetMyReport")
	window.minsize(300, 200)
	label = Label(window, text="Choose excel file :")
	label.pack(pady=10)

	button = Button(window, text="Choose file", command=open_file)
	button.pack(pady=10)
	window.mainloop()


if __name__ == '__main__':
	main()

# Remember install openpyxl package before trying to run
