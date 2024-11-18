# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiWqYIDF.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QFormLayout, QGridLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QSpinBox, QStatusBar, QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(981, 740)
        MainWindow.setStyleSheet(u"QPushButton[flat=\"true\"] {\n"
"    border: 2px solid #808080; /* Gray border */\n"
"    border-radius: 6px;        /* Rounded corners */\n"
"    padding: 6px 12px;         /* Inner padding */\n"
"    color: #333333;            /* Dark gray text */\n"
"    font-size: 14px;           /* Font size */\n"
"}\n"
"\n"
"QPushButton[flat=\"true\"]:hover {\n"
"    border-color: #606060;     /* Darker gray on hover */\n"
"}\n"
"\n"
"QPushButton[flat=\"true\"]:pressed {\n"
"    color: #000000;            /* Black text when pressed */\n"
"}\n"
"")
        self.actionExport_mdrt = QAction(MainWindow)
        self.actionExport_mdrt.setObjectName(u"actionExport_mdrt")
        self.actionImport_mdrt = QAction(MainWindow)
        self.actionImport_mdrt.setObjectName(u"actionImport_mdrt")
        self.actionDark = QAction(MainWindow)
        self.actionDark.setObjectName(u"actionDark")
        self.actionLight = QAction(MainWindow)
        self.actionLight.setObjectName(u"actionLight")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainTab = QTabWidget(self.centralwidget)
        self.mainTab.setObjectName(u"mainTab")
        self.mainTab.setGeometry(QRect(-1, 0, 981, 711))
        self.packDetailsTab = QWidget()
        self.packDetailsTab.setObjectName(u"packDetailsTab")
        self.formLayoutWidget = QWidget(self.packDetailsTab)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(340, 90, 271, 171))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.packNameLabel = QLabel(self.formLayoutWidget)
        self.packNameLabel.setObjectName(u"packNameLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.packNameLabel)

        self.packName = QLineEdit(self.formLayoutWidget)
        self.packName.setObjectName(u"packName")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.packName)

        self.packNamespaceLabel = QLabel(self.formLayoutWidget)
        self.packNamespaceLabel.setObjectName(u"packNamespaceLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.packNamespaceLabel)

        self.packNamespace = QLineEdit(self.formLayoutWidget)
        self.packNamespace.setObjectName(u"packNamespace")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.packNamespace)

        self.packAuthorLabel = QLabel(self.formLayoutWidget)
        self.packAuthorLabel.setObjectName(u"packAuthorLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.packAuthorLabel)

        self.packAuthor = QLineEdit(self.formLayoutWidget)
        self.packAuthor.setObjectName(u"packAuthor")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.packAuthor)

        self.packDescriptionLabel = QLabel(self.formLayoutWidget)
        self.packDescriptionLabel.setObjectName(u"packDescriptionLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.packDescriptionLabel)

        self.packDescription = QLineEdit(self.formLayoutWidget)
        self.packDescription.setObjectName(u"packDescription")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.packDescription)

        self.packCMDPrefixLabel = QLabel(self.formLayoutWidget)
        self.packCMDPrefixLabel.setObjectName(u"packCMDPrefixLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.packCMDPrefixLabel)

        self.packCMDPrefix = QLineEdit(self.formLayoutWidget)
        self.packCMDPrefix.setObjectName(u"packCMDPrefix")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.packCMDPrefix)

        self.packVersionLabel = QLabel(self.formLayoutWidget)
        self.packVersionLabel.setObjectName(u"packVersionLabel")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.packVersionLabel)

        self.packVersion = QComboBox(self.formLayoutWidget)
        self.packVersion.addItem("")
        self.packVersion.setObjectName(u"packVersion")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.packVersion)

        self.packGenerate = QPushButton(self.packDetailsTab)
        self.packGenerate.setObjectName(u"packGenerate")
        self.packGenerate.setGeometry(QRect(340, 270, 271, 31))
        self.titleLabel = QLabel(self.packDetailsTab)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(350, 30, 241, 51))
        self.mainTab.addTab(self.packDetailsTab, "")
        self.blockTab = QWidget()
        self.blockTab.setObjectName(u"blockTab")
        self.formLayoutWidget_2 = QWidget(self.blockTab)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(10, 10, 361, 641))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.blockDisplayNameLabel = QLabel(self.formLayoutWidget_2)
        self.blockDisplayNameLabel.setObjectName(u"blockDisplayNameLabel")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.blockDisplayNameLabel)

        self.blockNameLabel = QLabel(self.formLayoutWidget_2)
        self.blockNameLabel.setObjectName(u"blockNameLabel")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.blockNameLabel)

        self.blockBaseBlockName = QLabel(self.formLayoutWidget_2)
        self.blockBaseBlockName.setObjectName(u"blockBaseBlockName")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.blockBaseBlockName)

        self.blockDropLabel = QLabel(self.formLayoutWidget_2)
        self.blockDropLabel.setObjectName(u"blockDropLabel")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.blockDropLabel)

        self.blockPlaceSoundLabel = QLabel(self.formLayoutWidget_2)
        self.blockPlaceSoundLabel.setObjectName(u"blockPlaceSoundLabel")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.blockPlaceSoundLabel)

        self.blockDirectionalLabel = QLabel(self.formLayoutWidget_2)
        self.blockDirectionalLabel.setObjectName(u"blockDirectionalLabel")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.blockDirectionalLabel)

        self.blockDisplayName = QLineEdit(self.formLayoutWidget_2)
        self.blockDisplayName.setObjectName(u"blockDisplayName")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.blockDisplayName)

        self.blockName = QLineEdit(self.formLayoutWidget_2)
        self.blockName.setObjectName(u"blockName")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.blockName)

        self.blockBaseBlock = QLineEdit(self.formLayoutWidget_2)
        self.blockBaseBlock.setObjectName(u"blockBaseBlock")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.blockBaseBlock)

        self.blockDrop = QLineEdit(self.formLayoutWidget_2)
        self.blockDrop.setObjectName(u"blockDrop")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.blockDrop)

        self.blockPlaceSound = QLineEdit(self.formLayoutWidget_2)
        self.blockPlaceSound.setObjectName(u"blockPlaceSound")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.blockPlaceSound)

        self.blockDirectional = QCheckBox(self.formLayoutWidget_2)
        self.blockDirectional.setObjectName(u"blockDirectional")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.blockDirectional)

        self.blockTextureButtonTop = QPushButton(self.blockTab)
        self.blockTextureButtonTop.setObjectName(u"blockTextureButtonTop")
        self.blockTextureButtonTop.setGeometry(QRect(450, 50, 50, 50))
        self.blockTextureButtonTop.setFlat(True)
        self.blockTextureButtonBack = QPushButton(self.blockTab)
        self.blockTextureButtonBack.setObjectName(u"blockTextureButtonBack")
        self.blockTextureButtonBack.setGeometry(QRect(450, 100, 50, 50))
        self.blockTextureButtonBack.setFlat(True)
        self.blockTextureButtonRight = QPushButton(self.blockTab)
        self.blockTextureButtonRight.setObjectName(u"blockTextureButtonRight")
        self.blockTextureButtonRight.setGeometry(QRect(500, 100, 50, 50))
        self.blockTextureButtonRight.setFlat(True)
        self.blockTextureButtonBottom = QPushButton(self.blockTab)
        self.blockTextureButtonBottom.setObjectName(u"blockTextureButtonBottom")
        self.blockTextureButtonBottom.setGeometry(QRect(450, 150, 50, 50))
        self.blockTextureButtonBottom.setFlat(True)
        self.blockTextureButtonLeft = QPushButton(self.blockTab)
        self.blockTextureButtonLeft.setObjectName(u"blockTextureButtonLeft")
        self.blockTextureButtonLeft.setGeometry(QRect(400, 100, 50, 50))
        self.blockTextureButtonLeft.setFlat(True)
        self.blockTextureButtonFront = QPushButton(self.blockTab)
        self.blockTextureButtonFront.setObjectName(u"blockTextureButtonFront")
        self.blockTextureButtonFront.setGeometry(QRect(550, 100, 50, 50))
        self.blockTextureButtonFront.setFlat(True)
        self.blockTextureBottom = QLabel(self.blockTab)
        self.blockTextureBottom.setObjectName(u"blockTextureBottom")
        self.blockTextureBottom.setGeometry(QRect(450, 150, 50, 50))
        self.blockTextureFront = QLabel(self.blockTab)
        self.blockTextureFront.setObjectName(u"blockTextureFront")
        self.blockTextureFront.setGeometry(QRect(550, 100, 50, 50))
        self.blockTextureRight = QLabel(self.blockTab)
        self.blockTextureRight.setObjectName(u"blockTextureRight")
        self.blockTextureRight.setGeometry(QRect(500, 100, 50, 50))
        self.blockTextureBack = QLabel(self.blockTab)
        self.blockTextureBack.setObjectName(u"blockTextureBack")
        self.blockTextureBack.setGeometry(QRect(450, 100, 50, 50))
        self.blockTextureTop = QLabel(self.blockTab)
        self.blockTextureTop.setObjectName(u"blockTextureTop")
        self.blockTextureTop.setGeometry(QRect(450, 50, 50, 50))
        self.blockTextureLeft = QLabel(self.blockTab)
        self.blockTextureLeft.setObjectName(u"blockTextureLeft")
        self.blockTextureLeft.setGeometry(QRect(400, 100, 50, 50))
        self.gridLayoutWidget = QWidget(self.blockTab)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(639, 10, 321, 341))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.blockAddButton = QPushButton(self.gridLayoutWidget)
        self.blockAddButton.setObjectName(u"blockAddButton")

        self.gridLayout.addWidget(self.blockAddButton, 1, 1, 1, 1)

        self.blockEditButton = QPushButton(self.gridLayoutWidget)
        self.blockEditButton.setObjectName(u"blockEditButton")

        self.gridLayout.addWidget(self.blockEditButton, 1, 0, 1, 1)

        self.blockRemoveButton = QPushButton(self.gridLayoutWidget)
        self.blockRemoveButton.setObjectName(u"blockRemoveButton")

        self.gridLayout.addWidget(self.blockRemoveButton, 1, 2, 1, 1)

        self.blockList = QListWidget(self.gridLayoutWidget)
        self.blockList.setObjectName(u"blockList")

        self.gridLayout.addWidget(self.blockList, 0, 0, 1, 3)

        self.blockModelLabel = QLabel(self.blockTab)
        self.blockModelLabel.setObjectName(u"blockModelLabel")
        self.blockModelLabel.setGeometry(QRect(381, 11, 34, 16))
        self.blockModel = QComboBox(self.blockTab)
        self.blockModel.addItem("")
        self.blockModel.addItem("")
        self.blockModel.setObjectName(u"blockModel")
        self.blockModel.setGeometry(QRect(420, 10, 181, 22))
        self.mainTab.addTab(self.blockTab, "")
        self.blockModelLabel.raise_()
        self.blockModel.raise_()
        self.formLayoutWidget_2.raise_()
        self.blockTextureBottom.raise_()
        self.blockTextureRight.raise_()
        self.blockTextureBack.raise_()
        self.blockTextureTop.raise_()
        self.blockTextureLeft.raise_()
        self.gridLayoutWidget.raise_()
        self.blockTextureFront.raise_()
        self.blockTextureButtonRight.raise_()
        self.blockTextureButtonBack.raise_()
        self.blockTextureButtonLeft.raise_()
        self.blockTextureButtonFront.raise_()
        self.blockTextureButtonBottom.raise_()
        self.blockTextureButtonTop.raise_()
        self.itemTab = QWidget()
        self.itemTab.setObjectName(u"itemTab")
        self.formLayoutWidget_3 = QWidget(self.itemTab)
        self.formLayoutWidget_3.setObjectName(u"formLayoutWidget_3")
        self.formLayoutWidget_3.setGeometry(QRect(10, 10, 361, 641))
        self.formLayout_3 = QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.itemDisplayNameLabel = QLabel(self.formLayoutWidget_3)
        self.itemDisplayNameLabel.setObjectName(u"itemDisplayNameLabel")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.itemDisplayNameLabel)

        self.itemDisplayName = QLineEdit(self.formLayoutWidget_3)
        self.itemDisplayName.setObjectName(u"itemDisplayName")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.itemDisplayName)

        self.itemNameLabel = QLabel(self.formLayoutWidget_3)
        self.itemNameLabel.setObjectName(u"itemNameLabel")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.itemNameLabel)

        self.itemName = QLineEdit(self.formLayoutWidget_3)
        self.itemName.setObjectName(u"itemName")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.itemName)

        self.itemBaseItemLabel = QLabel(self.formLayoutWidget_3)
        self.itemBaseItemLabel.setObjectName(u"itemBaseItemLabel")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.itemBaseItemLabel)

        self.itemBaseItem = QLineEdit(self.formLayoutWidget_3)
        self.itemBaseItem.setObjectName(u"itemBaseItem")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.itemBaseItem)

        self.itemModelLabel = QLabel(self.itemTab)
        self.itemModelLabel.setObjectName(u"itemModelLabel")
        self.itemModelLabel.setGeometry(QRect(400, 10, 49, 16))
        self.itemModel = QComboBox(self.itemTab)
        self.itemModel.addItem("")
        self.itemModel.addItem("")
        self.itemModel.setObjectName(u"itemModel")
        self.itemModel.setGeometry(QRect(445, 8, 121, 22))
        self.itemTextureLabel = QLabel(self.itemTab)
        self.itemTextureLabel.setObjectName(u"itemTextureLabel")
        self.itemTextureLabel.setGeometry(QRect(400, 60, 49, 16))
        self.itemTextureButton = QPushButton(self.itemTab)
        self.itemTextureButton.setObjectName(u"itemTextureButton")
        self.itemTextureButton.setGeometry(QRect(460, 40, 50, 50))
        self.itemTextureButton.setFlat(True)
        self.itemTexture = QLabel(self.itemTab)
        self.itemTexture.setObjectName(u"itemTexture")
        self.itemTexture.setGeometry(QRect(460, 40, 50, 50))
        self.gridLayoutWidget_2 = QWidget(self.itemTab)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(639, 10, 321, 341))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.itemAddButton = QPushButton(self.gridLayoutWidget_2)
        self.itemAddButton.setObjectName(u"itemAddButton")

        self.gridLayout_3.addWidget(self.itemAddButton, 4, 2, 1, 1)

        self.itemEditButton = QPushButton(self.gridLayoutWidget_2)
        self.itemEditButton.setObjectName(u"itemEditButton")

        self.gridLayout_3.addWidget(self.itemEditButton, 4, 1, 1, 1)

        self.itemRemoveButton = QPushButton(self.gridLayoutWidget_2)
        self.itemRemoveButton.setObjectName(u"itemRemoveButton")

        self.gridLayout_3.addWidget(self.itemRemoveButton, 4, 3, 1, 1)

        self.itemList = QListWidget(self.gridLayoutWidget_2)
        self.itemList.setObjectName(u"itemList")

        self.gridLayout_3.addWidget(self.itemList, 3, 1, 1, 3)

        self.mainTab.addTab(self.itemTab, "")
        self.formLayoutWidget_3.raise_()
        self.itemModelLabel.raise_()
        self.itemModel.raise_()
        self.itemTextureLabel.raise_()
        self.itemTexture.raise_()
        self.gridLayoutWidget_2.raise_()
        self.itemTextureButton.raise_()
        self.recipeTab = QWidget()
        self.recipeTab.setObjectName(u"recipeTab")
        self.recipeNameLabel = QLabel(self.recipeTab)
        self.recipeNameLabel.setObjectName(u"recipeNameLabel")
        self.recipeNameLabel.setGeometry(QRect(20, 30, 81, 16))
        self.recipeName = QLineEdit(self.recipeTab)
        self.recipeName.setObjectName(u"recipeName")
        self.recipeName.setGeometry(QRect(100, 30, 181, 22))
        self.recipeSubTabs = QTabWidget(self.recipeTab)
        self.recipeSubTabs.setObjectName(u"recipeSubTabs")
        self.recipeSubTabs.setGeometry(QRect(20, 70, 511, 351))
        self.craftingTab = QWidget()
        self.craftingTab.setObjectName(u"craftingTab")
        self.slot0Button = QPushButton(self.craftingTab)
        self.slot0Button.setObjectName(u"slot0Button")
        self.slot0Button.setGeometry(QRect(40, 40, 50, 50))
        self.slot0Button.setFlat(True)
        self.slot1Button = QPushButton(self.craftingTab)
        self.slot1Button.setObjectName(u"slot1Button")
        self.slot1Button.setGeometry(QRect(90, 40, 50, 50))
        self.slot1Button.setFlat(True)
        self.slot2Button = QPushButton(self.craftingTab)
        self.slot2Button.setObjectName(u"slot2Button")
        self.slot2Button.setGeometry(QRect(140, 40, 50, 50))
        self.slot2Button.setFlat(True)
        self.slot3Button = QPushButton(self.craftingTab)
        self.slot3Button.setObjectName(u"slot3Button")
        self.slot3Button.setGeometry(QRect(40, 90, 50, 50))
        self.slot3Button.setFlat(True)
        self.slot4Button = QPushButton(self.craftingTab)
        self.slot4Button.setObjectName(u"slot4Button")
        self.slot4Button.setGeometry(QRect(90, 90, 50, 50))
        self.slot4Button.setFlat(True)
        self.slot5Button = QPushButton(self.craftingTab)
        self.slot5Button.setObjectName(u"slot5Button")
        self.slot5Button.setGeometry(QRect(140, 90, 50, 50))
        self.slot5Button.setFlat(True)
        self.slot6Button = QPushButton(self.craftingTab)
        self.slot6Button.setObjectName(u"slot6Button")
        self.slot6Button.setGeometry(QRect(40, 140, 50, 50))
        self.slot6Button.setFlat(True)
        self.slot7Button = QPushButton(self.craftingTab)
        self.slot7Button.setObjectName(u"slot7Button")
        self.slot7Button.setGeometry(QRect(90, 140, 50, 50))
        self.slot7Button.setFlat(True)
        self.slot8Button = QPushButton(self.craftingTab)
        self.slot8Button.setObjectName(u"slot8Button")
        self.slot8Button.setGeometry(QRect(140, 140, 50, 50))
        self.slot8Button.setFlat(True)
        self.slot9Button = QPushButton(self.craftingTab)
        self.slot9Button.setObjectName(u"slot9Button")
        self.slot9Button.setGeometry(QRect(250, 90, 50, 50))
        self.slot9Button.setFlat(True)
        self.slot9Count = QSpinBox(self.craftingTab)
        self.slot9Count.setObjectName(u"slot9Count")
        self.slot9Count.setGeometry(QRect(250, 140, 88, 24))
        self.slot9Count.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.slot9Count.setMinimum(1)
        self.slot9Count.setMaximum(64)
        self.shapelessRadio = QRadioButton(self.craftingTab)
        self.shapelessRadio.setObjectName(u"shapelessRadio")
        self.shapelessRadio.setGeometry(QRect(50, 200, 92, 20))
        self.shapelessRadio.setAutoRepeat(False)
        self.shapelessRadio.setAutoExclusive(True)
        self.exactlyRadio = QRadioButton(self.craftingTab)
        self.exactlyRadio.setObjectName(u"exactlyRadio")
        self.exactlyRadio.setGeometry(QRect(50, 230, 161, 20))
        self.exactlyRadio.setAutoRepeat(False)
        self.exactlyRadio.setAutoExclusive(True)
        self.slot0 = QLabel(self.craftingTab)
        self.slot0.setObjectName(u"slot0")
        self.slot0.setGeometry(QRect(40, 40, 50, 50))
        self.slot1 = QLabel(self.craftingTab)
        self.slot1.setObjectName(u"slot1")
        self.slot1.setGeometry(QRect(90, 40, 50, 50))
        self.slot2 = QLabel(self.craftingTab)
        self.slot2.setObjectName(u"slot2")
        self.slot2.setGeometry(QRect(140, 40, 50, 50))
        self.slot3 = QLabel(self.craftingTab)
        self.slot3.setObjectName(u"slot3")
        self.slot3.setGeometry(QRect(40, 90, 50, 50))
        self.slot4 = QLabel(self.craftingTab)
        self.slot4.setObjectName(u"slot4")
        self.slot4.setGeometry(QRect(90, 90, 50, 50))
        self.slot5 = QLabel(self.craftingTab)
        self.slot5.setObjectName(u"slot5")
        self.slot5.setGeometry(QRect(140, 90, 50, 50))
        self.slot6 = QLabel(self.craftingTab)
        self.slot6.setObjectName(u"slot6")
        self.slot6.setGeometry(QRect(40, 140, 50, 50))
        self.slot7 = QLabel(self.craftingTab)
        self.slot7.setObjectName(u"slot7")
        self.slot7.setGeometry(QRect(90, 140, 50, 50))
        self.slot8 = QLabel(self.craftingTab)
        self.slot8.setObjectName(u"slot8")
        self.slot8.setGeometry(QRect(140, 140, 50, 50))
        self.slot9 = QLabel(self.craftingTab)
        self.slot9.setObjectName(u"slot9")
        self.slot9.setGeometry(QRect(250, 90, 50, 50))
        self.recipeSubTabs.addTab(self.craftingTab, "")
        self.slot9Count.raise_()
        self.shapelessRadio.raise_()
        self.exactlyRadio.raise_()
        self.slot0.raise_()
        self.slot1.raise_()
        self.slot2.raise_()
        self.slot3.raise_()
        self.slot4.raise_()
        self.slot5.raise_()
        self.slot6.raise_()
        self.slot7.raise_()
        self.slot8.raise_()
        self.slot9.raise_()
        self.slot6Button.raise_()
        self.slot1Button.raise_()
        self.slot2Button.raise_()
        self.slot7Button.raise_()
        self.slot0Button.raise_()
        self.slot4Button.raise_()
        self.slot3Button.raise_()
        self.slot8Button.raise_()
        self.slot9Button.raise_()
        self.slot5Button.raise_()
        self.smeltingTab = QWidget()
        self.smeltingTab.setObjectName(u"smeltingTab")
        self.smeltingInputButton = QPushButton(self.smeltingTab)
        self.smeltingInputButton.setObjectName(u"smeltingInputButton")
        self.smeltingInputButton.setGeometry(QRect(140, 90, 50, 50))
        self.smeltingInputButton.setFlat(True)
        self.smeltingOutputButton = QPushButton(self.smeltingTab)
        self.smeltingOutputButton.setObjectName(u"smeltingOutputButton")
        self.smeltingOutputButton.setGeometry(QRect(250, 90, 50, 50))
        self.smeltingOutputButton.setFlat(True)
        self.smeltingInput = QLabel(self.smeltingTab)
        self.smeltingInput.setObjectName(u"smeltingInput")
        self.smeltingInput.setGeometry(QRect(140, 90, 50, 50))
        self.smeltingOutput = QLabel(self.smeltingTab)
        self.smeltingOutput.setObjectName(u"smeltingOutput")
        self.smeltingOutput.setGeometry(QRect(250, 90, 50, 50))
        self.recipeSubTabs.addTab(self.smeltingTab, "")
        self.smeltingInput.raise_()
        self.smeltingOutput.raise_()
        self.smeltingOutputButton.raise_()
        self.smeltingInputButton.raise_()
        self.gridLayoutWidget_3 = QWidget(self.recipeTab)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(639, 10, 321, 341))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.recipeEditButton = QPushButton(self.gridLayoutWidget_3)
        self.recipeEditButton.setObjectName(u"recipeEditButton")

        self.gridLayout_4.addWidget(self.recipeEditButton, 2, 1, 1, 1)

        self.recipeAddButton = QPushButton(self.gridLayoutWidget_3)
        self.recipeAddButton.setObjectName(u"recipeAddButton")

        self.gridLayout_4.addWidget(self.recipeAddButton, 2, 2, 1, 1)

        self.recipeRemoveButton = QPushButton(self.gridLayoutWidget_3)
        self.recipeRemoveButton.setObjectName(u"recipeRemoveButton")

        self.gridLayout_4.addWidget(self.recipeRemoveButton, 2, 3, 1, 1)

        self.recipeList = QListWidget(self.gridLayoutWidget_3)
        self.recipeList.setObjectName(u"recipeList")

        self.gridLayout_4.addWidget(self.recipeList, 1, 1, 1, 3)

        self.mainTab.addTab(self.recipeTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 981, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionExport_mdrt)
        self.menuFile.addAction(self.actionImport_mdrt)

        self.retranslateUi(MainWindow)

        self.mainTab.setCurrentIndex(0)
        self.recipeSubTabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"mDirt - A Datapack Tool - v2.0", None))
        self.actionExport_mdrt.setText(QCoreApplication.translate("MainWindow", u"Export (*.mdrt)", None))
        self.actionImport_mdrt.setText(QCoreApplication.translate("MainWindow", u"Import (*.mdrt)", None))
        self.actionDark.setText(QCoreApplication.translate("MainWindow", u"Dark", None))
        self.actionLight.setText(QCoreApplication.translate("MainWindow", u"Light", None))
        self.packNameLabel.setText(QCoreApplication.translate("MainWindow", u"Pack Name", None))
        self.packName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"The Ruby Pack", None))
        self.packNamespaceLabel.setText(QCoreApplication.translate("MainWindow", u"Namespace", None))
        self.packNamespace.setPlaceholderText(QCoreApplication.translate("MainWindow", u"rubypack", None))
        self.packAuthorLabel.setText(QCoreApplication.translate("MainWindow", u"Author", None))
        self.packAuthor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"jupiterdev", None))
        self.packDescriptionLabel.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.packDescription.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Adds Rubys, Ruby Blocks, etc.", None))
        self.packCMDPrefixLabel.setText(QCoreApplication.translate("MainWindow", u"CMD Prefix", None))
        self.packCMDPrefix.setPlaceholderText(QCoreApplication.translate("MainWindow", u"589", None))
        self.packVersionLabel.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.packVersion.setItemText(0, QCoreApplication.translate("MainWindow", u"1.21.3", None))

        self.packGenerate.setText(QCoreApplication.translate("MainWindow", u"Generate Pack", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"mDirt - a tool made to help make Datapacks\n"
"Created By JupiterDev & JustJoshinDev 2024", None))
        self.mainTab.setTabText(self.mainTab.indexOf(self.packDetailsTab), QCoreApplication.translate("MainWindow", u"Datapack Details", None))
        self.blockDisplayNameLabel.setText(QCoreApplication.translate("MainWindow", u"Display Name", None))
        self.blockNameLabel.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.blockBaseBlockName.setText(QCoreApplication.translate("MainWindow", u"Base Block", None))
        self.blockDropLabel.setText(QCoreApplication.translate("MainWindow", u"Drop", None))
        self.blockPlaceSoundLabel.setText(QCoreApplication.translate("MainWindow", u"Place Sound", None))
        self.blockDirectionalLabel.setText(QCoreApplication.translate("MainWindow", u"Directional", None))
        self.blockDisplayName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ruby Ore", None))
        self.blockName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ruby_ore", None))
        self.blockBaseBlock.setPlaceholderText(QCoreApplication.translate("MainWindow", u"stone", None))
        self.blockPlaceSound.setPlaceholderText(QCoreApplication.translate("MainWindow", u"block.stone.place", None))
        self.blockDirectional.setText("")
        self.blockTextureButtonTop.setText("")
        self.blockTextureButtonBack.setText("")
        self.blockTextureButtonRight.setText("")
        self.blockTextureButtonBottom.setText("")
        self.blockTextureButtonLeft.setText("")
        self.blockTextureButtonFront.setText("")
        self.blockTextureBottom.setText("")
        self.blockTextureFront.setText("")
        self.blockTextureRight.setText("")
        self.blockTextureBack.setText("")
        self.blockTextureTop.setText("")
        self.blockTextureLeft.setText("")
        self.blockAddButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.blockEditButton.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.blockRemoveButton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.blockModelLabel.setText(QCoreApplication.translate("MainWindow", u"Model", None))
        self.blockModel.setItemText(0, QCoreApplication.translate("MainWindow", u"Block", None))
        self.blockModel.setItemText(1, QCoreApplication.translate("MainWindow", u"Custom", None))

        self.mainTab.setTabText(self.mainTab.indexOf(self.blockTab), QCoreApplication.translate("MainWindow", u"Blocks", None))
        self.itemDisplayNameLabel.setText(QCoreApplication.translate("MainWindow", u"Display Name", None))
        self.itemDisplayName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ruby", None))
        self.itemNameLabel.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.itemName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ruby", None))
        self.itemBaseItemLabel.setText(QCoreApplication.translate("MainWindow", u"Base Item", None))
        self.itemBaseItem.setPlaceholderText(QCoreApplication.translate("MainWindow", u"minecraft:flint", None))
        self.itemModelLabel.setText(QCoreApplication.translate("MainWindow", u"Model", None))
        self.itemModel.setItemText(0, QCoreApplication.translate("MainWindow", u"Normal", None))
        self.itemModel.setItemText(1, QCoreApplication.translate("MainWindow", u"Custom", None))

        self.itemTextureLabel.setText(QCoreApplication.translate("MainWindow", u"Texture", None))
        self.itemTextureButton.setText("")
        self.itemTexture.setText("")
        self.itemAddButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.itemEditButton.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.itemRemoveButton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.mainTab.setTabText(self.mainTab.indexOf(self.itemTab), QCoreApplication.translate("MainWindow", u"Items", None))
        self.recipeNameLabel.setText(QCoreApplication.translate("MainWindow", u"Recipe Name", None))
        self.slot0Button.setText("")
        self.slot1Button.setText("")
        self.slot2Button.setText("")
        self.slot3Button.setText("")
        self.slot4Button.setText("")
        self.slot5Button.setText("")
        self.slot6Button.setText("")
        self.slot7Button.setText("")
        self.slot8Button.setText("")
        self.slot9Button.setText("")
        self.shapelessRadio.setText(QCoreApplication.translate("MainWindow", u"Shapeless", None))
        self.exactlyRadio.setText(QCoreApplication.translate("MainWindow", u"Exactly Where Placed", None))
        self.slot0.setText("")
        self.slot1.setText("")
        self.slot2.setText("")
        self.slot3.setText("")
        self.slot4.setText("")
        self.slot5.setText("")
        self.slot6.setText("")
        self.slot7.setText("")
        self.slot8.setText("")
        self.slot9.setText("")
        self.recipeSubTabs.setTabText(self.recipeSubTabs.indexOf(self.craftingTab), QCoreApplication.translate("MainWindow", u"Crafting", None))
        self.smeltingInputButton.setText("")
        self.smeltingOutputButton.setText("")
        self.smeltingInput.setText("")
        self.smeltingOutput.setText("")
        self.recipeSubTabs.setTabText(self.recipeSubTabs.indexOf(self.smeltingTab), QCoreApplication.translate("MainWindow", u"Smelting", None))
        self.recipeEditButton.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.recipeAddButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.recipeRemoveButton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.mainTab.setTabText(self.mainTab.indexOf(self.recipeTab), QCoreApplication.translate("MainWindow", u"Recipes", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

