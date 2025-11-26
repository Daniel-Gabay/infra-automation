import subprocess
import logging

class Installer:

    def install_nginx(self):
        if input("do you want to install nginx [y/n]: ").lower() == "y":
            logging.info("starting to install nginx")
            print("starting to install nginx")
            try:
                result = subprocess.run(
                    ["bash", "scripts/install_nginx.sh"],
                    check=True, text=True, capture_output=True
                )
                print("script output:")
                print(result.stdout)
                logging.info("finish install nginx")
            except subprocess.CalledProcessError as error:
                print("script failed with error:")
                print(error)
                logging.error(f"failed to install nginx: {error}")


    def install_pydantic(self):
        if input("do you want to install pydantic [y/n]: ").lower() == "y":
            logging.info("starting to install pydantic")
            print("starting to install pydantic")
            try:
                result = subprocess.run(
                    ["bash", "scripts/install_pydantic.sh"],
                    check=True, text=True, capture_output=True
                )
                print("script output:")
                print(result.stdout)
                logging.info("finish install pydantic")
            except subprocess.CalledProcessError as error:
                print("script failed with error:")
                print(error)
                logging.error(f"failed to install pydantic: {error}")