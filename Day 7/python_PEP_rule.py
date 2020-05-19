menu = {
    'momo':19,
    'chowmein':16,
    'pasta':14,
    'Thupka':10,
    'chicken_chilli':20,
    'sausage':18
}
def __init__(self):
    self.order = str
    self.menu = str

def customer_order(self,order_list):
    order_list=[]
    order=input("enter your order followed by comma: ")
    order_list.append(order)
    return order_list

def check_order(self, menu, order_list):
    for i in menu:
        if order_list in menu:
            prompt = f'We have {i} in menu.'
            print(prompt)
customer_order(self,order_list = 'pasta')
check_order(self, menu, order_list='pasta')