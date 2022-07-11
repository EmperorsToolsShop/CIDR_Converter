import ipaddress
from concurrent.futures import ThreadPoolExecutor
import colorama
import os
import platform
import subprocess


try:
    os.mkdir("Results")
except:
    pass


def clear():
    if platform.system() == "Windows":
        subprocess.call('cls', shell=True)
    else:
        subprocess.call('clear', shell=True)


reset = colorama.Style.RESET_ALL
groen = colorama.Fore.GREEN
geel = colorama.Fore.YELLOW
cyan = colorama.Fore.CYAN
blauw = colorama.Fore.BLUE
roood = colorama.Fore.RED


def converter(range_list):
    count = 0
    cidr = range_list.replace("\n", "").replace("\r", "")
    net = ipaddress.IPv4Network(cidr)
    try:
        formater = '%s-%s' % (net[0], net[-1])
        opslaan = open('Results/cidr2netrange.txt', 'a')
        opslaan.write(str(formater + '\n'))
        opslaan.close()
        for ip in net:
            count += 1
            with open("Results/ips_list.txt", "a") as ip_lijst:
                ip_lijst.write(str(ip) + "\n")
                ip_lijst.close()
        print(f"{geel}RANGE{reset}{roood}: {reset}{groen}{formater}{reset} {geel}CIDR{reset}{roood}: {reset}{groen}{cidr}"
              f"{reset} {geel}IPS_IN_RANGE{reset}{roood}: {reset}{groen}{str(count)}")
        full_info = formater + " | " + " IPS IN RANGE: " + str(count)
        aiai = open("Results/ip_counts.txt", 'a')
        aiai.write(full_info + "\n")
        aiai.close()
    except KeyboardInterrupt:
        print(f"{roood}BROOOOO WHY ARE WE STOPPING{reset}{geel}?!{reset} {blauw}#{reset}@{roood}#{reset}${geel}!{reset}")
        pass
    except (ipaddress.AddressValueError, ipaddress.NetmaskValueError):
        print(f"{roood}BROOOOO Go clean your list{reset}{geel}?!{reset} {blauw}#{reset}@{roood}#{reset}${geel}!{reset}")
        pass


if __name__ == '__main__':
    clear()
    print(f"{geel}EMPERORSTOOLSSHOP LEGACY{reset}\n{groen}https://t.me/freshesleadsb{reset}\n{geel}"
          f"@Freshesleadsever{reset}\n{groen}Threaded Mass cidr converter v2{reset}")
    try:
        range_list = open(input(f"{geel}Give me your cidr list{reset}{groen}?{reset}{geel}:{reset} "), 'r')
        clear()
        threads = int(input(f"{geel}How many threads{reset}{groen}?{reset}{geel}:{reset} "))
        clear()
        with ThreadPoolExecutor(max_workers=threads) as starten:
            starten.map(converter, range_list)
    except KeyboardInterrupt:
        print(f"{roood}BROOOOO WHY ARE WE STOPPING{reset}{geel}?!{reset} {blauw}#{reset}@{roood}#{reset}${geel}!{reset}")
        exit()
    except (FileExistsError, FileNotFoundError):
        print(f"{roood}BRO GIVE ME A CDIR LIST{reset}{geel}!{reset} {blauw}#{reset}@{roood}#{reset}${geel}!{reset}")
        exit()
