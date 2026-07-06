from colorama import Fore, Style, init
import socket
from concurrent.futures import ThreadPoolExecutor

init()

def banner():
    print(Fore.WHITE + r"""
██████╗  ██████╗ ██████╗ ████████╗
██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝
██████╔╝██║   ██║██████╔╝   ██║
██╔═══╝ ██║   ██║██╔══██╗   ██║
██║     ╚██████╔╝██║  ██║   ██║
╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝

███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗
██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝

""" + Style.RESET_ALL)

    print(Fore.GREEN + """
╔═════════════════════════════════════════════════════╗
║                                                     ║
║  Developer Name : Adnan Abid                        ║
║  Instagram      : @hackersec_lab                    ║
║  Purpose        : Cybersecurity Learning & Testing  ║
║  Version        : 1.0                               ║
║                                                     ║
╚═════════════════════════════════════════════════════╝
""" + Style.RESET_ALL)

banner()


# Input
target = input("Enter target (IP or website): ")

# Clean input (remove http/https)
target = target.replace("http://", "").replace("https://", "").split("/")[0]


# Port range input
try:
    start_port = int(input("Start Port (default 1): ") or 1)
    end_port = int(input("End Port (default 100): ") or 100)

except ValueError:
    print(Fore.RED + "Invalid port range!" + Style.RESET_ALL)
    exit()


# Resolve target
try:
    target_ip = socket.gethostbyname(target)

except socket.gaierror:
    print(Fore.RED + "Invalid target!" + Style.RESET_ALL)
    exit()


print(
    Fore.CYAN +
    f"\n🔍 Scanning {target} ({target_ip}) "
    f"from port {start_port} to {end_port}...\n"
    + Style.RESET_ALL
)


# Scan function
def scan_port(port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)

            result = s.connect_ex((target_ip, port))

            if result == 0:
                try:
                    service = socket.getservbyport(port)

                except:
                    service = "Unknown"

                print(
                    Fore.GREEN +
                    f"[+] Port {port} OPEN ({service})"
                    + Style.RESET_ALL
                )

    except:
        pass



# Multi-threading
threads = 50

with ThreadPoolExecutor(max_workers=threads) as executor:
    executor.map(scan_port, range(start_port, end_port + 1))


print(Fore.YELLOW + "\n✅ Scanning finished." + Style.RESET_ALL)