from pynput import keyboard,mouse
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from assets.main_ui import Ui_MainWindow
import os
import time

TIME_BASE=1000

_keyboard=keyboard.Controller()
_mouse=mouse.Controller()

key_names=['A','E1','E2','E3','SH']

config_ini = QSettings('config.ini',QSettings.IniFormat)
if not os.path.exists('config.ini'):
    for name in key_names:
        config_ini.setValue(name,0)
    config_ini.setValue("IS_DENGING",0)
    
config_ini.setValue("IS_BLOCK",0)

def wait(t_val):
    time.sleep(t_val)

def getValues():
    return [int(config_ini.value(name)) for name in key_names]
    
def on_activate(mode):
    if config_ini.value("IS_DENGING")==0 and config_ini.value("IS_BLOCK")==0:
        config_ini.setValue("IS_DENGING",1)
        A,E1,E2,E3,SH=getValues()
        if mode=='A':
            _mouse.click(mouse.Button.left)
        else:
            _keyboard.tap('e')
        wait(eval(mode)/TIME_BASE)
        _mouse.click(mouse.Button.right)
        wait(SH/TIME_BASE)
        _keyboard.tap(keyboard.Key.space)
    config_ini.setValue("IS_DENGING",0)

def on_block():
    val=(int(config_ini.value("IS_BLOCK"))+1) % 2
    config_ini.setValue("IS_BLOCK",val)
    

class Worker(QRunnable):
    def __init__(self) -> None:
        super().__init__()
        self.listener=keyboard.GlobalHotKeys({
            'f': lambda: on_activate(mode='A'),
            'r': lambda: on_activate(mode='E1'),
            't': lambda: on_activate(mode='E2'),
            'v': lambda: on_activate(mode='E3'),
            '<alt>': on_block,
        })
        
    @Slot()  
    def run(self):
        self.listener.start()
        self.listener.join()
        
    
    
class Window(Ui_MainWindow,QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.threadpool = QThreadPool()
        self.Bstart.clicked.connect(self.start)
        self.Bstop.clicked.connect(self.stop)
        self.Bstop.setDisabled(True)
        self.paras.setEnabled(False)
        self.Block.clicked.connect(self.changeState)
        self.showValues()
        self.setChanges()      
        
    def showValues(self):
        for index,val in enumerate(getValues()):
            obj=getattr(self,'v'+key_names[index])
            obj.setValue(val) 
    
    def start(self):
        self.Bstart.setDisabled(True)
        self.Bstop.setDisabled(False)
        self.worker = Worker()
        self.threadpool.start(self.worker)
        
    def stop(self):
        self.Bstop.setDisabled(True)
        self.Bstart.setDisabled(False)
        if hasattr(self,'worker'):
            self.worker.listener.stop()
        
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
        
        
if __name__=="__main__":
    app=QApplication()
    window=Window()
    window.show()
    app.exec()
    
