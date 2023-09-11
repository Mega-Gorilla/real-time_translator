from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def show_all_audio_device():

    # 接続されているオーディオエンドポイントデバイスのリストを取得
    endpoints = AudioUtilities.GetAllDevices()
    for endpoint in endpoints:
        print("ID: {}, Name: {}".format(endpoint.id, endpoint.FriendlyName))

def Return_VB_Audio_ID():

    # 接続されているオーディオエンドポイントデバイスのリストを取得
    endpoints = AudioUtilities.GetAllDevices()
    for endpoint in endpoints:
        if "CABLE Output (VB-Audio Virtual Cable)" in f"{endpoint.FriendlyName}":
            return endpoint.id
        
if __name__ == "__main__":
    #show_all_audio_device()
    Return_VB_Audio_ID()