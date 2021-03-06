# This file has automatically been generated
# biogeme 2.5 [Die Okt 4 11:31:19 CEST 2016]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Tue Nov 22 10:31:11 2016</p>
#
ASC_TRAIN = Beta('ASC_TRAIN',-0.668907,-10000,10000,0,'ASC_TRAIN' )

B_TRAIN_TIME = Beta('B_TRAIN_TIME',-0.0164741,-10000,10000,0,'B_TRAIN_TIME' )

B_COST_TRAIN = Beta('B_COST_TRAIN',0.0131563,-10000,10000,0,'B_COST_TRAIN' )

B_LANG_CODE = Beta('B_LANG_CODE',1.30221,-10000,10000,0,'B_LANG_CODE' )

B_AGE = Beta('B_AGE',-0.00357317,-10000,10000,0,'B_AGE' )

ASC_CAR = Beta('ASC_CAR',1.1036,-10000,10000,0,'ASC_CAR' )

B_CAR_TIME = Beta('B_CAR_TIME',-0.0402746,-10000,10000,0,'B_CAR_TIME' )

B_COST_CAR = Beta('B_COST_CAR',0.0641385,-10000,10000,0,'B_COST_CAR' )

B_MALE_CAR = Beta('B_MALE_CAR',0.239814,-10000,10000,0,'B_MALE_CAR' )

B_TYPE_COMMUNE_CAR = Beta('B_TYPE_COMMUNE_CAR',0.182045,-10000,10000,0,'B_TYPE_COMMUNE_CAR' )

ASC_WALK = Beta('ASC_WALK',0,-10000,10000,1,'ASC_WALK' )

B_WALK_DIST = Beta('B_WALK_DIST',-0.231549,-10000,10000,0,'B_WALK_DIST' )

B_TRIP_PURPOSE = Beta('B_TRIP_PURPOSE',-0.268285,-10000,10000,0,'B_TRIP_PURPOSE' )


## Code for the sensitivity analysis
names = ['ASC_CAR','ASC_TRAIN','B_AGE','B_CAR_TIME','B_COST_CAR','B_COST_TRAIN','B_LANG_CODE','B_MALE_CAR','B_TRAIN_TIME','B_TRIP_PURPOSE','B_TYPE_COMMUNE_CAR','B_WALK_DIST']
values = [[0.242233,0.163516,-7.09395e-05,0.000490915,-0.00143536,6.68942e-05,0.0333621,-0.00675685,0.000125183,0.0223486,-0.00266125,0.0189271],[0.163516,0.186621,-0.000499478,0.000570307,-0.00295244,-0.000109308,-6.23993e-05,-0.00734613,3.70122e-05,0.0216043,-0.000538766,0.0181358],[-7.09395e-05,-0.000499478,1.02282e-05,-1.61449e-06,1.11379e-05,1.10094e-06,3.47666e-07,0.000115768,-9.77003e-09,7.56911e-06,2.39639e-06,-3.69178e-06],[0.000490915,0.000570307,-1.61449e-06,0.000109787,-0.0003718,9.60485e-06,-2.22574e-05,-0.000160608,2.01348e-05,3.8573e-06,-1.64629e-05,0.000192094],[-0.00143536,-0.00295244,1.11379e-05,-0.0003718,0.00226907,0.000161875,-0.000145871,0.000299264,-3.38261e-05,3.7634e-05,8.97841e-05,-0.000378032],[6.68942e-05,-0.000109308,1.10094e-06,9.60485e-06,0.000161875,5.81973e-05,-4.42082e-05,-2.238e-05,4.21129e-06,3.31183e-05,7.01981e-07,6.00748e-05],[0.0333621,-6.23993e-05,3.47666e-07,-2.22574e-05,-0.000145871,-4.42082e-05,0.0209117,0.00107379,-1.08207e-05,0.000234652,0.000816142,-0.000117428],[-0.00675685,-0.00734613,0.000115768,-0.000160608,0.000299264,-2.238e-05,0.00107379,0.0130058,-3.45175e-05,-0.000143878,0.000245727,-0.000453393],[0.000125183,3.70122e-05,-9.77003e-09,2.01348e-05,-3.38261e-05,4.21129e-06,-1.08207e-05,-3.45175e-05,6.33493e-06,-1.93289e-06,1.1917e-06,5.02876e-05],[0.0223486,0.0216043,7.56911e-06,3.8573e-06,3.7634e-05,3.31183e-05,0.000234652,-0.000143878,-1.93289e-06,0.00749559,2.66218e-05,0.00116727],[-0.00266125,-0.000538766,2.39639e-06,-1.64629e-05,8.97841e-05,7.01981e-07,0.000816142,0.000245727,1.1917e-06,2.66218e-05,0.00074651,-6.33385e-05],[0.0189271,0.0181358,-3.69178e-06,0.000192094,-0.000378032,6.00748e-05,-0.000117428,-0.000453393,5.02876e-05,0.00116727,-6.33385e-05,0.00298763]]
vc = bioMatrix(12,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
