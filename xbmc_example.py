# import the XBMC libraries so we can use the controls and functions of XBMC
import xbmc, xbmcgui
 
# name and create our window 
class BlahMainWindow(xbmcgui.Window): 
    # and define it as self
    def __init__(self):
    # add picture control to our window (self) with a hardcoded path name to picture
    self.addControl(xbmcgui.ControlImage(0,0,720,480, '/home/jon/teste.jpg'))
 
# store our window as a short variable for easy of use
W = BlahMainWindow()
# run our window we created with our background jpeg image
W.doModal()
# after the window is closed, Destroy it.
del W
# a principio essa tranqueira vai em /home/pi/.xbmc/scripts e tem que ser chamada a partir de um autoexec.py que vai /home/pi/.xbmc/userdata
# para criar addon: http://www.element14.com/community/community/raspberry-pi/blog/2013/06/26/creating-an-xmbc-plugin-hello-world
