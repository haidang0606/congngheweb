import requests



# data = {}
# data['suppliername'] = 'dang '
# data['contactname'] = 'thyg'
# data['address'] = '05 tien son 10'
# data['city'] = 'Da nang'
# data['postalcode'] = 'Charlotte Cooper'
# data['country'] = 'VN'
# data['phone'] = '(084) 986 716'

# res = requests.put('http://192.168.0.23:5000/suppliers/4',json=data)
# print(res.text)





#----------------------

# data = {}
# data['lastname'] = 'hieu'
# data['firstname'] = 'huu'
# data['birthdate'] = '1998-06-06'
# data['photo'] = 'photo'
# data['notes'] = 'photo'

# res = requests.post('http://192.168.0.23:5000/add_employees',json=data)
# print(res.text)
#------------------------------------------------------
# data = {}
# data['customerid'] = 'nha2'
# data['employeeid'] = '7'
# data['orderdate'] = '1998-06-6'
# data['shipperid'] = '20 red bull20 red bull20 red bull'

# res = requests.post('http://192.168.0.23:5000/add_orders',json=data)
# print(res.text)
#---------------------------------
# data = {}
# data['shippername'] = 'khanh'
# data['phone'] = '(012) 678 789'


# res = requests.put('http://192.168.0.23:5000/shippers/4',json=data)
# print(res.text)



#---------------------------
# data = {}
# data['productname'] = 'khanh'
# data['supplierid'] = '7'
# data['categoryid'] = '7'
# data['unit'] = '20 red bull'
# data['price'] = '78'

# res = requests.put('http://192.168.0.23:5000/products/4',json=data)
# print(res.text)


# data = {}
# data['customername'] = 'an'
# data['contactname'] = '235465'
# data['address'] = '21 phan trong tue'
# data['city'] = 'dn'
# data['postalcode'] = '6000'
# data['country'] = 'Gia lai'

# res = requests.post('http://172.20.10.9:5000/add_customer',json=data)
# print(res.text)
#--------------------------------------
# data = {}
# data['customername'] = 'dang'
# data['contactname'] = '03034'
# data['address'] = 'to huu'
# data['city'] = 'dn'
# data['postalcode'] = '5000'
# data['country'] = 'Quang Tri'

# res = requests.put('http://192.168.0.23:5000/customer/3',json=data)
# print(res.text)
#------------------------------
res = requests.delete('http://192.168.0.23:5000/suppliers/4')
print(res.text)

#--------------------