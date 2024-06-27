import psutil
import math
import speedtest

print(psutil.cpu_count())

print(psutil.virtual_memory()[0])

# getting the network speed
st = speedtest.Speedtest()
# print("download", st.download())
# print("upload", st.upload())
