from PneumoCVUTFBMI.DeviceLoader import DeviceLoader

dl = DeviceLoader()

b1 = dl.getBoard1()
b2 = dl.getBoard2()
b3 = dl.getBoard3()
b4 = dl.getBoard4()
b5 = dl.getBoard5()

b1.on()
b2.on()
b3.on()
b4.on()
b5.on()

b1.stop()
b2.stop()
b3.stop()
b4.stop()
b5.stop()