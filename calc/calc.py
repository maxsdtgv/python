from my1 import my11
import threading


qwe = my11.But_print()
qwe1 = my11.But_print()

t1 = threading.Thread(target=qwe.start)
t2 = threading.Thread(target=qwe1.start)
t1.start()
t2.start()
t1.join()
t2.join()