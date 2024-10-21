import requests

r =  requests.get('https://www.google.com/search?q=mct+oil&rlz=1C1UEAD_enCA1104CA1104&oq=mct&gs_lcrp=EgZjaHJvbWUqDggAEEUYJxg7GIAEGIoFMg4IABBFGCcYOxiABBiKBTIPCAEQRRg5GIMBGLEDGIAEMg0IAhAuGK8BGMcBGIAEMgoIAxAuGLEDGIAEMg0IBBAAGIMBGLEDGIAEMgYIBRBFGDwyBggGEEUYPTIGCAcQRRg80gEIMTM4MGowajSoAgCwAgE&sourceid=chrome&ie=UTF-8')

print(r.text)