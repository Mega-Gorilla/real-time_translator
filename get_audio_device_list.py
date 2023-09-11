from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities
import sounddevice as sd

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
        
def find_device_id_SD(target_name):
    devices = sd.query_devices()
    for device in devices:
        if target_name in device['name'] :
            return device['index']
    return None
        
if __name__ == "__main__":
    #show_all_audio_device()
    #Return_VB_Audio_ID()
    device_id = find_device_id_SD("CABLE Output (VB-Audio Virtual Cable)")
    print(device_id)