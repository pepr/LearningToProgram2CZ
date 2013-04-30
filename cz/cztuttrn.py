# -*- coding: cp1250 -*-

"""Skript pro generování a vkládání referencí na začátek cztuttrn.html.

Zmíněné reference se sbírají pouze ze souboru cztuttrn.html a tvoří obsah
dokumentu -- pro rychlou navigaci a přehled.
"""
# $Id: cztuttrn.py,v 1.1 2004/07/02 08:12:10 prikryl Exp $
import re, sys, os

filename = 'cztuttrn.html'

# Načteme všechny řádky souboru jako jeden řetězec. Originální obsah 
# ponecháme v proměnné content nedotčený až do finální fáze.
f = file(filename)
content = f.read()
f.close()

# Konce řádků změníme na mezery. Od tohoto okamžiku budeme pracovat
# s proměnnou cont.
cont = content.replace('\n', ' ')

# Zrušíme zakomentované části.
cont = re.sub('<!--.+?-->', ' ', cont)

# Zkonstruujeme regulární výraz pro extrakci nadpisů třetí úrovně a pro 
# extrakci položek označkovaných dt. Tyto texty nás zajímají. Všechny 
# zajímavé texty vyextrahujeme do seznamu. Bude to seznam n-tic odpovídajících
# jednotlivým skupinám. 
texts = re.findall(r'((<h3(\s.+?)?>.+?</h3>)|(<dt>.+?</dt>))', cont) 

# Ze seznamu n-tic vybíráme pouze první z nich a upravíme ji do podoby n-tic.
# První položka bude indikovat, zda jde o hlavičku nebo pojem. Druhá položka 
# bude obsahovat text a případná třetí položka bude obsahovat id.
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

# Zkonstruujeme miniobsah do proměnné result jako jeden řetězec.             
result = ''
for t in res: 
    if t[0] == 'h':
        if t[1]:
            result += '<p><a href="#%s"><b>%s</b></a><br>\n' % (t[1], t[2])
        else:
            result += '<p><b>%s</b><br>\n' % t[2]
    else:
        result += ' - <a href="#%s">%s</a><br>\n' % (t[1], t[2])

# V obraze původního dokumentu nalezneme původní miniobsah a nahradíme jej
# novým.
rex_minitoc = re.compile(r'(?s)<div class="minitoc">.+?</div>')
content = rex_minitoc.sub('<div class="minitoc">\n%s</div>' % result, content)

# Přejmenujeme původní soubor na záložní.
backup_filename = filename.replace('.html', '.bak')
if os.path.isfile(backup_filename):
    os.remove(backup_filename)
os.rename(filename, backup_filename)

# Původní soubor otevřeme pro zápis a zapíšeme do něj nový obsah.
f = file(filename, 'w')
f.write(content)
f.close()

