#!/usr/bin/env python
# coding: shift_jis

import os, sys
import re

# origin of kaiho number
# 2018 01 = 150
# volume 2018=30
orig=150
orig_v=30

def ReadIndex():

    cont=[]
    f=open("index.txt", "rb")
    l=f.readlines()
    f.close
    for i in l :
        i=i.decode('shift_jisx0213')
        cont.append(re.split('[\t\n]',i))
    return cont

# Before Index Table
def MakeStringHead(yr,no,kno,ftype):

    mn=['1', '3', '5', '7', '9', '11']
    imd=['images/','images/','../../images/']
    no_f='%02d' % (int(no))
    vol='%d' % (orig_v+int(yr)-2018)

    s='<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN\">\n'.encode('shift_jisx0213')

    tmps='<HTML LANG=\"Ja-jp\">\n<HEAD>\n'.encode('shift_jisx0213')
    s=s+tmps

    tmps='<META HTTP-EQUIV="Content-Type\" CONTENT="text/html; charset=shift_jisx0213\">\n'.encode('shift_jisx0213')
    s=s+tmps

    tmps='<TITLE>「天文教育」（'+yr+'年'+mn[int(no)-1]+'月号）</TITLE>\n'
    tmps=tmps.encode('shift_jisx0213')
    s=s+tmps

    tmps='</HEAD>\n\n'.encode('shift_jisx0213')
    s=s+tmps

    tmps='<BODY BGCOLOR=\"#ffffff\">\n\n'.encode('shift_jisx0213')
    s=s+tmps

    tmps='<TABLE>\n<TBODY>\n<TR>\n'.encode('shift_jisx0213')
    s=s+tmps

    image=imd[ftype]+yr+no_f
    tmps='<TD><A href=\"'+image+'.jpg\"><IMG SRC=\"'+image+'.jpg\" WIDTH=\"120\" BORDER=\"1\"></A></TD>\n'
    tmps=tmps.encode('shift_jisx0213')
    s=s+tmps

    tmps='<TD VALIGN=\"Top\">\n'.encode('shift_jisx0213')
    s=s+tmps

    tmps='<H2>'+yr+'年'+mn[int(no)-1]+'月号</H2>\n'
    tmps=tmps.encode('shift_jisx0213')
    s=s+tmps

    tmps='<H3>'+str(kno)+'号　Vol.'+vol+' No.'+str(int(no))+'</H3><BR>\n'
    tmps=tmps.encode('shift_jisx0213')
    s=s+tmps

    tmps='</TD></TR>\n</TBODY>\n</TABLE>\n\n'.encode('shift_jisx0213')
    s=s+tmps

    return s

# Before Index Table 2: For Members
def MakeStringMember(yr,no,kno,ftype):

    no_f='%02d' % (int(no))
    mn=['1', '3', '5', '7', '9', '11']

    #s='<A href=\"pdf/'+yr+'_'+no_f+'/kaiho'+mn[int(no)]+'.html\">'
    s='<A href=\"pdf/'+yr+'_'+no_f+'/kaiho'+str(kno)+'.html\">'
    s=s.encode('shift_jisx0213')

    tmps='<img src=\"../img/members.gif\" border=\"0\" alt=\"会員の方はこちら\"></A><br>\n\n'.encode('shift_jisx0213')
    s=s+tmps

    return s

# The Table Top Line
def MakeStringTableHead():

    s='<br>\n\n<TABLE CELLSPACING=\"0\" CELLPADDING=\"3\" BORDER=\"1\">\n'.encode('shift_jisx0213')

    tmps='<TBODY>\n\n<TR>\n<TD>目次</TD>\n'.encode('shift_jisx0213')
    s=s+tmps

    tmps='<TD>　</TD>\n<TD>1</TD>\n</TR>\n\n'.encode('shift_jisx0213')
    s=s+tmps

    return s

