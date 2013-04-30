# -*- coding: cp1250 -*-

"""Skript pro generov�n� a vkl�d�n� referenc� na za��tek cztuttrn.html.

Zm�n�n� reference se sb�raj� pouze ze souboru cztuttrn.html a tvo�� obsah
dokumentu -- pro rychlou navigaci a p�ehled.
"""
# $Id: cztuttrn.py,v 1.1 2004/07/02 08:12:10 prikryl Exp $
import re, sys, os

filename = 'cztuttrn.html'

# Na�teme v�echny ��dky souboru jako jeden �et�zec. Origin�ln� obsah 
# ponech�me v prom�nn� content nedot�en� a� do fin�ln� f�ze.
f = file(filename)
content = f.read()
f.close()

# Konce ��dk� zm�n�me na mezery. Od tohoto okam�iku budeme pracovat
# s prom�nnou cont.
cont = content.replace('\n', ' ')

# Zru��me zakomentovan� ��sti.
cont = re.sub('<!--.+?-->', ' ', cont)

# Zkonstruujeme regul�rn� v�raz pro extrakci nadpis� t�et� �rovn� a pro 
# extrakci polo�ek ozna�kovan�ch dt. Tyto texty n�s zaj�maj�. V�echny 
# zaj�mav� texty vyextrahujeme do seznamu. Bude to seznam n-tic odpov�daj�c�ch
# jednotliv�m skupin�m. 
texts = re.findall(r'((<h3(\s.+?)?>.+?</h3>)|(<dt>.+?</dt>))', cont) 

# Ze seznamu n-tic vyb�r�me pouze prvn� z nich a uprav�me ji do podoby n-tic.
# Prvn� polo�ka bude indikovat, zda jde o hlavi�ku nebo pojem. Druh� polo�ka 
# bude obsahovat text a p��padn� t�et� polo�ka bude obsahovat id.
res = []
rexh3 = re.compile(r'<h3(\sid="(?P<id>.+?)")?>(?P<txt>.+?)</h3>')
rexdt = re.compile(r'<dt>.+?\sid="(?P<id>\S+?)".+?</a>\s*(?P<txt>.+?)\s*:?\s*</dt>')

for t in texts:
    m = rexh3.match(t[0])
    if m:
        res.append(('h', m.group('id'), m.group('txt')))
    else:
        m = rexdt.match(t[0])
        if m:
            res.append(('i', m.group('id'), m.group('txt')))

# Zkonstruujeme miniobsah do prom�nn� result jako jeden �et�zec.             
result = ''
for t in res: 
    if t[0] == 'h':
        if t[1]:
            result += '<p><a href="#%s"><b>%s</b></a><br>\n' % (t[1], t[2])
        else:
            result += '<p><b>%s</b><br>\n' % t[2]
    else:
        result += ' - <a href="#%s">%s</a><br>\n' % (t[1], t[2])

# V obraze p�vodn�ho dokumentu nalezneme p�vodn� miniobsah a nahrad�me jej
# nov�m.
rex_minitoc = re.compile(r'(?s)<div class="minitoc">.+?</div>')
content = rex_minitoc.sub('<div class="minitoc">\n%s</div>' % result, content)

# P�ejmenujeme p�vodn� soubor na z�lo�n�.
backup_filename = filename.replace('.html', '.bak')
if os.path.isfile(backup_filename):
    os.remove(backup_filename)
os.rename(filename, backup_filename)

# P�vodn� soubor otev�eme pro z�pis a zap�eme do n�j nov� obsah.
f = file(filename, 'w')
f.write(content)
f.close()

