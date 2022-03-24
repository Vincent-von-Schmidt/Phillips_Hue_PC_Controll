import requests
import json
import subprocess


# def search_bridge() -> str:
#     instances = subprocess.run(["dns-sd", "-B", "_hue._tcp", "local."], capture_output=True).stdout.decode()
#     name = instances.split()
#
#     bridge_id = subprocess.run(["dns-sd", "-L", f"{name}", "_hue._tcp", "local."], capture_output=True).stdout.decode()
#
#     bridge_ip = subprocess.run(["dns-sd", "-G", f"{bridge_id}.local"], capture_output=True).stdout.decode()
#
#     return bridge_ip


def create_user(ip: str, name: str, app_name: str) -> list:
    return json.loads(
        requests.post(
            url=f"http://{ip}/api/",
            json={"devicetype": f"{app_name}#{name}"}
        ).text)


class PHueLight:
    def __init__(self, ip: str, user: str, light: int):
        self.url = f"http://{ip}/api/{user}/lights/{light}/"

    def set_state(self, data: dict) -> None:
        requests.put(url=f"{self.url}state/", json=data)

    def set_name(self, name: str) -> None:
        requests.put(url=self.url, json={"name": name})

    def get_state(self) -> dict:
        return self.get_info()["state"]

    def get_name(self) -> str:
        return str(self.get_info()["name"])

    def get_info(self) -> dict:
        return json.loads(requests.get(self.url).text)

    def get_capabilities(self) -> dict:
        colormode = json.loads(requests.get(self.url).text)["capabilities"]["control"]
        return_dict = {
            "ct": False,
            "color": False
        }

        if "colorgamut" in colormode:
            return_dict["color"] = True

        if "ct" in colormode:
            return_dict["ct"] = True

        return return_dict


if __name__ == "__main__":
    print(search_bridge())