# Line for Section
def MakeLineTH(sn):

    s='<TR>\n<TD COLSPAN=\"3\"></TD>\n</TR>\n\n<TR>\n'.encode('shift_jisx0213')

    tmps='<TH ALIGN=\"Left\" COLSPAN=\"3\">◎'+sn+'</TH>\n'
    tmps=tmps.encode('shift_jisx0213')
    s=s+tmps

    tmps='</TR>\n\n'.encode('shift_jisx0213')
    s=s+tmps

    return s

# Line for Article
def MakeLineTD(tit, stit, auth, page, pdf, ftype):

    dot='、'.encode('shift_jisx0213')
    br='<br>'.encode('shift_jisx0213')

    if 'info-' in pdf:
        if 'events' in pdf or 'books' in pdf:
            pass
        else:
            ftype=0
    if 'n/a' in pdf:
        ftype=0

    ha='<A HREF=\"'
    ta='\" TARGET=\"_blank\">'
    sa=['', ha+'pdf/'+pdf+ta, ha+pdf[8:]+ta]
    ea=['','</A>','</A>']


    s='<TR>\n'.encode('shift_jisx0213')

    tmps='<TD>'+sa[ftype]+tit+'<FONT SIZE=\"-1\"> '+stit+'</FONT></TD>\n'
    tmps=tmps.encode('shift_jisx0213')
    s=s+tmps

    tmps='<TD>'+auth+'</TD>\n'
    tmps=tmps.encode('shift_jisx0213')
    tmps1=tmps.replace(dot,br)
    s=s+tmps1

    tmps='<TD>'+page+ea[ftype]+'</TD>\n'
    tmps=tmps.encode('shift_jisx0213')
    s=s+tmps

    tmps='</TR>\n\n'.encode('shift_jisx0213')
    s=s+tmps

    return s

# Line for Cover
def MakeLineCover(tit, auth):

    s='<TR>\n'.encode('shift_jisx0213')

    tmps='<TD>表紙の言葉：'+tit+'</TD>\n'
    tmps=tmps.encode('shift_jisx0213')
    s=s+tmps

    tmps='<TD COLSPAN=\"2\">撮影・文：'+auth+'</TD></TR>\n\n'
    tmps=tmps.encode('shift_jisx0213')
    s=s+tmps

    return s

# After Index Table
def MakeStringFoot():

    s='</TBODY>\n\n</TABLE>\n\n<P><BR></P>\n\n'.encode('shift_jisx0213')

    tmps='<P><HR></P>\n\n<CENTER>\n<FORM>\n'.encode('shift_jisx0213')
    s=s+tmps

    tmps='<INPUT TYPE=\"button\" VALUE=\"一つ前に戻る\" onClick=history.go(-1)>　\n'.encode('shift_jisx0213')
    s=s+tmps

    tmps='<INPUT TYPE=\"button\" VALUE=\"会誌『天文教育』\" onClick=location=\'http://tenkyo.net/kaiho.html\'>\n'.encode('shift_jisx0213')
    s=s+tmps

    tmps='<INPUT TYPE=\"button\" VALUE=\"当会について\" onClick=location=\'http://tenkyo.net/what.html\'>　\n'.encode('shift_jisx0213')
    s=s+tmps

    tmps='<INPUT TYPE=\"button\" VALUE=\"トップページ\" onClick=location=\'http://tenkyo.net/\'>\n'.encode('shift_jisx0213')
    s=s+tmps

    tmps='</FORM>\n</CENTER>\n\n'.encode('shift_jisx0213')
    s=s+tmps

    tmps='<P ALIGN=\"center\"><A HREF=\"http://tenkyo.net/\"><B>天文教育普及研究会</B> <FONT SIZE=\"-1\"><I>Japanese Society for Education and Popularization of Astronomy</I></FONT></A></P>\n\n'.encode('shift_jisx0213')
    s=s+tmps

    tmps='</BODY>\n</HTML>\n'.encode('shift_jisx0213')
    s=s+tmps


    return s

