from pynput import keyboard,mouse
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from assets.main_ui import Ui_MainWindow
import os
import time

# 单位ms
TIME_BASE=1000

_keyboard=keyboard.Controller()
_mouse=mouse.Controller()

key_names=['A','E1','E2','E3','SH']
key_triggers=['x','r','t','v','alt_gr']

config_ini = QSettings('config.ini',QSettings.IniFormat)
if not os.path.exists('config.ini'):
    for name,trg in zip(key_names,key_triggers):
        config_ini.setValue(name,0)
        config_ini.setValue(name+'_key',trg)
else:
    for index,name in enumerate(key_names):
        key_triggers[index]=config_ini.value(name+'_key')
        

def IsSameKey(key,char):
    if hasattr(keyboard.Key,char):
        return key==getattr(keyboard.Key,char)
    else:
        return key==keyboard.KeyCode(char=char)

def getValues():
    return [int(config_ini.value(name)) for name in key_names]
    
class Window(Ui_MainWindow,QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.Bstart.clicked.connect(self.start)
        self.Bstop.clicked.connect(self.stop)
        self.Bstop.setDisabled(True)
        self.paras.setEnabled(False)
        self.Block.clicked.connect(self.changeState)
        self.showValues()
        self.setChanges()  
        self.IsBlocking=False
        self.IsDenging=False
        
    def showValues(self):
        for index,val in enumerate(getValues()):
            obj=getattr(self,'v'+key_names[index])
            obj.setValue(val) 
    
    def start(self):
        self.Bstart.setDisabled(True)
        self.Bstop.setDisabled(False)
        self.listener = keyboard.Listener(on_release=self.on_release)
        self.listener.start()
        
    def stop(self):
        self.Bstop.setDisabled(True)
        self.Bstart.setDisabled(False)
        if hasattr(self,'listener'):
            self.listener.stop()
        
    def closeEvent(self, event) -> None:
        self.stop()
        return super().closeEvent(event)
    
    def setChanges(self):
        for name in key_names:
            obj=getattr(self,'v'+name)
            obj.valueChanged.connect(self.rewrite_config)
    
    def rewrite_config(self):
        obj=self.sender()
        name=obj.objectName().replace('v','')
        config_ini.setValue(name,obj.value())
        
    def changeState(self):
        if self.paras.isEnabled():
            self.paras.setEnabled(False)
        else:
            self.paras.setEnabled(True)
            
    def on_release(self,key):
        if IsSameKey(key,key_triggers[-1]):
            self.IsBlocking=not self.IsBlocking
        self.info.setText("{0}屏蔽,{1}".format('已' if self.IsBlocking else '未',key))
        if not self.IsBlocking:
            for index,trg in enumerate(key_triggers[:-1]):
                if IsSameKey(key,trg):
                    self.on_activate(mode=key_names[index])
        
    def on_activate(self,mode):
        if not self.IsDenging:
            self.IsDenging=True
            A,E1,E2,E3,SH=getValues()
            if mode=='A':
                _mouse.click(mouse.Button.left)
            else:
                _keyboard.tap('e')
            time.sleep(eval(mode)/TIME_BASE)
            _mouse.click(mouse.Button.right)
            time.sleep(SH/TIME_BASE)
            _keyboard.tap(keyboard.Key.space)
        self.IsDenging=False
             
        
if __name__=="__main__":
    app=QApplication()
    window=Window()
    window.show()
    app.exec()
    
