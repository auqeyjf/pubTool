#=================================
# author: changlong.zang
#   date: 2014-03-18
#=================================
import sip, re
from PyQt4 import QtCore, QtGui, uic
from maya.OpenMayaUI import MQtUtil
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+

def getMayaWindow():
    '''
    return maya window by Qt object..
    '''
    ptr = MQtUtil.mainWindow()
    if ptr is not None:
        return sip.wrapinstance(long(ptr),QtCore.QObject)




def loadUi(uiPath):
    '''
    read an ui file, get two classes to returm..
    '''
    windowClass, baseClass = uic.loadUiType(uiPath)
    return windowClass, baseClass




def windowExists(parent, name):
    '''
    get named window, if window exists, return false; if not, return true..
    '''
    if not parent:return False
    
    wnd = parent.findChild(QtGui.QMainWindow, name)
    if wnd:
        wnd.show()
        wnd.showNormal()
        wnd.activateWindow()
        return True
    else:
        return False





def getChildrenWindows(parent):
    '''
    get object's children windows..
    '''
    windows = []
    if not parent:return windows
    
    for child in parent.children():
        if not hasattr(child, 'isWindow'):
            continue
        if not child.isWindow():
            continue
        windows.append(child)

    return windows




def cleanChildrenWindows(parent, delete=True):
    '''
    delete window's child window...
    '''
    if not parent:return
    
    for child in getChildrenWindows(parent):
        if not re.match('RootUI|Plugcmds', child.__module__):
            continue
        child.close()
        if not delete:continue
        child.deleteLater()





def warning(message='Yes ? ?'):
    '''
    show a window, you chose Yes or NO..
    '''
    warningUI = WarningDialog(message, getMayaWindow())
    return bool(warningUI.result())



    

class WarningDialog(QtGui.QDialog):
    '''
    build a widget for warning function..
    '''
    def __init__(self, message='', parent=None):
        super(WarningDialog, self).__init__(parent)
        self.setupUi(self)
        self.label.setText(message)
        self.exec_()
    
    
    def setupUi(self, Dialog):
        ICON_PATH = '//bjserver2/Temp Documents/Foley/Tools/icons'
        
        Dialog.setWindowTitle('Warning !!!')
        Dialog.setObjectName('Dialog')
        Dialog.resize(200, 150)
        #--+--+--+--+
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        #--+--+--+--+
        self.btn_title = QtGui.QPushButton(Dialog)
        self.btn_title.setEnabled(False)
        self.btn_title.setStyleSheet('background-color: rgba(0, 0, 0, 0);')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap('%s/frb_exclamation.png'%ICON_PATH), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.btn_title.setIcon(icon)
        self.btn_title.setIconSize(QtCore.QSize(35, 35))
        self.verticalLayout.addWidget(self.btn_title)
        #--+--+--+--+
        self.label = QtGui.QLabel('? ? ?', Dialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName('label')
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout.addItem(QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding))
        #--+--+--+--+
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.addItem(QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
        #--+--+--+--+
        self.btn_OK = QtGui.QPushButton('OK', Dialog)
        self.btn_OK.setMinimumSize(QtCore.QSize(100, 25))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap('%s/frb_ok.png'%ICON_PATH), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_OK.setIcon(icon1)
        self.btn_OK.setIconSize(QtCore.QSize(22, 22))
        self.horizontalLayout.addWidget(self.btn_OK)
        #--+--+--+--+
        self.btn_Cancle = QtGui.QPushButton('Cancle', Dialog)
        self.btn_Cancle.setMinimumSize(QtCore.QSize(100, 25))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap('%s/frb_cancle.png'%ICON_PATH), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Cancle.setIcon(icon2)
        self.btn_Cancle.setIconSize(QtCore.QSize(15, 15))
        self.horizontalLayout.addWidget(self.btn_Cancle)
        #--+--+--+--+
        self.verticalLayout.addLayout(self.horizontalLayout)
        #--+--+--+--+
        QtCore.QObject.connect(self.btn_OK,     QtCore.SIGNAL('clicked()'), Dialog.accept)
        QtCore.QObject.connect(self.btn_Cancle, QtCore.SIGNAL('clicked()'), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)