def MakeHtmlFiles(yr,no,kno):

    # Read contents
    cont=ReadIndex()

    # Read pdf list
    fp=open("pdf.txt", "r")
    p=fp.readlines()
    #if len(p)-3 is not len(cont)-2 :
    if len(p) is not len(cont)-1 :
        print("The number of index is different from the numbr of files.")
        #print len(p),len(cont)-2
        return 0

    #dname=yr+"_"+no
    #print kno
    # For public
    fn0="kaiho"+str(kno)+".html"
    # For public (after opening)
    fn1="kaiho"+str(kno)+"_open.html"
    # For members
    fn2="kaiho"+str(kno)+"_member.html"

    # Prepare files
    f0=open(fn0, "w")
    f1=open(fn1, "w")
    f2=open(fn2, "w")

    # Write heads
    s=MakeStringHead(yr,no,kno,0)
    print(s.decode('shift_jisx0213'),file=f0)
    s=MakeStringHead(yr,no,kno,1)
    print(s.decode('shift_jisx0213'),file=f1)
    s=MakeStringHead(yr,no,kno,2)
    print(s.decode('shift_jisx0213'),file=f2)

    # For Public in the first year
    s=MakeStringMember(yr,no,kno,0)
    print(s.decode('shift_jisx0213'),file=f0)

    # Table Top Head
    s=MakeStringTableHead()
    print(s.decode('shift_jisx0213'),file=f0)
    print(s.decode('shift_jisx0213'),file=f1)
    print(s.decode('shift_jisx0213'),file=f2)

    # Main Table
    s0=''.encode('shift_jisx0213')
    s1=''.encode('shift_jisx0213')
    s2=''.encode('shift_jisx0213')
    j=0
    for i in cont:
        #print len(i),i
        if len(i) is 6:
            #print i
            if i[0] is not '':
                s0=s0+MakeLineTH(i[0])
                s1=s1+MakeLineTH(i[0])
                s2=s2+MakeLineTH(i[0])
                s0=s0+MakeLineTD(i[1],i[2],i[3],i[4],p[j],0)
                s1=s1+MakeLineTD(i[1],i[2],i[3],i[4],p[j],1)
                s2=s2+MakeLineTD(i[1],i[2],i[3],i[4],p[j],2)
            else:
                s0=s0+MakeLineTD(i[1],i[2],i[3],i[4],p[j],0)
                s1=s1+MakeLineTD(i[1],i[2],i[3],i[4],p[j],1)
                s2=s2+MakeLineTD(i[1],i[2],i[3],i[4],p[j],2)
        else:
            s0=s0+MakeLineCover(i[0], i[1])
            s1=s1+MakeLineCover(i[0], i[1])
            s2=s2+MakeLineCover(i[0], i[1])
        j=j+1

    print(s0.decode('shift_jisx0213'),file=f0)
    print(s1.decode('shift_jisx0213'),file=f1)
    print(s2.decode('shift_jisx0213'),file=f2)

    # Write foots
    s=MakeStringFoot()
    print(s.decode('shift_jisx0213'),file=f0)
    print(s.decode('shift_jisx0213'),file=f1)
    print(s.decode('shift_jisx0213'),file=f2)

    # Close files
    f0.close
    f1.close
    f2.close

def Usage():

    print('# Preparation')
    print('# 1) Make pfd.txt listing pdf files')
    print('#       ls yyyy_mm/*pdf > pdf.txt')
    print('#     write\"n/a\" if the file is not available.')
    print('# 2) Make index.txt coping from index (word)')
    print('#     Column 1: section (blank if the same)')
    print('#     Column 2: title')
    print('#     Column 3: Sub-title')
    print('#     Column 4: Authors (divide with Japanese comma)')
    print('#     Column 5: page')
    print('')
    print('make_html.py yyyy no')

if __name__ == '__main__':

    if sys.argv[1]=='-h' or sys.argv[1]=='help' :
        Usage()
        exit()

    # ./MakeHtmlFiles.py yyyy No
    yyyy=sys.argv[1]
    no=sys.argv[2]
    kno=orig+(int(yyyy)-2018)*6+(int(no)-1)
    MakeHtmlFiles(yyyy,no,kno)
