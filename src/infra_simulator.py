import logging
import json
from machine import Machine
from installer import Installer
installer = Installer()


logging.basicConfig(
level=logging.INFO,
format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
handlers=[
        logging.FileHandler("src/logs/infra.log")]
)

#move the fancion to a class
def save_machine(machine):
    file_path="src/configs/instances.json"
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    data.append(machine.model_dump())


    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
        logging.info("Machine saved successfully.")
    print("Machine saved successfully")


def read_user():
    #enter machine name
        name = input("enter machine name: ").strip()
        while len(name) >=8:
            logging.warning(f"user entered too long machine {name}")
            print("your name is more than 8 characters. try again.")
            name = input("enter machine name: ").strip()


        #os must be ubuntu, centos or windows
        os = input("Operating System (ubuntu, centos, windows): ").strip()
        while os not in ["ubuntu", "centos", "windows"]:
            logging.warning(f"user entered not valid os {os}")
            print(f"the {os} is not valid os. try again. ")
            os = input("Operating System (ubuntu, centos, windows): ").strip()


    #cpu must be a positive number
        cpu = input("CPU cores (number): ").strip()
        while not cpu.isdigit() or int (cpu) <= 0 or int(cpu) > 64:
            print("CPU must be a positive number. ")
            logging.warning(f"user entered a invalid {cpu} number ")
            cpu = input("CPU cores (number) ").strip()
        cpu = int (cpu)


    #RAM must be a positive number
        ram = (input("RAM size (GB): ")).strip()
        while not ram.isdigit() or int (ram) <= 0 or int(ram) > 32:
            print("RAM must be a positive number. ")
            logging.warning(f"user entered a invalid {ram} number")
            ram = input("RAM size (GB): ").strip()
        ram = int (ram)


        return Machine(name=name,
                       os=os,
                       cpu=cpu,
                       ram=ram
                       )


logging.info("program started")
print("starting the program . . .")

installer.install_nginx()
installer.install_pydantic()

#read from user and save it
machine = read_user()
save_machine(machine)

logging.info("program finished succssfully ")
print("ended the program ")

