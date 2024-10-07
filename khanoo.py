'''
</> Scripy Coded By > DARK LMNx9
</> Special Gift For > 2.7k+ Subscribers
</> Channel > t.me/DARK_TEAM_LMNx9
'''

import requests,os,sys,rich,string,json,time
from rich import print_json as Lj
from rich import print as LMX

class LMNxMAIL:
    os.system("clear")
    LMX("""[bold green]
░█████╗░██╗░░██╗░██████╗░█████╗░███╗░░██╗
██╔══██╗██║░░██║██╔════╝██╔══██╗████╗░██║
███████║███████║╚█████╗░███████║██╔██╗██║
██╔══██║██╔══██║░╚═══██╗██╔══██║██║╚████║
██║░░██║██║░░██║██████╔╝██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝ 
[red1]>>_____________________________________""")
    
    def __init__(self):
        url = "https://www.1secmail.com/api/v1/"
        params = {
            'action': "genRandomMailbox",
            'count': "1"}
        headers = {
            'User-Agent': "okhttp/3.9.1",
            'Accept-Encoding': "gzip"}
        try:LMNx9 = requests.get(url, params=params, headers=headers).text
        except:
            LMX("[bold cyan]</> [red1] Internet Connection Error..!")
            sys.exit()
        self.email = LMNx9.split('["')[1].split('"]')[0]
        LMX(f"[bold cyan]</> [bold yellow]Generated Email :[bold green] {self.email}")
        LMX(46*"[red1]-")
        
    def LMNxRefresh(self):
        name = self.email.split('@')[0]
        dom = self.email.split('@')[1]
        url = "https://www.1secmail.com/api/v1/"
        params = {
            'action': "getMessages",
            'login': name,
            'domain': dom}
        headers = {
            'User-Agent': "okhttp/3.9.1",
            'Accept-Encoding': "gzip"}
        LMNx9 = requests.post(url, params=params, headers=headers).json()
        LMX(46*"[red1]-")
        Lj(data=LMNx9);LMX(46*"[red1]-")

    def start(self):
        try:
            while True:
                input("</> Enter to refresh & [Ctrl+Z] For Exit >")
                self.LMNxRefresh()
        except KeyboardInterrupt:
            LMX("[red1]</> Something Wrong ![bold yellow] Exiting...!")
            time.sleep(1.5)
            sys.exit()

if __name__ in "__main__":LMNxMAIL().start()
