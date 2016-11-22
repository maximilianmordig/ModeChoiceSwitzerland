# This file has automatically been generated
# biogeme 2.5 [Die Okt 4 11:31:19 CEST 2016]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Tue Nov 22 11:28:26 2016</p>
#
ASC_TRAIN = Beta('ASC_TRAIN',-1.06905,-10000,10000,0,'ASC_TRAIN' )

B_COST_TRAIN = Beta('B_COST_TRAIN',-0.0504074,-10000,10000,0,'B_COST_TRAIN' )

B_LANG_CODE = Beta('B_LANG_CODE',0.9998,-10000,10000,0,'B_LANG_CODE' )

LAMBDA = Beta('LAMBDA',0.559282,-10,10,0,'LAMBDA' )

B_TRAIN_TIME = Beta('B_TRAIN_TIME',-0.129071,-10000,10000,0,'B_TRAIN_TIME' )

ASC_CAR = Beta('ASC_CAR',0.832363,-10000,10000,0,'ASC_CAR' )

B_COST_CAR = Beta('B_COST_CAR',-0.0169965,-10000,10000,0,'B_COST_CAR' )

B_CAR_AVAIL1 = Beta('B_CAR_AVAIL1',0.711389,-10000,10000,0,'B_CAR_AVAIL1' )

B_CAR_AVAIL2 = Beta('B_CAR_AVAIL2',-0.912247,-10000,10000,0,'B_CAR_AVAIL2' )

B_CAR_AVAIL3 = Beta('B_CAR_AVAIL3',-3.12189,-10000,10000,0,'B_CAR_AVAIL3' )

B_FreqCarPar1 = Beta('B_FreqCarPar1',0,-10000,10000,1,'B_FreqCarPar1' )

B_FreqCarPar2 = Beta('B_FreqCarPar2',0.449757,-10000,10000,0,'B_FreqCarPar2' )

B_FreqCarPar3 = Beta('B_FreqCarPar3',0.536529,-10000,10000,0,'B_FreqCarPar3' )

B_CAR_TIME = Beta('B_CAR_TIME',-0.258876,-10000,10000,0,'B_CAR_TIME' )

B_MALE_TRAIN = Beta('B_MALE_TRAIN',0.00863784,-10000,10000,0,'B_MALE_TRAIN' )

ASC_WALK = Beta('ASC_WALK',0,-10000,10000,1,'ASC_WALK' )

B_TRIP_PURPOSE = Beta('B_TRIP_PURPOSE',-0.266484,-10000,10000,0,'B_TRIP_PURPOSE' )

B_WALK_DIST = Beta('B_WALK_DIST',-1.30107,-10000,10000,0,'B_WALK_DIST' )

LAMBDA_WALK = Beta('LAMBDA_WALK',0.312496,-10,10,0,'LAMBDA_WALK' )


