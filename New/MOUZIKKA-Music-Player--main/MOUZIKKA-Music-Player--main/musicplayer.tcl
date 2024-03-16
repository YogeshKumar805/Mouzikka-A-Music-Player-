#############################################################################
# Generated by PAGE version 4.19
#  in conjunction with Tcl version 8.6
#  Jan 21, 2019 05:22:31 PM +0530  platform: Windows NT
set vTcl(timestamp) ""


#############################################################################
## vTcl Code to Load User Images see vTcl:save2 in file.tcl

catch {package require Img}

foreach img {

        {{[file join C:/ Users Sachin Desktop musicplayergui icons add.png]} {user image} user {}}
        {{[file join C:/ Users Sachin Desktop musicplayergui icons broken-heart.png]} {user image} user {}}
        {{[file join C:/ Users Sachin Desktop musicplayergui icons delete.png]} {user image} user {}}
        {{[file join C:/ Users Sachin Desktop musicplayergui icons like.png]} {user image} user {}}
        {{[file join C:/ Users Sachin Desktop musicplayergui icons pause.png]} {user image} user {}}
        {{[file join C:/ Users Sachin Desktop musicplayergui icons play.png]} {user image} user {}}
        {{[file join C:/ Users Sachin Desktop musicplayergui icons previous.png]} {user image} user {}}
        {{[file join C:/ Users Sachin Desktop musicplayergui icons refresh.png]} {user image} user {}}
        {{[file join C:/ Users Sachin Desktop musicplayergui icons stop.png]} {user image} user {}}
        {{[file join C:/ Users Sachin Desktop musicplayergui icons vinylrecord.png]} {user image} user {}}

            } {
# from vTcl:image:dump_create_image_footer
    eval set _file [lindex $img 0]
    vTcl:image:create_new_image\
        $_file [lindex $img 1] [lindex $img 2] [lindex $img 3]
}

if {!$vTcl(borrow)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(active_menu_fg) #000000
}

#############################################################################
# vTcl Code to Load User Fonts

vTcl:font:add_font \
    "-family {Avenir Next Cyr Medium} -size 23 -weight normal -slant roman -underline 0 -overstrike 0" \
    user \
    vTcl:font11
vTcl:font:add_font \
    "-family {Avenir Next Cyr} -size 9 -weight bold -slant roman -underline 0 -overstrike 0" \
    user \
    vTcl:font12
#################################
#LIBRARY PROCEDURES
#


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top42
    global vTcl
    set base $vTcl(btop)
    if {$base == ""} {
        set base .top42
    }
    namespace eval ::widgets::$base {
        set dflt,origin 0
        set runvisible 1
    }
    namespace eval ::widgets_bindings {
        set tagslist _TopLevel
    }
    namespace eval ::vTcl::modules::main {
        set procs {
        }
        set compounds {
        }
        set projectType single
    }
}
}

#################################
# GENERATED GUI PROCEDURES
#

