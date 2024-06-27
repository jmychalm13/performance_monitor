from tkinter import *
import psutil
import math
import speedtest


def usage():
    cpu_count = psutil.cpu_count()
    cpu_count_label.config(text=cpu_count)

    cpu_usage = psutil.cpu_percent(1)
    cpu_usage_label.config(text=cpu_usage)
    cpu_usage_label.after(100, usage)

    ram_count = math.floor(psutil.virtual_memory()[0] / 1000000000)
    ram_count_text = str(ram_count) + "GB"
    ram_count_label.config(text=ram_count_text)

    ram_usage = psutil.virtual_memory()[2]
    ram_usage_text = str(ram_usage) + "%"
    ram_usage_label.config(text=ram_usage_text)

    avail_ram = math.floor(psutil.virtual_memory()[1] / 1000000000)
    avail_ram_text = str(avail_ram) + "GB"
    ram_avail_label.config(text=avail_ram_text)


def internet_speed():
    st = speedtest.Speedtest()
    download_speed = str(math.floor(st.download() / 1000000)) + "Mb/s"
    upload_speed = str(math.floor(st.upload() / 1000000)) + "Mb/s"
    ping = str(st.results.ping) + "MS"
    upload_label.config(text=upload_speed)
    download_label.config(text=download_speed)
    ping_label.config(text=ping)


root = Tk()
root.geometry("1300x1080")
root.title("CPU Status")

# code for cpu count
cpu_count_label = Label(root, text="0")
cpu_count_label.grid(row=0, column=0)
l1 = Label(root, text="CPUs")
l1.grid(row=1, column=0)

# cpu usage
cpu_usage_label = Label(root, text="0")
cpu_usage_label.grid(row=0, column=1)
l2 = Label(root, text="CPU Usage in Percentage")
l2.grid(row=1, column=1)

# Total RAM
ram_count_label = Label(root, text="0")
ram_count_label.grid(row=0, column=2)
l3 = Label(root, text="Total RAM")
l3.grid(row=1, column=3)

# RAM Percent Usage
ram_usage_label = Label(root, text="0")
ram_usage_label.grid(row=0, column=3)
l4 = Label(root, text="Percentage Used")
l4.grid(row=1, column=4)

# RAM Available
ram_avail_label = Label(root, text="0")
ram_avail_label.grid(row=0, column=4)
l5 = Label(root, text="Available RAM")
l5.grid(row=1, column=4)

speed_button = Button(root, text="Test Internet Speed", command=internet_speed)
speed_button.grid(row=3, column=0)

download_label = Label(root, text="0 Mb/s")
download_label.grid(row=3, column=1)
l6 = Label(root, text="Download Speed")
l6.grid(row=4, column=1)

upload_label = Label(root, text="0 Mb/s")
upload_label.grid(row=3, column=2)
l7 = Label(root, text="Upload Speed")
l7.grid(row=4, column=2)

ping_label = Label(root, text="0 Mb/s")
ping_label.grid(row=3, column=3)
l8 = Label(root, text="Ping")
l8.grid(row=4, column=3)

usage()
root.mainloop()
