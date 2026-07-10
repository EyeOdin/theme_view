# Theme View is a Krita plugin to display theme colors
# Copyright ( C ) 2026  Ricardo Jeremias.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# ( at your option ) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


#region Imports

# Krita Module
from krita import *
# PyQt5 Modules
from PyQt5 import QtWidgets, QtCore, QtGui, uic

#endregion
#region Global Variables

version = "2026_07_10"
DOCKER_NAME = "Theme View"

#endregion


class ThemeView_Docker( DockWidget ):
    """
    Display Theme Colors
    """

    #region Initialize

    def __init__( self ):
        super( ThemeView_Docker, self ).__init__()

        # Construct
        self.Interface()
        self.Module()
        self.Variable()
        self.Connection()

    def Interface( self ):
        # Window
        self.setWindowTitle( DOCKER_NAME )
        # Path Name
        self.directory_plugin = str( os.path.dirname( os.path.realpath( __file__ ) ) )
        # Widget Docker
        self.layout = uic.loadUi( os.path.join( self.directory_plugin, "theme_view_docker.ui" ), QWidget( self ) )
        self.setWidget( self.layout )
    def Module( self ):
        self.notifier = Krita.instance().notifier()
        self.notifier.windowCreated.connect( self.Window_Created )
    def Variable( self ):
        self.w_alternate     = "#000000"
        self.w_base          = "#000000"
        self.w_button        = "#000000"
        self.w_dark          = "#000000"
        self.w_light         = "#000000"
        self.w_mid           = "#000000"
        self.w_midlight      = "#000000"
        self.w_shadow        = "#000000"
        self.w_tool_tip      = "#000000"
        self.w_window        = "#000000"
        # Text
        self.t_bright        = "#000000"
        self.t_button        = "#000000"
        self.t_highlighted   = "#000000"
        self.t_placeholder   = "#000000"
        self.t_text          = "#000000"
        self.t_tool_tip      = "#000000"
        self.t_window        = "#000000"
        # Color
        self.c_highlight     = "#000000"
        self.c_link          = "#000000"
        self.c_visited       = "#000000"
        self.c_accent        = "#000000"
    def Connection( self ):
        # Window
        self.layout.window_alternate.clicked.connect(   lambda: self.Clipboard_Hexcode( self.w_alternate ) )
        self.layout.window_base.clicked.connect(        lambda: self.Clipboard_Hexcode( self.w_base ) )
        self.layout.window_button.clicked.connect(      lambda: self.Clipboard_Hexcode( self.w_button ) )
        self.layout.window_dark.clicked.connect(        lambda: self.Clipboard_Hexcode( self.w_dark ) )
        self.layout.window_light.clicked.connect(       lambda: self.Clipboard_Hexcode( self.w_light ) )
        self.layout.window_mid.clicked.connect(         lambda: self.Clipboard_Hexcode( self.w_mid ) )
        self.layout.window_midlight.clicked.connect(    lambda: self.Clipboard_Hexcode( self.w_midlight ) )
        self.layout.window_shadow.clicked.connect(      lambda: self.Clipboard_Hexcode( self.w_shadow ) )
        self.layout.window_tool_tip.clicked.connect(    lambda: self.Clipboard_Hexcode( self.w_tool_tip ) )
        self.layout.window_window.clicked.connect(      lambda: self.Clipboard_Hexcode( self.w_window ) )
        # Text
        self.layout.text_bright.clicked.connect(        lambda: self.Clipboard_Hexcode( self.t_bright ) )
        self.layout.text_button.clicked.connect(        lambda: self.Clipboard_Hexcode( self.t_button ) )
        self.layout.text_highlighted.clicked.connect(   lambda: self.Clipboard_Hexcode( self.t_highlighted ) )
        self.layout.text_placeholder.clicked.connect(   lambda: self.Clipboard_Hexcode( self.t_placeholder ) )
        self.layout.text_text.clicked.connect(          lambda: self.Clipboard_Hexcode( self.t_text ) )
        self.layout.text_tool_tip.clicked.connect(      lambda: self.Clipboard_Hexcode( self.t_tool_tip ) )
        self.layout.text_window.clicked.connect(        lambda: self.Clipboard_Hexcode( self.t_window ) )
        # Window
        self.layout.color_highlight.clicked.connect(    lambda: self.Clipboard_Hexcode( self.c_highlight ) )
        self.layout.color_link.clicked.connect(         lambda: self.Clipboard_Hexcode( self.c_link ) )
        self.layout.color_visited.clicked.connect(      lambda: self.Clipboard_Hexcode( self.c_visited ) )

    #endregion
    #region Theme

    # Interaction
    def Clipboard_Hexcode( self, hex_code ):
        QtCore.qDebug( f"hex_code = { hex_code }" )
        try:
            clip_board = QApplication.clipboard()
            clip_board.clear()
            clip_board.setText( hex_code )
        except:
            pass
    # Style
    def Style_Theme( self ):
        """
        Theme Breeze Dark
        w_alternate     = #31363b
        w_base          = #232629
        w_button        = #31363b
        w_dark          = #1d2023
        w_light         = #464d54
        w_mid           = #2b3034
        w_midlight      = #3c4248
        w_shadow        = #151719
        w_tool_tip      = #31363b
        w_window        = #31363b
        t_bright        = #ffffff
        t_button        = #eff0f1
        t_highlighted   = #eff0f1
        t_placeholder   = #eff0f1
        t_text          = #eff0f1
        t_tool_tip      = #eff0f1
        t_window        = #eff0f1
        c_highlight     = #3daee9
        c_link          = #2980b9
        c_visited       = #7f8c8d

        Theme Breeze Ligh
        w_alternate     = #f8f7f6
        w_base          = #fcfcfc
        w_button        = #eff0f1
        w_dark          = #888e93
        w_light         = #ffffff
        w_mid           = #c4c8cc
        w_midlight      = #f6f7f7
        w_shadow        = #474a4c
        w_tool_tip      = #fcfcfc
        w_window        = #eff0f1
        t_bright        = #ffffff
        t_button        = #31363b
        t_highlighted   = #fcfcfc
        t_placeholder   = #31363b
        t_text          = #31363b
        t_tool_tip      = #31363b
        t_window        = #31363b
        c_highlight     = #3daee9
        c_link          = #0057ae
        c_visited       = #452886
        """
        # Read
        palette = QApplication.palette()
        base = palette.base().color()
        # Window
        self.w_alternate     = palette.alternateBase().color().name()
        self.w_base          = palette.base().color().name()
        self.w_button        = palette.button().color().name()
        self.w_dark          = palette.dark().color().name()
        self.w_light         = palette.light().color().name()
        self.w_mid           = palette.mid().color().name()
        self.w_midlight      = palette.midlight().color().name()
        self.w_shadow        = palette.shadow().color().name()
        self.w_tool_tip      = palette.toolTipBase().color().name()
        self.w_window        = palette.window().color().name()
        # Text
        self.t_bright        = palette.brightText().color().name()
        self.t_button        = palette.buttonText().color().name()
        self.t_highlighted   = palette.highlightedText().color().name()
        self.t_placeholder   = palette.placeholderText().color().name()
        self.t_text          = palette.text().color().name()
        self.t_tool_tip      = palette.toolTipText().color().name()
        self.t_window        = palette.windowText().color().name()
        # Color
        self.c_highlight     = palette.highlight().color().name()
        self.c_link          = palette.link().color().name()
        self.c_visited       = palette.linkVisited().color().name()
        # self.c_accent        = palette.accent().color().name() # qt6

        # Layout
        self.layout.contents.setStyleSheet(         "#contents{ background-color: rgba(0, 0, 0, 20);}" )
        # Window
        self.layout.dw_alternate.setStyleSheet(     "background-color: " + self.w_alternate + ";" )
        self.layout.dw_base.setStyleSheet(          "background-color: " + self.w_base + ";" )
        self.layout.dw_button.setStyleSheet(        "background-color: " + self.w_button + ";" )
        self.layout.dw_dark.setStyleSheet(          "background-color: " + self.w_dark + ";" )
        self.layout.dw_light.setStyleSheet(         "background-color: " + self.w_light + ";" )
        self.layout.dw_mid.setStyleSheet(           "background-color: " + self.w_mid + ";" )
        self.layout.dw_midlight.setStyleSheet(      "background-color: " + self.w_midlight + ";" )
        self.layout.dw_shadow.setStyleSheet(        "background-color: " + self.w_shadow + ";" )
        self.layout.dw_tool_tip.setStyleSheet(      "background-color: " + self.w_tool_tip + ";" )
        self.layout.dw_window.setStyleSheet(        "background-color: " + self.w_window + ";" )
        # Text
        self.layout.dt_bright.setStyleSheet(        "background-color: " + self.t_bright + ";" )
        self.layout.dt_button.setStyleSheet(        "background-color: " + self.t_button + ";" )
        self.layout.dt_highlighted.setStyleSheet(   "background-color: " + self.t_highlighted + ";" )
        self.layout.dt_placeholder.setStyleSheet(   "background-color: " + self.t_placeholder + ";" )
        self.layout.dt_text.setStyleSheet(          "background-color: " + self.t_text + ";" )
        self.layout.dt_tool_tip.setStyleSheet(      "background-color: " + self.t_tool_tip + ";" )
        self.layout.dt_window.setStyleSheet(        "background-color: " + self.t_window + ";" )
        # Color
        self.layout.dc_highlight.setStyleSheet(     "background-color: " + self.c_highlight + ";" )
        self.layout.dc_link.setStyleSheet(          "background-color: " + self.c_link + ";" )
        self.layout.dc_visited.setStyleSheet(       "background-color: " + self.c_visited + ";" )

    #endregion
    #region Notifier

    # Notifier
    def Window_Created( self ):
        self.window = Krita.instance().activeWindow()
        self.window.themeChanged.connect( self.Theme_Changed )
    def Theme_Changed( self ):
        self.Style_Theme()

    #endregion
    #region Widget Events

    def showEvent( self, event ):
        self.Style_Theme()

    def canvasChanged( self, canvas ):
        pass

    #endregion
    #region Notes

    """
    # Label Message
    self.layout.label.setText( "message" )

    # Pop Up Message
    QMessageBox.information( QWidget(), i18n( "Warnning" ), i18n( "message" ) )

    # Log Viewer Message
    QtCore.qDebug( f"value = { value }" )
    QtCore.qDebug( "message" )
    QtCore.qWarning( "message" )
    QtCore.qCritical( "message" )
    """

    #endregion
