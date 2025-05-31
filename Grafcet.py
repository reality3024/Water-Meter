import requests
import json
import firebase_admin
from firebase_admin import credentials, auth
import requests

all_device = ["device_esp32_A", "device_esp32_B"]

class Main():
	def __init__(self):
		self.X0 = self.X10 = self.X20 = self.X210 = self.X220 = self.X2210 = self.X30 = self.X310 = self.X3120 = self.X3130 = self.X3140 = self.X320 = 1
		self.X1 = self.X11 = self.X12 = self.X2 = self.X21 = self.X211 = self.X212 = self.X22 = self.X221 = self.X2211 = self.X2212 = self.X222 = self.X3 = self.X31 = self.X311 = self.X312 = self.X3121 = self.X3122 = self.X3123 = self.X313 = self.X3131 = self.X3132 = self.X3133 = self.X314 = self.X3141 = self.X3142 = self.X315 = self.X32 = self.X321 = self.X322 = self.X33 = 0
		self.errorMessage = ""
		self.device = ""
		self.meter1 = 0
		self.meter2 = 0
		self.meter3 = 0
		self.device_uid = ""
		self.custom_token = ""
		self.firebase_api_key = ""
		self.resp = ""
		self.id_token = ""
		self.firebase_url = ""
		self.data = ""
		self.write_resp = ""
		print("X0 = %d,X1 = %d,X2 = %d,X3 = %d"%(self.X0 ,self.X1 ,self.X2 ,self.X3 ))
		while(True):
			self.datapath0()
			self.grafcet0()
			if(self.X0 == 0 and self.X1 == 0 and self.X2 == 0 and self.X3 == 0):
				return
			print("X0 = %d,X1 = %d,X2 = %d,X3 = %d"%(self.X0 ,self.X1 ,self.X2 ,self.X3 ))
	def grafcet0(self):

		if self.X0 == 1 and 1:
			self.X0 = 0
			self.X1 = 1
			return


		if self.X1 == 1 and 1:
			self.X1 = 0
			self.X2 = 1
			return


		if self.X2 == 1 and 1:
			self.X2 = 0
			self.X3 = 1
			return


		if self.X3 == 1 and self.X322:
			self.X3 = 0
			# self.X0 = 1
			return

	def grafcet1(self):

		if self.X10 == 1 and 1:
			self.X10 = 0
			self.X11 = 1
			return


		if self.X11 == 1 and 1:
			self.X11 = 0
			self.X12 = 1
			return


		if self.X12 == 1 and 1:
			self.X12 = 0
			self.X10 = 1
			return

	def grafcet2(self):

		if self.X20 == 1 and 1:
			self.X20 = 0
			self.X21 = 1
			return


		if self.X21 == 1 and 1:
			self.X21 = 0
			self.X22 = 1
			return


		if self.X22 == 1 and 1:
			self.X22 = 0
			self.X20 = 1
			return

	def grafcet21(self):

		if self.X210 == 1 and 1:
			self.X210 = 0
			self.X211 = 1
			return


		if self.X211 == 1 and 1:
			self.X211 = 0
			self.X212 = 1
			return


		if self.X212 == 1 and 1:
			self.X212 = 0
			self.X210 = 1
			return

	def grafcet22(self):

		if self.X220 == 1 and 1:
			self.X220 = 0
			self.X221 = 1
			return


		if self.X221 == 1 and 1:
			self.X221 = 0
			self.X222 = 1
			return


		if self.X222 == 1 and 1:
			self.X222 = 0
			self.X220 = 1
			return

	def grafcet221(self):

		if self.X2210 == 1 and 1:
			self.X2210 = 0
			self.X2211 = 1
			return


		if self.X2211 == 1 and 1:
			self.X2211 = 0
			self.X2212 = 1
			return


		if self.X2212 == 1 and 1:
			self.X2212 = 0
			self.X2210 = 1
			return

	def grafcet3(self):

		if self.X30 == 1 and self.X3:
			self.X30 = 0
			self.X31 = 1
			return


		if self.X31 == 1 and self.X315:
			self.X31 = 0
			self.X32 = 1
			return


		if self.X32 == 1 and self.X322:
			self.X32 = 0
			self.X33 = 1
			return


		if self.X33 == 1 and self.X33:
			self.X33 = 0
			self.X30 = 1
			return

	def grafcet31(self):

		if self.X310 == 1 and self.X31:
			self.X310 = 0
			self.X311 = 1
			return


		if self.X311 == 1 and self.X311:
			self.X311 = 0
			self.X312 = 1
			return


		if self.X312 == 1 and self.X3123:
			self.X312 = 0
			self.X313 = 1
			return


		if self.X313 == 1 and self.X3133:
			self.X313 = 0
			self.X314 = 1
			return


		if self.X314 == 1 and self.X3142:
			self.X314 = 0
			self.X315 = 1
			return


		if self.X315 == 1 and self.X315:
			self.X315 = 0
			self.X310 = 1
			return

	def grafcet312(self):

		if self.X3120 == 1 and self.X312:
			self.X3120 = 0
			self.X3121 = 1
			return


		if self.X3121 == 1 and self.X3121:
			self.X3121 = 0
			self.X3122 = 1
			return


		if self.X3122 == 1 and self.X3122:
			self.X3122 = 0
			self.X3123 = 1
			return


		if self.X3123 == 1 and self.X3123:
			self.X3123 = 0
			self.X3120 = 1
			return

	def grafcet313(self):

		if self.X3130 == 1 and self.X313:
			self.X3130 = 0
			self.X3131 = 1
			return


		if self.X3131 == 1 and self.X3131:
			self.X3131 = 0
			self.X3132 = 1
			return


		if self.X3132 == 1 and self.X3132:
			self.X3132 = 0
			self.X3133 = 1
			return


		if self.X3133 == 1 and self.X3133:
			self.X3133 = 0
			self.X3130 = 1
			return

	def grafcet314(self):

		if self.X3140 == 1 and self.X314:
			self.X3140 = 0
			self.X3141 = 1
			return


		if self.X3141 == 1 and self.X3141:
			self.X3141 = 0
			self.X3142 = 1
			return


		if self.X3142 == 1 and self.X3142:
			self.X3142 = 0
			self.X3140 = 1
			return

	def grafcet32(self):

		if self.X320 == 1 and self.X32:
			self.X320 = 0
			self.X321 = 1
			return


		if self.X321 == 1 and self.X321:
			self.X321 = 0
			self.X322 = 1
			return


		if self.X322 == 1 and self.X322:
			self.X322 = 0
			self.X320 = 1
			return

	def datapath0(self):
		if self.X0 == 1:
			self.action()
		if self.X1 == 1:
			self.A1()
		if self.X2 == 1:
			self.A2()
		if self.X3 == 1:
			self.A3()
	def datapath1(self):
		if self.X10 == 1:
			self.action()
		if self.X11 == 1:
			self.A11()
		if self.X12 == 1:
			self.A12()
	def datapath2(self):
		if self.X20 == 1:
			self.action()
		if self.X21 == 1:
			self.A21()
		if self.X22 == 1:
			self.A22()
	def datapath21(self):
		if self.X210 == 1:
			self.action()
		if self.X211 == 1:
			self.A211()
		if self.X212 == 1:
			self.A212()
	def datapath22(self):
		if self.X220 == 1:
			self.action()
		if self.X221 == 1:
			self.A221()
		if self.X222 == 1:
			self.A222()
	def datapath221(self):
		if self.X2210 == 1:
			self.action()
		if self.X2211 == 1:
			self.A2211()
		if self.X2212 == 1:
			self.A2212()
	def datapath3(self):
		if self.X30 == 1:
			self.action()
		if self.X31 == 1:
			self.update_database()
		if self.X32 == 1:
			self.exception_handler()
		if self.X33 == 1:
			self.end()
	def datapath31(self):
		if self.X310 == 1:
			self.action()
		if self.X311 == 1:
			self.Initialize_firebase_SDK()
		if self.X312 == 1:
			self.verify_device()
		if self.X313 == 1:
			self.identity_verification()
		if self.X314 == 1:
			self.update_result()
		if self.X315 == 1:
			self.end()
	def datapath312(self):
		if self.X3120 == 1:
			self.action()
		if self.X3121 == 1:
			self.save_identification_result()
		if self.X3122 == 1:
			self.check_deviceExist()
		if self.X3123 == 1:
			self.end()
	def datapath313(self):
		if self.X3130 == 1:
			self.action()
		if self.X3131 == 1:
			self.create_customToken()
		if self.X3132 == 1:
			self.get_IDToken()
		if self.X3133 == 1:
			self.end()
	def datapath314(self):
		if self.X3140 == 1:
			self.action()
		if self.X3141 == 1:
			self.apply_putRequest()
		if self.X3142 == 1:
			self.end()
	def datapath32(self):
		if self.X320 == 1:
			self.action()
		if self.X321 == 1:
			self.print_ErrorMessage()
		if self.X322 == 1:
			self.end()
	def action(self):
		print("action activate !!\n")
	def A1(self):
		print("A1 activate !!\n")
		self.datapath1()
		self.grafcet1()
		print("X10 = %d,X11 = %d,X12 = %d"%(self.X10,self.X11,self.X12))
	def A2(self):
		print("A2 activate !!\n")
		self.datapath2()
		self.grafcet2()
		print("X20 = %d,X21 = %d,X22 = %d"%(self.X20,self.X21,self.X22))
	def A3(self):
		print("A3 activate !!\n")
		self.datapath3()
		self.grafcet3()
		print("X30 = %d,X31 = %d,X32 = %d,X33 = %d"%(self.X30,self.X31,self.X32,self.X33))
	def action(self):
		print("action activate !!\n")
	def A11(self):
		print("A11 activate !!\n")
	def A12(self):
		print("A12 activate !!\n")
	def action(self):
		print("action activate !!\n")
	def A21(self):
		print("A21 activate !!\n")
		self.datapath21()
		self.grafcet21()
		print("X210 = %d,X211 = %d,X212 = %d"%(self.X210,self.X211,self.X212))
	def A22(self):
		print("A22 activate !!\n")
		self.datapath22()
		self.grafcet22()
		print("X220 = %d,X221 = %d,X222 = %d"%(self.X220,self.X221,self.X222))
	def action(self):
		print("action activate !!\n")
	def A211(self):
		print("A211 activate !!\n")
	def A212(self):
		print("A212 activate !!\n")
	def action(self):
		print("action activate !!\n")
	def A221(self):
		print("A221 activate !!\n")
		self.datapath221()
		self.grafcet221()
		print("X2210 = %d,X2211 = %d,X2212 = %d"%(self.X2210,self.X2211,self.X2212))
	def A222(self):
		print("A222 activate !!\n")
	def action(self):
		print("action activate !!\n")
	def A2211(self):
		print("A2211 activate !!\n")
	def A2212(self):
		print("A2212 activate !!\n")
	def action(self):
		print("action activate !!\n")
	def update_database(self):
		print("update_database activate !!\n")
		self.datapath31()
		self.grafcet31()
		print("X310 = %d,X311 = %d,X312 = %d,X313 = %d,X314 = %d,X315 = %d"%(self.X310,self.X311,self.X312,self.X313,self.X314,self.X315))
	def exception_handler(self):
		print("exception_handler activate !!\n")
		self.datapath32()
		self.grafcet32()
		print("X320 = %d,X321 = %d,X322 = %d"%(self.X320,self.X321,self.X322))
	def end(self):
		print("end activate !!\n")
	def action(self):
		print("action activate !!\n")
	def Initialize_firebase_SDK(self):
		print("Initialize_firebase_SDK activate !!\n")
		# 初始化 Firebase Admin SDK（只需一次）
		cred = credentials.Certificate("./water-meter-24a2f-firebase-adminsdk-fbsvc-219db20b96.json")
		firebase_admin.initialize_app(cred)
	def verify_device(self):
		print("verify_device activate !!\n")
		self.datapath312()
		self.grafcet312()
		print("X3120 = %d,X3121 = %d,X3122 = %d,X3123 = %d"%(self.X3120,self.X3121,self.X3122,self.X3123))
	def identity_verification(self):
		print("identity_verification activate !!\n")
		self.datapath313()
		self.grafcet313()
		print("X3130 = %d,X3131 = %d,X3132 = %d,X3133 = %d"%(self.X3130,self.X3131,self.X3132,self.X3133))
	def update_result(self):
		print("update_result activate !!\n")
		self.datapath314()
		self.grafcet314()
		print("X3140 = %d,X3141 = %d,X3142 = %d"%(self.X3140,self.X3141,self.X3142))
	def end(self):
		print("end activate !!\n")
	def action(self):
		print("action activate !!\n")
	def save_identification_result(self):
		self.meter1 = 1111
		self.meter2 = 2222
		self.meter3 = 3333
		print("save_identification_result activate !!\n")
	def check_deviceExist(self):
		self.device = "device_esp32_B"
		if self.device == None or self.device not in all_device:
			self.errorMessage = "Please check your input device is correct and is in device list"
		print("check_deviceExist activate !!\n")
	def end(self):
		print("end activate !!\n")
	def action(self):
		print("action activate !!\n")
	def create_customToken(self):
		self.device_uid = "device_esp32_B"
		# 1. 建立自訂登入 Token（由後台控制）
		self.custom_token = auth.create_custom_token(self.device_uid).decode("utf-8")
		# 2. 用 custom token 登入 Firebase，拿到 idToken（REST API 寫入要用這個）
		self.firebase_api_key = "AIzaSyALCNtqCR8K87M__lWnwig506Fg92GRBdI"
		self.resp = requests.post(
            f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithCustomToken?key={self.firebase_api_key}",
            json={"token": self.custom_token, "returnSecureToken": True}
        )
		print("create_customToken activate !!\n")
	def get_IDToken(self):
		self.id_token = self.resp.json()["idToken"]
		print("get_IDToken activate !!\n")
	def end(self):
		print("end activate !!\n")
	def action(self):
		print("action activate !!\n")
	def apply_putRequest(self):
		self.firebase_url = f"https://water-meter-24a2f-default-rtdb.firebaseio.com/meters/{self.device_uid}.json?auth={self.id_token}"
		data = {
            "meter1": self.meter1,
            "meter2": self.meter2,
            "meter3": self.meter3
        }
		self.write_resp = requests.put(self.firebase_url, json=data)
		if self.write_resp.status_code == 200:
			print(f"Successfully save {self.write_resp.text} to firebase")
		else:
			self.errorMessage = f"Status code return {self.write_resp.status_code}"
		print("apply_putRequest activate !!\n")
	def end(self):
		print("end activate !!\n")
	def action(self):
		print("action activate !!\n")
	def print_ErrorMessage(self):
		if self.errorMessage != "":
			print(self.errorMessage)
		print("print_ErrorMessage activate !!\n")
	def end(self):
		print("end activate !!\n")
if __name__ == '__main__':
	Main()