import time,threading
from var_dump import var_dump
def do_test():
    time.sleep(2)
    return {'STATUS':1,'RSSI':-55,'ADDR':'12:34:45:56','MODEL':'e','LEFT':3,'RIGHT':2,'CASE':'f','CHARGE':'b'}
def prints():
    for i in range(16):
        print(str(i)+str(time.time()))
        time.sleep(1)
'''
a = threading.Thread(target=prints)
#a.daemon = True
t = a.start()
var_dump(t)
'''
def check_bt():
    import eventlet  # 导入eventlet这个模块
    import get_status
    t1 = time.time()
    print(t1)
    eventlet.monkey_patch()  # 必须加这条代码
    with eventlet.Timeout(0.1, False):  # 设置超时时间为2秒
        #get_status.fetch_status()
        print('BT off')
        t2 = time.time()
        print(t2)
        print('----' + str(t2 - t1))
        return False
        #print('没有跳过这条输出')
    print('bt on')
    t2 = time.time()
    print(t2)
    print('----'+str(t2-t1))
    return True
check_bt()