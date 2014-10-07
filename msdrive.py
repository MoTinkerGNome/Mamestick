#!/usr/bin/python
 
import spidev
import time
import os
import uinput

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
 
# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data

device =uinput.Device([uinput.BTN_JOYSTICK,
                      uinput.ABS_X+(0,1023,0,0),
                      uinput.ABS_Y+(0,1023,0,0),
					  uinput.KEY_1,
					  uinput.KEY_2,
					  uinput.KEY_3,
					  uinput.KEY_4,
					  uinput.KEY_5,
					  uinput.KEY_6,
                      ])



joy_y=0 #abs_y+ value 
joy_x=1	#abs_x+ value
coin=2  #number key 1
ls=3	#number key 2 
rs=4	#number key 3
esc=5	#number key 4
sel=6	#number key 5
start=7	#number key 6

while True:
    joy_x_value=ReadChannel(joy_x)
		#print ("Joy X Value:{}".format(joy_x_value))
		device.emit(uinput.ABS_X,joy_x_value,syn=False)

    joy_y_value=ReadChannel(joy_y)
		#print ("Joy Y Value:{}".format(joy_y_value))
		device.emit(uinput.ABS_Y,joy_y_value)

    coin_value=ReadChannel(coin)
    if coin_value==1:
		#print ("Button Pressed {}".format(coin_value))
		device.emit_click(uinput.KEY_1,1)
    else:
		#print ("Button Not Pressed {}".format(coin_value))
		device.emit_click(uinput.KEY_1,0)

    ls_value=ReadChannel(ls)
    if ls_value==1:
		#print ("Button Pressed {}".format(ls_value))
		device.emit_click(uinput.KEY_2,1)
    else:
		#print ("Button Not Pressed {}".format(ls_value))
		device.emit_click(uinput.KEY_2,0)
	  
	rs_value=ReadChannel(rs)
    if rs_value==1:
		#print ("Button Pressed {}".format(rs_value))
		device.emit_click(uinput.KEY_3,1)
    else:
		#print ("Button Not Pressed {}".format(rs_value))
		device.emit_click(uinput.KEY_3,0)
	  
	esc_value=ReadChannel(esc)
    if esc_value==1:
		#print ("Button Pressed {}".format(esc_value))
		device.emit_click(uinput.KEY_4,1)
    else:
		#print ("Button Not Pressed {}".format(esc_value))
		device.emit_click(uinput.KEY_4,0) 
	  
	sel_value=ReadChannel(sel)
    if sel_value==1:
		#print ("Button Pressed {}".format(sel_value))
		device.emit_click(uinput.KEY_5,1)
    else:
		#print ("Button Not Pressed {}".format(sel_value))
		device.emit_click(uinput.KEY_5,0)
	  
	start_value=ReadChannel(start)
    if start_value==1:
		#print ("Button Pressed {}".format(start_value))
		device.emit_click(uinput.KEY_6,1)
    else:
		#print ("Button Not Pressed {}".format(start_value))
		device.emit_click(uinput.KEY_6,0)
	  
    time.sleep(0.020) 
