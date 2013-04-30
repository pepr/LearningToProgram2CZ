set f=v10
set t=v11

call cvs diff -r %f% -r %t% tutintro.htm   >01tutintro.dif
call cvs diff -r %f% -r %t% tutneeds.htm   >02tutneeds.dif
call cvs diff -r %f% -r %t% tutwhat.htm    >03tutwhat.dif
call cvs diff -r %f% -r %t% tutstart.htm   >04tutstart.dif
call cvs diff -r %f% -r %t% tutseq1.htm    >05tutseq1.dif
call cvs diff -r %f% -r %t% tutdata.htm    >06tutdata.dif
call cvs diff -r %f% -r %t% tutseq2.htm    >07tutseq2.dif
call cvs diff -r %f% -r %t% tutloops.htm   >08tutloops.dif
call cvs diff -r %f% -r %t% tutstyle.htm   >09tutstyle.dif
call cvs diff -r %f% -r %t% tutinput.htm   >10tutinput.dif

set f=v9

call cvs diff -r %f% -r %t% tutbranch.htm  >11tutbranch.dif
call cvs diff -r %f% -r %t% tutfunc.htm    >12tutfunc.dif
call cvs diff -r %f% -r %t% tutfiles.htm   >13tutfiles.dif
call cvs diff -r %f% -r %t% tuttext.htm    >14tuttext.dif
call cvs diff -r %f% -r %t% tuterrors.htm  >15tuterrors.dif
call cvs diff -r %f% -r %t% tutname.htm    >16tutname.dif
call cvs diff -r %f% -r %t% tutregex.htm   >17tutregex.dif
call cvs diff -r %f% -r %t% tutclass.htm   >18tutclass.dif
call cvs diff -r %f% -r %t% tutevent.htm   >19tutevent.dif
call cvs diff -r %f% -r %t% tutgui.htm     >20tutgui.dif
call cvs diff -r %f% -r %t% tutrecur.htm   >21tutrecur.dif
call cvs diff -r %f% -r %t% tutfctnl.htm   >22tutfctnl.dif
call cvs diff -r %f% -r %t% tutcase.htm    >23tutcase.dif
call cvs diff -r %f% -r %t% tutrefs.htm    >24tutrefs.dif

call cvs diff -r %f% -r %t% complang.htm   >25complang.dif
call cvs diff -r %f% -r %t% computing.htm  >26computing.dif
call cvs diff -r %f% -r %t% index.htm      >27index.dif
call cvs diff -r %f% -r %t% ispfed.htm     >28ispfed.dif
call cvs diff -r %f% -r %t% uml.htm        >29uml.dif
call cvs diff -r %f% -r %t% vbscript.htm   >30vbscript.dif

set f=
set t=                   
