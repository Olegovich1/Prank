import webbrowser
import time


num_tabs = 10 #кол-во окон


url = "https://www.yyyyyyy.info/" #ссылка на сайт


for _ in range(num_tabs):
    webbrowser.open(url)
    time.sleep(0.01) #время перед открытием новой вкладки