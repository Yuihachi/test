

def test() :
    initial_list = []
    initial = ''' Start {} End '''

    test_list = []


    xml_list = []



    xml_ = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <ns8:networkDeviceBulkRequest operationType="create" resourceMediaType="vnd.com.cisco.ise.network.networkdevice.1.1+xml" xmlns:ns6="sxp.ers.ise.cisco.com" xmlns:ns5="trustsec.ers.ise.cisco.com" xmlns:ns8="network.ers.ise.cisco.com" xmlns:ns7="anc.ers.ise.cisco.com" xmlns:ers="ers.ise.cisco.com" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:ns4="identity.ers.ise.cisco.com">
        <ns8:resourcesList>
            {}
        </ns8:resourcesList>
    </ns8:networkDeviceBulkRequest>'''




    xml_device = """<ns8:networkdevice description="Network Device{}" id="id_{}" name="networkDevice{}">
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
                </ns8:networkdevice>"""


    # Ok
    device_count = 1
    for i in range(1,101) :
        for j in range(1,101) :
            initial_list.append(xml_device.format(device_count,device_count,device_count,i,j))
            device_count += 1
            #print("count2 : {}          count : {}".format(i,j))




    count = 0
    count2 = 0
    temp = ''


    for aa in initial_list :
        count += 1
        temp += aa
        #print(count)
        if count % 500 == 0 :
            test_list.append(temp)
            count2 += 1
            count = 0
            #print(count2)
            temp = ''

        #print("count2 : {}          count : {}".format(count2,count))

    print(test_list)

    for i in test_list :
        xml_list.append(xml_.format(i))



    return xml_list

test()
