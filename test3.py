IP_LIST = []

for i in range(1,101):
    for j in range (1,6):
        a = i
        b = i
        c = i
        d = i
        p = j

        e = """<ns8:networkdevice description="Network Device {}{}" id="id_{}{}" name="networkDevice{}{}">
                <NetworkDeviceIPList>
                    <NetworkDeviceIP>
                        <ipaddress>1.1.{}.{}</ipaddress>
                        <mask>32</mask>
                    </NetworkDeviceIP>
                </NetworkDeviceIPList>
                <NetworkDeviceGroupList>
                    <NetworkDeviceGroup>Location#All Locations</NetworkDeviceGroup>
                    <NetworkDeviceGroup>Device Type#All Device Types</NetworkDeviceGroup>
                </NetworkDeviceGroupList>
                <profileName>Cisco</profileName>
            </ns8:networkdevice>""".format(i,j,i,j,i,j,i,j)

        print(e)

