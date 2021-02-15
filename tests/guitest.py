'''
Created on 18 Jan 2021

@author: smeghammer
'''

import sys
import os
from PySide import QtGui, QtCore
from ftplib import FTP

class MainWindowWidget(QtGui.QWidget):
    """
    Subclass the widget and add a button to load images. 
    
    Alternatively set up dragging and dropping of image files onto the widget
    """

    def __init__(self):
        super(MainWindowWidget, self).__init__()

        # Button that allows loading of images
        self.load_button = QtGui.QPushButton("Load image")
        self.load_button.clicked.connect(self.load_image_but)

        # Image viewing region
        self.lbl = QtGui.QLabel(self)

        # A horizontal layout to include the button on the left
        layout_button = QtGui.QHBoxLayout()
        layout_button.addWidget(self.load_button)
        layout_button.addStretch()

        # A Vertical layout to include the button layout and then the image
        layout = QtGui.QVBoxLayout()
        layout.addLayout(layout_button)
        layout.addWidget(self.lbl)

        self.setLayout(layout)

        # Enable dragging and dropping onto the GUI
        self.setAcceptDrops(True)

        self.show()


    def upload(self):
        print(self.fname) 
        
        '''
        for ID Games:
        '''
        ftp = FTP('archives.gamers.org','anonymous','smeghammer@live.com')
        ftp.cwd('pub/idgames/incoming')
        
        res = ftp.retrlines('LIST')
        print(res)
        #text mode
        with open(self.fname, 'rb') as text_file:
            try:
        #         ftp.storlines('STOR '+file, text_file)
                ftp.storbinary('STOR '+self.fname.split(os.path.sep)[-1], text_file)
            except Exception as ex:
                print(ex)
        
        ftp.quit()





    def load_image_but(self):
        """
        Open a File dialog when the button is pressed
        :return:
        """
        
        #Get the file location
        self.fname, _ = QtGui.QFileDialog.getOpenFileName(self, 'Open file')
        # Load the image from the location
#         self.load_image()

#             self.load_image()
        self.upload()

    def load_image(self):
        """
        Set the image to the pixmap
        :return:
        """
        pixmap = QtGui.QPixmap(self.fname)
        pixmap = pixmap.scaled(500, 500, QtCore.Qt.KeepAspectRatio)
        self.lbl.setPixmap(pixmap)

    # The following three methods set up dragging and dropping for the app
    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls:
            e.accept()
        else:
            e.ignore()

    def dragMoveEvent(self, e):
        if e.mimeData().hasUrls:
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        """
        Drop files directly onto the widget
        File locations are stored in fname
        :param e:
        :return:
        """
        if e.mimeData().hasUrls:
            e.setDropAction(QtCore.Qt.CopyAction)
            e.accept()
            # Workaround for OSx dragging and dropping
            for url in e.mimeData().urls():
#                 if op_sys == 'Darwin':
#                     fname = str(NSURL.URLWithString_(str(url.toString())).filePathURL().path())
#                 else:
#                     fname = str(url.toLocalFile())
                fname = str(url.toLocalFile())

            self.fname = fname
#             self.load_image()
            self.upload()
        else:
            e.ignore()

# Run if called directly
if __name__ == '__main__':
    # Initialise the application
    app = QtGui.QApplication(sys.argv)
    # Call the widget
    ex = MainWindowWidget()
    sys.exit(app.exec_())