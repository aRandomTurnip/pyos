item = str(input("What would you like to install?\n0. App\n1. OS\n"))
if item == "0":
 apps.append(requests.get("https://arandomturnip.github.io/pyos/apps/") + str(input("Package Name:\n")
 appnames.append(input("App Display Name:\n")
elif itme == "1":
 oscodes.append(requests.get("https://arandomturnip.github.io/pyos/os/") + str(input("Package Name:\n")
 osnames.append(input("OS Display Name:\n")
