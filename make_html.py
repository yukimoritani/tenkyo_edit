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
    f=open("index.txt", "r")
    l=f.readlines()
    f.close
    for i in l :
        cont.append(re.split('[\t\n]',i))
    return cont

# Before Index Table
def MakeStringHead(yr,no,kno,ftype):

    mn=['1', '3', '5', '7', '9', '11']
    imd=['images/','images/','../../images/']
    no_f='%02d' % (int(no))
    vol='%d' % (orig_v+int(yr)-2018)

    s=unicode('<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN\">\n','shift_jisx0213')

    tmps=unicode('<HTML LANG=\"Ja-jp\">\n','shift_jisx0213')
    s=s+tmps

    tmps=unicode('<HEAD>\n','shift_jisx0213')
    s=s+tmps

    tmps=unicode('<META HTTP-EQUIV="Content-Type\" CONTENT="text/html; charset=shift_jisx0213\">\n','shift_jisx0213')
    s=s+tmps

    tmps=unicode('<TITLE>「天文教育」（'+yr+'年'+mn[int(no)-1]+'月号）</TITLE>\n','shift_jisx0213')
    s=s+tmps

    tmps=unicode('</HEAD>\n','shift_jisx0213')
    s=s+tmps

    tmps=unicode('\n','shift_jisx0213')
    s=s+tmps

    tmps=unicode('<BODY BGCOLOR=\"#ffffff\">\n','shift_jisx0213')
    s=s+tmps

    tmps=unicode('\n','shift_jisx0213')
    s=s+tmps

    tmps=unicode('<TABLE>\n','shift_jisx0213')
    s=s+tmps

    tmps=unicode('<TBODY>\n','shift_jisx0213')
    s=s+tmps

    tmps=unicode('<TR>\n','shift_jisx0213')
    s=s+tmps

    image=imd[ftype]+yr+no_f
    tmps=unicode('<TD><A href=\"'+image+'.jpg\"><IMG SRC=\"'+image+'.jpg\" WIDTH=\"120\" BORDER=\"1\"></A></TD>\n','shift_jisx0213')
    s=s+tmps

    tmps=unicode('<TD VALIGN=\"Top\">\n','shift_jisx0213')
    s=s+tmps

    tmps=unicode('<H2>'+yr+'年'+mn[int(no)-1]+'月号</H2>\n','shift_jisx0213')
    s=s+tmps

    tmps=unicode('<H3>'+str(kno)+'号　Vol.'+vol+' No.'+str(int(no))+'</H3><BR>\n','shift_jisx0213')
    s=s+tmps

    tmps=unicode('</TD></TR>\n','shift_jisx0213')
    s=s+tmps

    tmps=unicode('</TBODY>\n','shift_jisx0213')
    s=s+tmps

    tmps=unicode('</TABLE>\n','shift_jisx0213')
    s=s+tmps

    tmps=unicode('\n','shift_jisx0213')
    s=s+tmps

    return s

# Before Index Table 2: For Members
def MakeStringMember(yr,no,kno,ftype):

    no_f='%02d' % (int(no))
    mn=['1', '3', '5', '7', '9', '11']

    s=unicode('<A href=\"pdf/'+yr+'_'+no_f+'/kaiho'+mn[int(no)]+'.html\">','shift_jisx0213')

    tmps=unicode('<img src=\"../img/members.gif\" border=\"0\" alt=\"会員の方はこちら\"></A><br>\n','shift_jisx0213')
    s=s+tmps

    tmps=unicode('\n','shift_jisx0213')
    s=s+tmps

    return s

# The Table Top Line
def MakeStringTableHead():

    s=unicode('<br>\n\n','shift_jisx0213')

    tmps=unicode('<TABLE CELLSPACING=\"0\" CELLPADDING=\"3\" BORDER=\"1\">\n','shift_jisx0213')
    s=s+tmps

    tmps=unicode('<TBODY>\n\n','shift_jisx0213')
    s=s+tmps

    tmps=unicode('<TR>\n','shift_jisx0213')
    s=s+tmps

    tmps=unicode('<TD>目次</TD>\n','shift_jisx0213')
    s=s+tmps

    tmps=unicode('<TD>　</TD>\n','shift_jisx0213')
    s=s+tmps

    tmps=unicode('<TD>1</TD>\n','shift_jisx0213')
    s=s+tmps

    tmps=unicode('</TR>\n\n','shift_jisx0213')
    s=s+tmps

    return s