## Code for the sensitivity analysis
names = ['ASC_CAR','ASC_TRAIN','B_CAR_AVAIL1','B_CAR_AVAIL2','B_CAR_AVAIL3','B_CAR_TIME','B_COST_CAR','B_COST_TRAIN','B_FreqCarPar2','B_FreqCarPar3','B_LANG_CODE','B_MALE_TRAIN','B_TRAIN_TIME','B_TRIP_PURPOSE','B_WALK_DIST','LAMBDA','LAMBDA_WALK']
values = [[0.225629,0.0954583,-0.0360786,-0.0418387,-0.0469108,-0.000212362,0.00102993,0.000911213,-0.00103636,-0.011609,0.0459419,-0.00297666,-7.20063e-05,0.0267099,0.0186011,-0.000340986,0.000704674],[0.0954583,0.115086,0.00225867,0.00389468,0.001184,-0.00418353,-0.00174367,-0.000259235,-0.00166755,-0.00368932,0.00225022,-0.000292559,-0.00392434,0.0256221,0.0103795,-0.00435964,0.000454826],[-0.0360786,0.00225867,0.0509651,0.0481825,0.0480634,3.17208e-05,-0.000840181,-0.000484575,-0.0077928,-0.0069455,0.00210397,-0.00538207,-0.000163122,0.000140571,-0.000374384,-0.000323606,8.62798e-05],[-0.0418387,0.00389468,0.0481825,0.0787475,0.0537431,-0.000622207,-0.00103043,-0.000903136,-0.00959262,-0.0110657,-0.000785299,-0.00324938,-0.000482755,-0.000227912,-0.000287858,-0.000922212,0.000317083],[-0.0469108,0.001184,0.0480634,0.0537431,0.200999,-0.00177842,-0.00121468,-0.00105928,-0.0125399,-0.0119261,-0.00488002,-0.00146607,-0.000980331,-0.00147665,0.00110009,-0.00319513,1.50527e-05],[-0.000212362,-0.00418353,3.17208e-05,-0.000622207,-0.00177842,0.00672914,0.000154045,0.000113865,-0.000255664,-6.56162e-06,0.000797661,0.00021851,0.00418192,2.93439e-05,0.0103064,0.00667618,0.00164118],[0.00102993,-0.00174367,-0.000840181,-0.00103043,-0.00121468,0.000154045,0.000591696,0.000146189,0.000504382,5.00652e-05,-5.43895e-06,-0.000133938,0.000313639,-2.10048e-05,0.000282853,0.000604624,8.10695e-05],[0.000911213,-0.000259235,-0.000484575,-0.000903136,-0.00105928,0.000113865,0.000146189,0.000160136,0.000113548,-2.71281e-05,0.000170341,-0.000287753,4.64334e-05,1.18498e-06,0.000275531,8.96274e-05,3.39416e-05],[-0.00103636,-0.00166755,-0.0077928,-0.00959262,-0.0125399,-0.000255664,0.000504382,0.000113548,0.0311935,0.0104727,0.000103462,-0.000705532,8.46743e-05,0.000594155,-0.00173306,0.000161476,-0.000449611],[-0.011609,-0.00368932,-0.0069455,-0.0110657,-0.0119261,-6.56162e-06,5.00652e-05,-2.71281e-05,0.0104727,0.0187492,-0.00302961,0.00147213,0.000118178,-0.000893153,-0.000765603,0.00024065,-0.000123381],[0.0459419,0.00225022,0.00210397,-0.000785299,-0.00488002,0.000797661,-5.43895e-06,0.000170341,0.000103462,-0.00302961,0.0250717,0.000110608,0.000310272,0.000771753,0.000312071,0.00090264,-7.07026e-05],[-0.00297666,-0.000292559,-0.00538207,-0.00324938,-0.00146607,0.00021851,-0.000133938,-0.000287753,-0.000705532,0.00147213,0.000110608,0.0153314,0.000305188,4.75824e-06,-0.000584506,0.000828663,-7.8148e-05],[-7.20063e-05,-0.00392434,-0.000163122,-0.000482755,-0.000980331,0.00418192,0.000313639,4.64334e-05,8.46743e-05,0.000118178,0.000310272,0.000305188,0.00276834,-1.27257e-05,0.00643547,0.00438377,0.00103294],[0.0267099,0.0256221,0.000140571,-0.000227912,-0.00147665,2.93439e-05,-2.10048e-05,1.18498e-06,0.000594155,-0.000893153,0.000771753,4.75824e-06,-1.27257e-05,0.0107983,0.00134203,0.000127042,-0.000220522],[0.0186011,0.0103795,-0.000374384,-0.000287858,0.00110009,0.0103064,0.000282853,0.000275531,-0.00173306,-0.000765603,0.000312071,-0.000584506,0.00643547,0.00134203,0.0401187,0.00871306,0.0115081],[-0.000340986,-0.00435964,-0.000323606,-0.000922212,-0.00319513,0.00667618,0.000604624,8.96274e-05,0.000161476,0.00024065,0.00090264,0.000828663,0.00438377,0.000127042,0.00871306,0.00817089,0.00168144],[0.000704674,0.000454826,8.62798e-05,0.000317083,1.50527e-05,0.00164118,8.10695e-05,3.39416e-05,-0.000449611,-0.000123381,-7.07026e-05,-7.8148e-05,0.00103294,-0.000220522,0.0115081,0.00168144,0.0055639]]
vc = bioMatrix(17,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
