import requests
import json
import firebase_admin
from firebase_admin import credentials, auth
import requests

all_device = ["device_esp32_A", "device_esp32_B"]

def single_device():
    url = "https://water-meter-24a2f-default-rtdb.firebaseio.com/meters.json"
    data = {
        "meter1": 1,
        "meter2": 2,
        "meter3": 3
    }

    res = requests.put(url, data=json.dumps(data))
    print(res.status_code, res.text)

def multiple_device_with_auth(device = None):
    if device != None and device in all_device:    
        # 初始化 Firebase Admin SDK（只需一次）
        cred = credentials.Certificate("./water-meter-24a2f-firebase-adminsdk-fbsvc-61b4d8cc55.json")
        firebase_admin.initialize_app(cred)

        # 指定裝置的 UID，例如 "device_esp32_A"
        device_uid = device

        # 1. 建立自訂登入 Token（由後台控制）
        custom_token = auth.create_custom_token(device_uid).decode("utf-8")

        # 2. 用 custom token 登入 Firebase，拿到 idToken（REST API 寫入要用這個）
        firebase_api_key = "AIzaSyALCNtqCR8K87M__lWnwig506Fg92GRBdI"
        resp = requests.post(
            f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithCustomToken?key={firebase_api_key}",
            json={"token": custom_token, "returnSecureToken": True}
        )
        id_token = resp.json()["idToken"]

        # 3. 使用 REST API 寫入對應節點
        firebase_url = f"https://water-meter-24a2f-default-rtdb.firebaseio.com/meters/{device_uid}.json?auth={id_token}"
        data = {
            "meter1": 3,
            "meter2": 55,
            "meter3": 88
        }
        write_resp = requests.put(firebase_url, json=data)

        # print("寫入結果：", write_resp.status_code, write_resp.text)
        if write_resp.status_code == 200:
            return f"Successfully save {write_resp.text} to firebase"
        else:
            return f"Status code return {write_resp.status_code}"
    else:
        return "Please check your input device is correct and is in device list"

def main():
    device = "device_esp32_B"
    result = multiple_device_with_auth(device)
    print(result)

if __name__ == '__main__':
    main()
