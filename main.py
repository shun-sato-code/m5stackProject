from m5stack import *
from m5ui import *
from uiflow import *
import module

import imu

setScreenColor(0x222222)


stop = None

gps = module.get(module.GPS, (17, 16))
imu0 = imu.IMU()
title0 = M5Title(title="Title", x=3, fgcolor=0xFFFFFF, bgcolor=0x0000FF)
label0 = M5TextBox(8, 53, "Text", lcd.FONT_DejaVu24, 0xFFFFFF, rotate=0)
label1 = M5TextBox(8, 107, "Text", lcd.FONT_DejaVu24, 0xFFFFFF, rotate=0)
label2 = M5TextBox(8, 163, "Text", lcd.FONT_DejaVu24, 0xFFFFFF, rotate=0)
label3 = M5TextBox(8, 214, "Text", lcd.FONT_DejaVu24, 0xFFFFFF, rotate=0)
rectangle0 = M5Rect(132, 105, 30, 30, 0xFFFFFF, 0xFFFFFF)



def buttonA_wasPressed():
  global stop
  if stop == True:
    timerSch.run('timer1', 100, 0x00)
    stop = False
  else:
    timerSch.stop('timer1')
    stop = True
    label0.hide()
    label1.hide()
    label2.hide()
    label3.hide()
    title0.setTitle('END')
  pass
btnA.wasPressed(buttonA_wasPressed)

@timerSch.event('timer1')
def ttimer1():
  global stop
  label0.show()
  label1.show()
  label2.show()
  label3.show()
  title0.setTitle(str((str(((str('Time : ') + str((gps.gps_time))))) + str(((str('  PQ : ') + str((gps.pos_quality))))))))
  label0.setText(str((str('Y : ') + str((imu0.acceleration[1])))))
  label1.setText(str((str('Roll : ') + str((imu0.ypr[2])))))
  label2.setText(str((str('Lon : ') + str((gps.longitude)))))
  label3.setText(str((str('Lat : ') + str((gps.latitude)))))
  pass


stop = True
title0.hide()
label0.setColor(0xffffff)
label1.setColor(0xffffff)
label2.setColor(0xffffff)
label3.setColor(0xffffff)
setScreenColor(0x000000)
title0.setBgColor(0x000000)
title0.hide()
gps.set_time_zone(9)
