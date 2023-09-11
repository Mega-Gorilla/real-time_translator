#main.py
from get_audio_device_list import Return_VB_Audio_ID,find_device_id_SD
from azure_transrate import azure_translate
from azure_speech_handler import SpeechHandler
from rich import print
from multiprocessing import Process,Event,Queue
import tkinter as tk
from tkinter import ttk, font
import sounddevice as sd
import os, asyncio, time, sys
import openai
#keys
openai.api_key = os.getenv("OPENAI_API_KEY")
speech_key = os.getenv("AZURE_API_KEY")
azure_transrate_key = os.getenv("AZURE_Transrate_KEY")
region = "japaneast"

#settings
record_langage='en-US' # https://learn.microsoft.com/ja-jp/azure/ai-services/speech-service/language-support?tabs=stt
from_langage='en' # https://learn.microsoft.com/ja-jp/azure/ai-services/translator/language-support
to_langage='ja' # https://learn.microsoft.com/ja-jp/azure/ai-services/translator/language-support
Stream_Speaker_Name = 'LG Ultra HD'

def tkinter_thread(q):
    def update_text_boxes():
        while not q.empty():
            item = q.get()
            left_text.insert(tk.END, f"{item[0]}\n")
            right_text.insert(tk.END, f"{item[1]}\n")
            left_text.see(tk.END)
            right_text.see(tk.END)
        root.after(1000, update_text_boxes)
    
    root = tk.Tk()
    root.title("リアルタイム 翻訳くん")

    frame = ttk.Frame(root, padding=10)
    frame.pack(fill=tk.BOTH, expand=True)

    customFont = font.Font(size=16)

    left_text = tk.Text(frame, wrap=tk.WORD, width=30, height=10, font=customFont)
    left_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    right_text = tk.Text(frame, wrap=tk.WORD, width=30, height=10, font=customFont)
    right_text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    
    update_text_boxes()

    root.mainloop()

def stream_mic(mic_id,speaker_id,stop_event):
    def callback(indata, outdata, frames, time, status):
        outdata[:] = indata
    with sd.Stream(device=(mic_id, speaker_id), callback=callback):
        while not stop_event.is_set():
            time.sleep(1)

async def handle_results(queue,q):
    while True:
        result = await queue.get()
        translate=azure_translate(result,from_langage,to_langage,azure_transrate_key,region)
        q.put([translate,result])
        print(f"{translate} / {result}")
        
        queue.task_done()

async def main():

    queue = asyncio.Queue()
    handler = SpeechHandler(queue,speech_key, region,language=record_langage,mic_id=mic_id,debug=False,TimeoutMs='4000')

    # Start the streaming task in another process
    stop_event= Event()
    p = Process(target=stream_mic, args=(mic_id_stream, speaker_id_stream,stop_event))
    gui = Process(target=tkinter_thread, args=(q, ))
    gui.start()
    p.start()

    # Start a task to handle results
    asyncio.create_task(handle_results(queue,q))

    while True:
        asyncio.create_task(handler.from_mic())
        await asyncio.sleep(1)

if __name__ == "__main__":

    mic_id = Return_VB_Audio_ID()
    mic_id_stream = find_device_id_SD("CABLE Output (VB-Audio Virtual")
    speaker_id_stream = find_device_id_SD(Stream_Speaker_Name)

    q=Queue()
    asyncio.run(main())