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
btn1=2  #number key 1
btn2=3	#number key 2 
btn3=4	#number key 3
btn4=5	#number key 4
btn5=6	#number key 5
btn6=7	#number key 6

while True:
    joy_x_value=ReadChannel(joy_x)
#print ("Joy X Value:{}".format(joy_x_value))
device.emit(uinput.ABS_X,joy_x_value,syn=False)

joy_y_value=ReadChannel(joy_y)
#print ("Joy Y Value:{}".format(joy_y_value))
device.emit(uinput.ABS_Y,joy_y_value)

btn1=ReadChannel(btn1)
if coin_value==1:
    #print ("Button Pressed {}".format(btn1_value))
    device.emit_click(uinput.KEY_1,1)
		
btn2_value=ReadChannel(btn2)
if ls_value==1:
    #print ("Button Pressed {}".format(btn2_value))
    device.emit_click(uinput.KEY_2,1)
    
	  
btn3_value=ReadChannel(btn3)
if rs_value==1:
    #print ("Button Pressed {}".format(btn3_value))
    device.emit_click(uinput.KEY_3,1)
    
		
	  
btn4_value=ReadChannel(btn4)
if esc_value==1:
    #print ("Button Pressed {}".format(btn4_value))
    device.emit_click(uinput.KEY_4,1)
   
	  
btn5_value=ReadChannel(btn5)
if sel_value==1:
    #print ("Button Pressed {}".format(sel_value))
    device.emit_click(uinput.KEY_5,1)


	  
btn6_value=ReadChannel(btn6)
if start_value==1:
    #print ("Button Pressed {}".format(btn6_value))
    device.emit_click(uinput.KEY_6,1)
    
time.sleep(0.020) 