proc vTclWindow.top42 {base} {
    if {$base == ""} {
        set base .top42
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background {#fff} -highlightbackground {#d9d9d9} \
        -highlightcolor black
    wm focusmodel $top passive
    wm geometry $top 687x526+558+155
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1604 882
    wm minsize $top 116 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "New Toplevel"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    label $top.lab47 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#fff} -disabledforeground {#a3a3a3} \
        -font $::vTcl(fonts,vTcl:font11,object) -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -text {Ladki Aankh Maare}
    vTcl:DefineAlias "$top.lab47" "songName" vTcl:WidgetProc "Toplevel1" 1
    ttk::progressbar $top.tPr48 \
        -value 60
    vTcl:DefineAlias "$top.tPr48" "songProgress" vTcl:WidgetProc "Toplevel1" 1
    ttk::label $top.tLa51 \
        -background {#fff} -foreground {#3399ff} \
        -font $::vTcl(fonts,vTcl:font12,object) -relief flat -text 2:10
    vTcl:DefineAlias "$top.tLa51" "songTotalDuration" vTcl:WidgetProc "Toplevel1" 1
    ttk::label $top.tLa53 \
        -background {#ffffff} -foreground {#000000} \
        -font $::vTcl(fonts,vTcl:font12,object) -relief flat -text 1:15
    vTcl:DefineAlias "$top.tLa53" "songTimePassed" vTcl:WidgetProc "Toplevel1" 1
    button $top.but61 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#fff} -borderwidth 0 -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -image [vTcl:image:get_image [file join C:/ Users Sachin Desktop musicplayergui icons pause.png]] \
        -pady 0 -text Button
    vTcl:DefineAlias "$top.but61" "pauseButton" vTcl:WidgetProc "Toplevel1" 1
    button $top.but62 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#fff} -borderwidth 0 -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -image [vTcl:image:get_image [file join C:/ Users Sachin Desktop musicplayergui icons play.png]] \
        -pady 0 -text Button
    vTcl:DefineAlias "$top.but62" "playButton" vTcl:WidgetProc "Toplevel1" 1
    button $top.but63 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#fff} -borderwidth 0 -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -image [vTcl:image:get_image [file join C:/ Users Sachin Desktop musicplayergui icons stop.png]] \
        -pady 0 -text Button
    vTcl:DefineAlias "$top.but63" "stopButton" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab64 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#d9d9d9} -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -image [vTcl:image:get_image [file join C:/ Users Sachin Desktop musicplayergui icons vinylrecord.png]] \
        -text Label
    vTcl:DefineAlias "$top.lab64" "vinylRecordImage" vTcl:WidgetProc "Toplevel1" 1
    vTcl::widgets::ttk::scrolledlistbox::CreateCmd $top.scr65 \
        -background {#d9d9d9} -height 75 -highlightbackground {#d9d9d9} \
        -highlightcolor black -width 125
    vTcl:DefineAlias "$top.scr65" "playList" vTcl:WidgetProc "Toplevel1" 1

    $top.scr65.01 configure -background white \
        -disabledforeground #a3a3a3 \
        -font TkFixedFont \
        -foreground black \
        -height 3 \
        -highlightbackground #d9d9d9 \
        -highlightcolor #d9d9d9 \
        -selectbackground #c4c4c4 \
        -selectforeground black \
        -width 10
    label $top.lab76 \
        -activebackground {#f9f9f9} -activeforeground black \
        -background {#fff} -borderwidth 0 -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -image [vTcl:image:get_image [file join C:/ Users Sachin Desktop musicplayergui icons previous.png]] \
        -text Label
    vTcl:DefineAlias "$top.lab76" "previousButton" vTcl:WidgetProc "Toplevel1" 1
    ttk::label $top.tLa90 \
        -background {#d9d9d9} -foreground {#000000} -font TkDefaultFont \
        -relief flat -state disabled
    vTcl:DefineAlias "$top.tLa90" "bottomBar" vTcl:WidgetProc "Toplevel1" 1
    vTcl:copy_lock $top.tLa90
    ttk::scale $top.tSc94 \
        -takefocus {}
    vTcl:DefineAlias "$top.tSc94" "TScale2" vTcl:WidgetProc "Toplevel1" 1
    button $top.but97 \
        -activebackground {#ececec} -activeforeground {#d9d9d9} \
        -background {#fff} -borderwidth 0 -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -image [vTcl:image:get_image [file join C:/ Users Sachin Desktop musicplayergui icons add.png]] \
        -pady 0 -text Button
    vTcl:DefineAlias "$top.but97" "addSongsToPlayListButton" vTcl:WidgetProc "Toplevel1" 1
    button $top.but98 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#fff} -borderwidth 0 -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -image [vTcl:image:get_image [file join C:/ Users Sachin Desktop musicplayergui icons delete.png]] \
        -pady 0 -text Button
    vTcl:DefineAlias "$top.but98" "deleteSongsFromPlaylistButton" vTcl:WidgetProc "Toplevel1" 1
    button $top.but103 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -borderwidth 0 -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -image [vTcl:image:get_image [file join C:/ Users Sachin Desktop musicplayergui icons broken-heart.png]] \
        -pady 0 -text Button
    vTcl:DefineAlias "$top.but103" "Button9" vTcl:WidgetProc "Toplevel1" 1
    button $top.but105 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -borderwidth 0 -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -image [vTcl:image:get_image [file join C:/ Users Sachin Desktop musicplayergui icons like.png]] \
        -pady 0 -text Button
    vTcl:DefineAlias "$top.but105" "Button10" vTcl:WidgetProc "Toplevel1" 1
    button $top.but107 \
        -activebackground {#ececec} -activeforeground {#000000} \
        -background {#d9d9d9} -borderwidth 0 -disabledforeground {#a3a3a3} \
        -font TkDefaultFont -foreground {#000000} \
        -highlightbackground {#d9d9d9} -highlightcolor black \
        -image [vTcl:image:get_image [file join C:/ Users Sachin Desktop musicplayergui icons refresh.png]] \
        -pady 0 -text Button
    vTcl:DefineAlias "$top.but107" "Button11" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.lab47 \
        -in $top -x 300 -y 20 -anchor nw -bordermode ignore
    place $top.tPr48 \
        -in $top -x 270 -y 110 -width 340 -relwidth 0 -height 7 -relheight 0 \
        -anchor nw -bordermode ignore
    place $top.tLa51 \
        -in $top -x 580 -y 90 -width 29 -height 19 -anchor nw \
        -bordermode ignore
    place $top.tLa53 \
        -in $top -x 270 -y 90 -width 29 -height 19 -anchor nw \
        -bordermode ignore
    place $top.but61 \
        -in $top -x 390 -y 140 -anchor nw -bordermode ignore
    place $top.but62 \
        -in $top -x 440 -y 140 -anchor nw -bordermode ignore
    place $top.but63 \
        -in $top -x 490 -y 140 -anchor nw -bordermode ignore
    place $top.lab64 \
        -in $top -x 0 -y 0 -anchor nw -bordermode ignore
    place $top.scr65 \
        -in $top -x 0 -y 200 -width 686 -relwidth 0 -height 280 -relheight 0 \
        -anchor nw -bordermode ignore
    place $top.lab76 \
        -in $top -x 340 -y 140 -anchor nw -bordermode ignore
    place $top.tLa90 \
        -in $top -x 0 -y 480 -width 686 -relwidth 0 -height 49 -relheight 0 \
        -anchor nw -bordermode ignore
    place $top.tSc94 \
        -in $top -x 10 -y 490 -width 100 -height 26 -anchor nw \
        -bordermode ignore
    place $top.but97 \
        -in $top -x 660 -y 170 -width 17 -height 17 -anchor nw \
        -bordermode ignore
    place $top.but98 \
        -in $top -x 630 -y 170 -width 18 -height 18 -anchor nw \
        -bordermode ignore
    place $top.but103 \
        -in $top -x 640 -y 482 -width 42 -relwidth 0 -height 42 -relheight 0 \
        -anchor nw -bordermode ignore
    place $top.but105 \
        -in $top -x 600 -y 482 -width 42 -relwidth 0 -height 42 -relheight 0 \
        -anchor nw -bordermode ignore
    place $top.but107 \
        -in $top -x 570 -y 490 -width 26 -height 26 -anchor nw \
        -bordermode ignore

    vTcl:FireEvent $base <<Ready>>
}

#############################################################################
## Binding tag:  _TopLevel

bind "_TopLevel" <<Create>> {
    if {![info exists _topcount]} {set _topcount 0}; incr _topcount
}
bind "_TopLevel" <<DeleteWindow>> {
    if {[set ::%W::_modal]} {
                vTcl:Toplevel:WidgetProc %W endmodal
            } else {
                destroy %W; if {$_topcount == 0} {exit}
            }
}
bind "_TopLevel" <Destroy> {
    if {[winfo toplevel %W] == "%W"} {incr _topcount -1}
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top42 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

