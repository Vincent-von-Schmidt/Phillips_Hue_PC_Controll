from zeroconf import ServiceBrowser, Zeroconf
import time


class MyListener:

    def remove_service(self, zeroconf, type, name):
        print("Service %s removed" % (name,))

    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        print("Service %s added, service info: %s" % (name, info))

    def update_service(self):
        pass


zeroconf = Zeroconf()
listener = MyListener()
browser = ServiceBrowser(zeroconf, "_hue._tcp.local.", listener)
time.sleep(2)
zeroconf.close()
