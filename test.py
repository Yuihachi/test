import requests
import datetime
import urllib3,json
import test_IP


#for i in range(1,100) :
#  pass

class ERP_TEST():
  def __init__(self,IP,USER,PASS):
    urllib3.disable_warnings()
    self.ISE_IP = IP
    self.ISE_USER = USER
    self.ISE_PASS = PASS
    self.HEADER_JSON = {'accept': 'application/json',
                        'Content-Type': 'application/json',
                        'Authorization': 'Basic ZXJzLXVzcjI6UGFzc3dvcmQxMjM0',
                        'Cache-Control': 'no-cache'}

    self.HEADER_XML = {'accept': 'application/xml',
                        'Content-Type': 'application/xml',
                        'Authorization': 'Basic ZXJzLXVzcjI6UGFzc3dvcmQxMjM0',
                        'Cache-Control': 'no-cache'}

    self.AUTH_INFO = (self.ISE_USER,self.ISE_PASS)

  def create_networkdevice(self,radius_pass = '1234'):
    data_json = {
      "NetworkDevice": {
        "name": 'test1',
        "description": "test1",
        "profileName": "Cisco",
        "coaPort": 1700,
        "authenticationSettings": {
          "networkProtocol": "RADIUS",
          "radiusSharedSecret": radius_pass,
          "enableKeyWrap": False,
          "dtlsRequired": False,
          "keyInputFormat": "ASCII",
          "messageAuthenticatorCodeKey": "",
          "enableMultiSecret": "false"
        },
        "NetworkDeviceIPList": [
          {
            "ipaddress": '10.10.10.10',
            "mask": 32
          }
        ],
        "NetworkDeviceGroupList": [
          "Device Type#All Device Types",
          "IPSEC#Is IPSEC Device#No",
          "Location#All Locations"
        ],
      },

      "NetworkDevice": {
        "name": 'test2',
        "description": "test2",
        "profileName": "Cisco",
        "coaPort": 1700,
        "authenticationSettings": {
          "networkProtocol": "RADIUS",
          "radiusSharedSecret": radius_pass,
          "enableKeyWrap": False,
          "dtlsRequired": False,
          "keyInputFormat": "ASCII",
          "messageAuthenticatorCodeKey": "",
          "enableMultiSecret": "false"
        },
        "NetworkDeviceIPList": [
          {
            "ipaddress": '20.20.20.20',
            "mask": 32
          }
        ],
        "NetworkDeviceGroupList": [
          "Device Type#All Device Types",
          "IPSEC#Is IPSEC Device#No",
          "Location#All Locations"
        ],
      }
    }






    data_test = test_IP.test()

    count = 0
    count2 = 0
    for data in data_test :
      count += 1
      conn = requests.put(url="https://{}:9060/ers/config/networkdevice/bulk/submit".format(self.ISE_IP), headers=self.HEADER_XML,
                           auth=self.AUTH_INFO,
                           #data=json.dumps(data_json),
                           data=data,
                           verify=False)


      print(conn.text)
      print(conn.status_code)



#data_xml ="<NetworkDevice><name>test</name></NetworkDevice>"




#conn2 = requests.post(url=test,herader=test,auth=test,data=test,verify=False)


#svr_token = requests.post(url=svr_url,)
#conn = requests.post(url=test,auth=svr_auth,verify=False)
#conn = requests.post(url=svr_url,auth=svr_auth,headers=headers_json,data=json.dumps(data_json),verify=False)
#conn = requests.post(url=svr_url,auth=svr_auth,headers=headers_xml,data=data_xml,verify=False)
#conn = requests.get(url="https://192.168.112.155/admin/API/apiGateway/get",auth=svr_auth,verify=False)





#re = conn
#print(re)


ISE_TEST = ERP_TEST('192.168.112.160','admin','Ringnet1!')

start = datetime.datetime.now()

#test_list = test2.IP_LIST()
#print('Hi: ' + str(len(test_list)))


'''
for i in range(0,100) :
    for j in range(0,100) :
        test_list.append("1.1.{}.{}".format(i,j))
'''

#for aa in test_list:
ISE_TEST.create_networkdevice()



#for i in range(1,200):
#  ISE_TEST.create_networkdevice('bbb' + str(i) ,'9.9.10.' + str(i))

print(datetime.datetime.now() - start)
#print("End :" + )







