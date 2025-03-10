# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/case_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_case_dialog(object):
    def setupUi(self, case_dialog):
        case_dialog.setObjectName("case_dialog")
        case_dialog.resize(706, 440)
        self.gridLayout_3 = QtWidgets.QGridLayout(case_dialog)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.OK_btn = QtWidgets.QDialogButtonBox(case_dialog)
        self.OK_btn.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.OK_btn.setFont(font)
        self.OK_btn.setOrientation(QtCore.Qt.Horizontal)
        self.OK_btn.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.OK_btn.setObjectName("OK_btn")
        self.gridLayout_3.addWidget(self.OK_btn, 2, 0, 1, 1)
        self.error_label = QtWidgets.QLabel(case_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.error_label.sizePolicy().hasHeightForWidth())
        self.error_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.error_label.setFont(font)
        self.error_label.setText("")
        self.error_label.setAlignment(QtCore.Qt.AlignCenter)
        self.error_label.setObjectName("error_label")
        self.gridLayout_3.addWidget(self.error_label, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_13 = QtWidgets.QLabel(case_dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 6, 0, 1, 1)
        self.case_xscale_sb = ScienDSpinBox(case_dialog)
        self.case_xscale_sb.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.case_xscale_sb.setFont(font)
        self.case_xscale_sb.setProperty("value", 1.0)
        self.case_xscale_sb.setObjectName("case_xscale_sb")
        self.gridLayout.addWidget(self.case_xscale_sb, 5, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(case_dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 5, 3, 1, 1)
        self.case_style_cb = QtWidgets.QComboBox(case_dialog)
        self.case_style_cb.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.case_style_cb.setFont(font)
        self.case_style_cb.setObjectName("case_style_cb")
        self.case_style_cb.addItem("")
        self.case_style_cb.addItem("")
        self.case_style_cb.addItem("")
        self.case_style_cb.addItem("")
        self.case_style_cb.addItem("")
        self.gridLayout.addWidget(self.case_style_cb, 7, 1, 1, 1)
        self.case_transform_cb = QtWidgets.QComboBox(case_dialog)
        self.case_transform_cb.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.case_transform_cb.setFont(font)
        self.case_transform_cb.setObjectName("case_transform_cb")
        self.case_transform_cb.addItem("")
        self.case_transform_cb.addItem("")
        self.case_transform_cb.addItem("")
        self.case_transform_cb.addItem("")
        self.case_transform_cb.addItem("")
        self.case_transform_cb.addItem("")
        self.case_transform_cb.addItem("")
        self.gridLayout.addWidget(self.case_transform_cb, 4, 4, 1, 1)
        self.label = QtWidgets.QLabel(case_dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.case_yscale_sb = ScienDSpinBox(case_dialog)
        self.case_yscale_sb.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.case_yscale_sb.setFont(font)
        self.case_yscale_sb.setProperty("value", 1.0)
        self.case_yscale_sb.setObjectName("case_yscale_sb")
        self.gridLayout.addWidget(self.case_yscale_sb, 5, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(case_dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(case_dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 7, 3, 1, 1)
        self.case_render_cb = QtWidgets.QComboBox(case_dialog)
        self.case_render_cb.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.case_render_cb.setFont(font)
        self.case_render_cb.setObjectName("case_render_cb")
        self.case_render_cb.addItem("")
        self.case_render_cb.addItem("")
        self.case_render_cb.addItem("")
        self.case_render_cb.addItem("")
        self.case_render_cb.addItem("")
        self.case_render_cb.addItem("")
        self.case_render_cb.addItem("")
        self.gridLayout.addWidget(self.case_render_cb, 4, 1, 1, 1)
        self.case_markersize_sb = QtWidgets.QDoubleSpinBox(case_dialog)
        self.case_markersize_sb.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.case_markersize_sb.setFont(font)
        self.case_markersize_sb.setDecimals(1)
        self.case_markersize_sb.setMinimum(0.1)
        self.case_markersize_sb.setMaximum(20.0)
        self.case_markersize_sb.setSingleStep(0.1)
        self.case_markersize_sb.setProperty("value", 2.0)
        self.case_markersize_sb.setObjectName("case_markersize_sb")
        self.gridLayout.addWidget(self.case_markersize_sb, 8, 4, 1, 1)
        self.case_first_cb = QtWidgets.QComboBox(case_dialog)
        self.case_first_cb.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.case_first_cb.setFont(font)
        self.case_first_cb.setObjectName("case_first_cb")
        self.gridLayout.addWidget(self.case_first_cb, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(case_dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)
        self.case_last_cb = QtWidgets.QComboBox(case_dialog)
        self.case_last_cb.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.case_last_cb.setFont(font)
        self.case_last_cb.setObjectName("case_last_cb")
        self.gridLayout.addWidget(self.case_last_cb, 0, 4, 1, 1)
        self.label_8 = QtWidgets.QLabel(case_dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 8, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(case_dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 3, 1, 1)
        self.label_9 = QtWidgets.QLabel(case_dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 8, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(case_dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 4, 0, 1, 1)
        self.case_ydata_cb = QtWidgets.QComboBox(case_dialog)
        self.case_ydata_cb.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.case_ydata_cb.setFont(font)
        self.case_ydata_cb.setObjectName("case_ydata_cb")
        self.gridLayout.addWidget(self.case_ydata_cb, 1, 4, 1, 1)
        self.label_14 = QtWidgets.QLabel(case_dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 6, 3, 1, 1)
        self.case_marker_cb = QtWidgets.QComboBox(case_dialog)
        self.case_marker_cb.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.case_marker_cb.setFont(font)
        self.case_marker_cb.setObjectName("case_marker_cb")
        self.case_marker_cb.addItem("")
        self.case_marker_cb.addItem("")
        self.case_marker_cb.addItem("")
        self.case_marker_cb.addItem("")
        self.case_marker_cb.addItem("")
        self.case_marker_cb.addItem("")
        self.case_marker_cb.addItem("")
        self.case_marker_cb.addItem("")
        self.case_marker_cb.addItem("")
        self.case_marker_cb.addItem("")
        self.case_marker_cb.addItem("")
        self.case_marker_cb.addItem("")
        self.case_marker_cb.addItem("")
        self.case_marker_cb.addItem("")
        self.case_marker_cb.addItem("")
        self.case_marker_cb.addItem("")
        self.case_marker_cb.addItem("")
        self.case_marker_cb.addItem("")
        self.case_marker_cb.addItem("")
        self.case_marker_cb.addItem("")
        self.case_marker_cb.addItem("")
        self.case_marker_cb.addItem("")
        self.case_marker_cb.addItem("")
        self.case_marker_cb.addItem("")
        self.case_marker_cb.addItem("")
        self.case_marker_cb.addItem("")
        self.gridLayout.addWidget(self.case_marker_cb, 8, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(case_dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.case_palettecol_cb = QtWidgets.QComboBox(self.groupBox)
        self.case_palettecol_cb.setMaximumSize(QtCore.QSize(150, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.case_palettecol_cb.setFont(font)
        self.case_palettecol_cb.setObjectName("case_palettecol_cb")
        self.case_palettecol_cb.addItem("")
        self.case_palettecol_cb.addItem("")
        self.case_palettecol_cb.addItem("")
        self.case_palettecol_cb.addItem("")
        self.case_palettecol_cb.addItem("")
        self.case_palettecol_cb.addItem("")
        self.case_palettecol_cb.addItem("")
        self.case_palettecol_cb.addItem("")
        self.gridLayout_2.addWidget(self.case_palettecol_cb, 0, 2, 1, 1)
        self.case_presetcol_rb = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.case_presetcol_rb.setFont(font)
        self.case_presetcol_rb.setObjectName("case_presetcol_rb")
        self.gridLayout_2.addWidget(self.case_presetcol_rb, 0, 1, 1, 1)
        self.case_randomcol_rb = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.case_randomcol_rb.setFont(font)
        self.case_randomcol_rb.setObjectName("case_randomcol_rb")
        self.gridLayout_2.addWidget(self.case_randomcol_rb, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 4, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.case_singlecol_rb = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.case_singlecol_rb.setFont(font)
        self.case_singlecol_rb.setChecked(True)
        self.case_singlecol_rb.setObjectName("case_singlecol_rb")
        self.horizontalLayout.addWidget(self.case_singlecol_rb)
        self.case_pickcol_btn = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.case_pickcol_btn.setFont(font)
        self.case_pickcol_btn.setObjectName("case_pickcol_btn")
        self.horizontalLayout.addWidget(self.case_pickcol_btn)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 5, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 3, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 2, 0, 1, 5)
        self.groupBox_2 = QtWidgets.QGroupBox(case_dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.case_addlegend_cb = QtWidgets.QCheckBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.case_addlegend_cb.setFont(font)
        self.case_addlegend_cb.setObjectName("case_addlegend_cb")
        self.gridLayout_4.addWidget(self.case_addlegend_cb, 1, 0, 1, 1)
        self.case_inforname_rb = QtWidgets.QRadioButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.case_inforname_rb.setFont(font)
        self.case_inforname_rb.setObjectName("case_inforname_rb")
        self.gridLayout_4.addWidget(self.case_inforname_rb, 1, 3, 1, 1)
        self.case_numname_rb = QtWidgets.QRadioButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.case_numname_rb.setFont(font)
        self.case_numname_rb.setChecked(True)
        self.case_numname_rb.setObjectName("case_numname_rb")
        self.gridLayout_4.addWidget(self.case_numname_rb, 1, 2, 1, 1)
        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout.addWidget(self.groupBox_2, 3, 0, 1, 5)
        self.label_6 = QtWidgets.QLabel(case_dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)
        self.case_xdata_cb = QtWidgets.QComboBox(case_dialog)
        self.case_xdata_cb.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.case_xdata_cb.setFont(font)
        self.case_xdata_cb.setObjectName("case_xdata_cb")
        self.gridLayout.addWidget(self.case_xdata_cb, 1, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(case_dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 5, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(case_dialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 3, 1, 1)
        self.case_linewidth_sb = QtWidgets.QDoubleSpinBox(case_dialog)
        self.case_linewidth_sb.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.case_linewidth_sb.setFont(font)
        self.case_linewidth_sb.setDecimals(1)
        self.case_linewidth_sb.setMinimum(0.1)
        self.case_linewidth_sb.setSingleStep(0.1)
        self.case_linewidth_sb.setProperty("value", 1.0)
        self.case_linewidth_sb.setObjectName("case_linewidth_sb")
        self.gridLayout.addWidget(self.case_linewidth_sb, 7, 4, 1, 1)
        self.case_xoffset_sb = ScienDSpinBox(case_dialog)
        self.case_xoffset_sb.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.case_xoffset_sb.setFont(font)
        self.case_xoffset_sb.setProperty("value", 0.0)
        self.case_xoffset_sb.setObjectName("case_xoffset_sb")
        self.gridLayout.addWidget(self.case_xoffset_sb, 6, 1, 1, 1)
        self.case_yoffset_sb = ScienDSpinBox(case_dialog)
        self.case_yoffset_sb.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.case_yoffset_sb.setFont(font)
        self.case_yoffset_sb.setProperty("value", 0.0)
        self.case_yoffset_sb.setObjectName("case_yoffset_sb")
        self.gridLayout.addWidget(self.case_yoffset_sb, 6, 4, 1, 1)
        self.gridLayout.setRowStretch(0, 10)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(case_dialog)
        self.case_style_cb.setCurrentIndex(0)
        self.case_marker_cb.setCurrentIndex(1)
        self.OK_btn.accepted.connect(case_dialog.accept) # type: ignore
        self.OK_btn.rejected.connect(case_dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(case_dialog)

    def retranslateUi(self, case_dialog):
        _translate = QtCore.QCoreApplication.translate
        case_dialog.setWindowTitle(_translate("case_dialog", "Case line addition"))
        self.label_13.setText(_translate("case_dialog", "X offset"))
        self.label_12.setText(_translate("case_dialog", "Y scale"))
        self.case_style_cb.setCurrentText(_translate("case_dialog", "None"))
        self.case_style_cb.setItemText(0, _translate("case_dialog", "None"))
        self.case_style_cb.setItemText(1, _translate("case_dialog", "Solid"))
        self.case_style_cb.setItemText(2, _translate("case_dialog", "Dashed"))
        self.case_style_cb.setItemText(3, _translate("case_dialog", "Dash-dot"))
        self.case_style_cb.setItemText(4, _translate("case_dialog", "Dotted"))
        self.case_transform_cb.setItemText(0, _translate("case_dialog", "None"))
        self.case_transform_cb.setItemText(1, _translate("case_dialog", "|.|"))
        self.case_transform_cb.setItemText(2, _translate("case_dialog", "Arg(.)"))
        self.case_transform_cb.setItemText(3, _translate("case_dialog", "unwrap Arg(.)"))
        self.case_transform_cb.setItemText(4, _translate("case_dialog", "20log(.)"))
        self.case_transform_cb.setItemText(5, _translate("case_dialog", "20log(|.|)"))
        self.case_transform_cb.setItemText(6, _translate("case_dialog", "unwrap(.)"))
        self.label.setText(_translate("case_dialog", "First case:"))
        self.label_3.setText(_translate("case_dialog", "X data"))
        self.label_7.setText(_translate("case_dialog", "Line width"))
        self.case_render_cb.setItemText(0, _translate("case_dialog", "Plot 1"))
        self.case_render_cb.setItemText(1, _translate("case_dialog", "Plot 2.1"))
        self.case_render_cb.setItemText(2, _translate("case_dialog", "Plot 2.2"))
        self.case_render_cb.setItemText(3, _translate("case_dialog", "Plot 3"))
        self.case_render_cb.setItemText(4, _translate("case_dialog", "Plot 4.1"))
        self.case_render_cb.setItemText(5, _translate("case_dialog", "Plot 4.2"))
        self.case_render_cb.setItemText(6, _translate("case_dialog", "Plot 5"))
        self.label_2.setText(_translate("case_dialog", "Last case:"))
        self.label_8.setText(_translate("case_dialog", "Mark style"))
        self.label_4.setText(_translate("case_dialog", "Y data"))
        self.label_9.setText(_translate("case_dialog", "Mark width"))
        self.label_10.setText(_translate("case_dialog", "Plot"))
        self.label_14.setText(_translate("case_dialog", "Y offset"))
        self.case_marker_cb.setCurrentText(_translate("case_dialog", "Point"))
        self.case_marker_cb.setItemText(0, _translate("case_dialog", "None"))
        self.case_marker_cb.setItemText(1, _translate("case_dialog", "Point"))
        self.case_marker_cb.setItemText(2, _translate("case_dialog", "Pixel"))
        self.case_marker_cb.setItemText(3, _translate("case_dialog", "Circle"))
        self.case_marker_cb.setItemText(4, _translate("case_dialog", "Triangle down"))
        self.case_marker_cb.setItemText(5, _translate("case_dialog", "Triangle up"))
        self.case_marker_cb.setItemText(6, _translate("case_dialog", "Triangle left"))
        self.case_marker_cb.setItemText(7, _translate("case_dialog", "Triangle right"))
        self.case_marker_cb.setItemText(8, _translate("case_dialog", "Tri down"))
        self.case_marker_cb.setItemText(9, _translate("case_dialog", "Tri up"))
        self.case_marker_cb.setItemText(10, _translate("case_dialog", "Tri left"))
        self.case_marker_cb.setItemText(11, _translate("case_dialog", "Tri right"))
        self.case_marker_cb.setItemText(12, _translate("case_dialog", "Octagon"))
        self.case_marker_cb.setItemText(13, _translate("case_dialog", "Square"))
        self.case_marker_cb.setItemText(14, _translate("case_dialog", "Pentagon"))
        self.case_marker_cb.setItemText(15, _translate("case_dialog", "Plus (filled)"))
        self.case_marker_cb.setItemText(16, _translate("case_dialog", "Star"))
        self.case_marker_cb.setItemText(17, _translate("case_dialog", "Hexagon"))
        self.case_marker_cb.setItemText(18, _translate("case_dialog", "Hexagon alt."))
        self.case_marker_cb.setItemText(19, _translate("case_dialog", "Plus"))
        self.case_marker_cb.setItemText(20, _translate("case_dialog", "x"))
        self.case_marker_cb.setItemText(21, _translate("case_dialog", "x (filled)"))
        self.case_marker_cb.setItemText(22, _translate("case_dialog", "Diamond"))
        self.case_marker_cb.setItemText(23, _translate("case_dialog", "Diamond (thin)"))
        self.case_marker_cb.setItemText(24, _translate("case_dialog", "Vline"))
        self.case_marker_cb.setItemText(25, _translate("case_dialog", "Hline"))
        self.groupBox.setTitle(_translate("case_dialog", "Color"))
        self.case_palettecol_cb.setItemText(0, _translate("case_dialog", "Solid palette"))
        self.case_palettecol_cb.setItemText(1, _translate("case_dialog", "Blue palette"))
        self.case_palettecol_cb.setItemText(2, _translate("case_dialog", "Green palette"))
        self.case_palettecol_cb.setItemText(3, _translate("case_dialog", "Red palette"))
        self.case_palettecol_cb.setItemText(4, _translate("case_dialog", "Hot palette"))
        self.case_palettecol_cb.setItemText(5, _translate("case_dialog", "Cold palette"))
        self.case_palettecol_cb.setItemText(6, _translate("case_dialog", "Diverging palette"))
        self.case_palettecol_cb.setItemText(7, _translate("case_dialog", "Diverging palette 2"))
        self.case_presetcol_rb.setText(_translate("case_dialog", "Preset:"))
        self.case_randomcol_rb.setText(_translate("case_dialog", "Random"))
        self.case_singlecol_rb.setText(_translate("case_dialog", "Single:"))
        self.case_pickcol_btn.setText(_translate("case_dialog", "Pick"))
        self.groupBox_2.setTitle(_translate("case_dialog", "Naming"))
        self.case_addlegend_cb.setText(_translate("case_dialog", "Add labels to legend"))
        self.case_inforname_rb.setText(_translate("case_dialog", "Case info"))
        self.case_numname_rb.setText(_translate("case_dialog", "Numbered"))
        self.label_6.setText(_translate("case_dialog", "Line style"))
        self.label_11.setText(_translate("case_dialog", "X scale"))
        self.label_5.setText(_translate("case_dialog", "Transform"))
from src.widgets.scientific_spinbox import ScienDSpinBox


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    case_dialog = QtWidgets.QDialog()
    ui = Ui_case_dialog()
    ui.setupUi(case_dialog)
    case_dialog.show()
    sys.exit(app.exec_())
