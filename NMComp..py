import random

#reference : https://www.thoughtco.com/common-prefixes-in-english-1692724
#            http://www.betterendings.org/homeschool/words/root%20words.htm            
prefix = ['a','an','ante','auto','circum','co','com','con',
       'contra','contro','de','dis','en','ex','extra','hetero',
       'homo','homeo','hyper','il','im','in','ir','inter','intra',
       'intro','macro','micro','mono','non','omni','post','pre','pro',
       'sub','sym','syn','tele','trans','tri','un','uni','up']
suffix = ['agog','agogue','cide','ectomy','ia','y','ic','tic','ical','ac','ics',
          'isk','iscus','ism','ist','ite','logy','oid','or','er','phobia','sis']
root= ['alter','ami','amic','amphi','ann','enni','anthrop','aqua','arch','arthro',
       'aud','bell','bibio','bio','brev','cap','carn','ced','chrom','chron','cogn',
       'cord','chord','corp','crac','crat','cred','cruc','crusta','crypt','culp','dei',
       'demo','dent','derm','dic','dox','duc','duct','duo','dynam','ego','equ','fac','fil',
       'frater','gam','geo','glyph','grad','gress','graph','gym','gyn','hemo','hema','hem',
       'holo','hydro','hydr','iso','ject','jud','leg','lect','liter','loc','log',
       'luc','magn','man','mar','mater','mere','meta','met','metri','meter','min',
       'mit','miss','mob','mot','mort','morph','mut','neuro','nomen','nomin','nov',
       'nym','onym','odonto','ortho','pac','pater','path','ped','pod','pel','puls',
       'pend','phon','phono','plan','pmeum','pod','port','psych','pugna','quer','quis'
       'scent','secend','schizo','schiz','sci','sciss','scrib','script','sec','sect','sed'
       'sess','sens','sent','sequ','secu','serv','simil','siphon','sol','soph','sepc','spic','spir',
       'spond','spons','spont','stat','tang','tact','temp','ten','tent','terr','theo',
       'therm','trophy','uro','vac','ven','vent','ver','vert','vit','voc','zoo']


for nm in range (5):
 porr = random.randint(0,1)
 char1 = ' '
 if porr == 0 :
   char1 = random.choice(prefix)
 else :
   char1= random.choice(root)


 ysorns = random.randint(0,1)
 char2 = ' '
 if ysorns == 0 :
   char2= random.choice(suffix)
 else :
   char2= random.choice(root)


 Up =str.capitalize(char1 + char2)
 print(Up)




