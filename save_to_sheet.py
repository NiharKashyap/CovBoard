import gspread
from gspread_dataframe import set_with_dataframe
import pandas as pd

class Gsheet:
	def __init__(self):
		self.gc = gspread.service_account(filename = 'covidsheet-321103-b9d13b3d3ca1.json')
		self.sh = self.gc.open("Covid_Jorhat")
		self.ws = self.sh.worksheet('Sheet1') 

	def save_sheet(self, list):
		df = pd.DataFrame(list)
		data_list = df.values.tolist()
		self.ws.append_rows(data_list)
		#set_with_dataframe(self.ws, df)
	