# Line for Section
def MakeLineTH(sn):

    s=unicode('<TR>\n','shift_jisx0213')

    tmps=unicode('<TD COLSPAN=\"3\"></TD>\n','shift_jisx0213')
    s=s+tmps

    tmps=unicode('</TR>\n\n','shift_jisx0213')
    s=s+tmps

    tmps=unicode('<TR>\n','shift_jisx0213')
    s=s+tmps

    tmps=unicode('<TH ALIGN=\"Left\" COLSPAN=\"3\">◎'+sn+'</TH>\n','shift_jisx0213')
    s=s+tmps

    tmps=unicode('</TR>\n\n','shift_jisx0213')
    s=s+tmps

    return s

# Line for Article
def MakeLineTD(tit, stit, auth, page, pdf, ftype):

    dot=unicode('、','shift_jisx0213')
    br=unicode('<br>','shift_jisx0213')

    if pdf.find('info-') is not -1:
        if pdf.find('events') is -1 and pdf.find('books') is -1:
            ftype=0

    ha='<A HREF=\"'
    ta='\" TARGET=\"_blank\">'
    sa=['', ha+'pdf/'+pdf+ta, ha+pdf[8:]+ta]
    ea=['','</A>','</A>']


    s=unicode('<TR>\n','shift_jisx0213')

    tmps=unicode('<TD>'+sa[ftype]+tit+'<FONT SIZE=\"-1\">'+stit+'</FONT></TD>\n','shift_jisx0213')
    s=s+tmps

    tmps=unicode('<TD>'+auth+'</TD>\n','shift_jisx0213')
    tmps1=tmps.replace(dot,br)
    s=s+tmps1

    tmps=unicode('<TD>'+page+ea[ftype]+'</TD>\n','shift_jisx0213')
    s=s+tmps

    tmps=unicode('</TR>\n\n','shift_jisx0213')
    s=s+tmps

    return s

# Line for Cover
def MakeLineCover(tit, auth):

    s=unicode('<TR>\n','shift_jisx0213')

    tmps=unicode('<TD>表紙の言葉：'+tit+'</TD>\n','shift_jisx0213')
    s=s+tmps

    tmps=unicode('<TD COLSPAN=\"2\">撮影・文：'+auth+'</TD></TR>\n\n','shift_jisx0213')
    s=s+tmps

    return s

# After Index Table
def MakeStringFoot():

    s=unicode('</TBODY>\n\n','shift_jisx0213')

    tmps=unicode('</TABLE>\n\n','shift_jisx0213')
    s=s+tmps

    tmps=unicode('<P><BR></P>\n\n','shift_jisx0213')
    s=s+tmps

    tmps=unicode('<P><HR></P>\n\n','shift_jisx0213')
    s=s+tmps

    tmps=unicode('<CENTER>\n','shift_jisx0213')
    s=s+tmps

    tmps=unicode('<FORM>\n','shift_jisx0213')
    s=s+tmps

    tmps=unicode('<INPUT TYPE=\"button\" VALUE=\"一つ前に戻る\" onClick=history.go(-1)>　\n','shift_jisx0213')
    s=s+tmps

    tmps=unicode('<INPUT TYPE=\"button\" VALUE=\"会誌『天文教育』\" onClick=location=\'http://tenkyo.net/kaiho.html\'>\n','shift_jisx0213')
    s=s+tmps

    tmps=unicode('<INPUT TYPE=\"button\" VALUE=\"当会について\" onClick=location=\'http://tenkyo.net/what.html\'>　\n','shift_jisx0213')
    s=s+tmps

    tmps=unicode('<INPUT TYPE=\"button\" VALUE=\"トップページ\" onClick=location=\'http://tenkyo.net/\'>\n','shift_jisx0213')
    s=s+tmps

    tmps=unicode('</FORM>\n','shift_jisx0213')
    s=s+tmps

    tmps=unicode('</CENTER>\n\n','shift_jisx0213')
    s=s+tmps

    tmps=unicode('<P ALIGN=\"center\"><A HREF=\"http://tenkyo.net/\"><B>天文教育普及研究会</B> <FONT SIZE=\"-1\"><I>Japanese Society for Education and Popularization of Astronomy</I></FONT></A></P>\n\n','shift_jisx0213')
    s=s+tmps

    tmps=unicode('</BODY>\n','shift_jisx0213')
    s=s+tmps

    tmps=unicode('</HTML>\n','shift_jisx0213')
    s=s+tmps

    return s

def MakeHtmlFiles(yr,no,kno):

    # Read contents
    cont=ReadIndex()

    # Read pdf list
    fp=open("pdf.txt", "r")
    p=fp.readlines()
    #if len(p)-3 is not len(cont)-2 :
    if len(p)-1 is not len(cont)-2 :
        print "The number of index is different from the numbr of files."
        print len(p),len(cont)-2
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
    print >> f0 , s.encode('shift_jisx0213')
    s=MakeStringHead(yr,no,kno,1)
    print >> f1 , s.encode('shift_jisx0213')
    s=MakeStringHead(yr,no,kno,2)
    print >> f2 , s.encode('shift_jisx0213')

    # For Public in the first year
    s=MakeStringMember(yr,no,kno,0)
    print >> f0 , s.encode('shift_jisx0213')

    # Table Top Head
    s=MakeStringTableHead()
    print >> f0 , s.encode('shift_jisx0213')
    print >> f1 , s.encode('shift_jisx0213')
    print >> f2 , s.encode('shift_jisx0213')

    # Main Table
    s0=unicode('','shift_jisx0213')
    s1=unicode('','shift_jisx0213')
    s2=unicode('','shift_jisx0213')
    j=-2
    for i in cont:
        #print len(i),i
        if len(i) is 6:
            print i
            if i[0] is not '':
                s0=s0+MakeLineTH(i[0])
                s1=s1+MakeLineTH(i[0])
                s2=s2+MakeLineTH(i[0])
                s0=s0+MakeLineTD(i[1],i[2],i[3],i[4],p[j+2],0)
                s1=s1+MakeLineTD(i[1],i[2],i[3],i[4],p[j+2],1)
                s2=s2+MakeLineTD(i[1],i[2],i[3],i[4],p[j+2],2)
            else:
                s0=s0+MakeLineTD(i[1],i[2],i[3],i[4],p[j+2],0)
                s1=s1+MakeLineTD(i[1],i[2],i[3],i[4],p[j+2],1)
                s2=s2+MakeLineTD(i[1],i[2],i[3],i[4],p[j+2],2)
        else:
            s0=s0+MakeLineCover(i[0], i[1])
            s1=s1+MakeLineCover(i[0], i[1])
            s2=s2+MakeLineCover(i[0], i[1])
        j=j+1

    print >> f0 , s0.encode('shift_jisx0213')
    print >> f1 , s1.encode('shift_jisx0213')
    print >> f2 , s2.encode('shift_jisx0213')

    # Write foots
    s=MakeStringFoot()
    print >> f0 , s.encode('shift_jisx0213')
    print >> f1 , s.encode('shift_jisx0213')
    print >> f2 , s.encode('shift_jisx0213')

    # Close files
    f0.close
    f1.close
    f2.close

if __name__ == '__main__':

    # Preparation
    # 1) make pfd.txt listing pdf files
    # ls yyyy_mm/*pdf > pdf.txt
    # Make index.txt coping from index (word)
    #     Column 1: section (blank if the same)
    #     Column 2: title
    #     Column 3: Sub-title
    #     Column 4: Authors (divide with Japanese comma)
    #     Column 5: page

    # ./MakeHtmlFiles.py yyyy No
    yyyy=sys.argv[1]
    no=sys.argv[2]
    kno=orig+(int(yyyy)-2018)*6+(int(no)-1)
    MakeHtmlFiles(yyyy,no,kno)
