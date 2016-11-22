# This file has automatically been generated
# biogeme 2.5 [Die Okt 4 11:31:19 CEST 2016]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Tue Nov 22 10:16:54 2016</p>
#
ASC_TRAIN = Beta('ASC_TRAIN',-0.794293,-10000,10000,0,'ASC_TRAIN' )

B_TRAIN_TIME = Beta('B_TRAIN_TIME',-0.0177793,-10000,10000,0,'B_TRAIN_TIME' )

B_COST_TRAIN = Beta('B_COST_TRAIN',0.0154468,-10000,10000,0,'B_COST_TRAIN' )

ASC_CAR = Beta('ASC_CAR',-0.249083,-10000,10000,0,'ASC_CAR' )

B_CAR_TIME = Beta('B_CAR_TIME',-0.0426735,-10000,10000,0,'B_CAR_TIME' )

B_COST_CAR = Beta('B_COST_CAR',0.0714897,-10000,10000,0,'B_COST_CAR' )

B_MALE_CAR = Beta('B_MALE_CAR',0.194412,-10000,10000,0,'B_MALE_CAR' )

ASC_WALK = Beta('ASC_WALK',0,-10000,10000,1,'ASC_WALK' )

B_WALK_DIST = Beta('B_WALK_DIST',-0.23397,-10000,10000,0,'B_WALK_DIST' )

B_TRIP_PURPOSE = Beta('B_TRIP_PURPOSE',-0.275273,-10000,10000,0,'B_TRIP_PURPOSE' )


## Code for the sensitivity analysis
names = ['ASC_CAR','ASC_TRAIN','B_CAR_TIME','B_COST_CAR','B_COST_TRAIN','B_MALE_CAR','B_TRAIN_TIME','B_TRIP_PURPOSE','B_WALK_DIST']
values = [[0.165317,0.156673,0.000456831,-0.000652782,0.000192534,-0.00653806,0.000149028,0.0228537,0.0185622],[0.156673,0.160497,0.000504236,-0.00228384,-8.15396e-06,-0.00178564,4.22497e-05,0.0227373,0.0176666],[0.000456831,0.000504236,0.000110164,-0.000368826,1.01669e-05,-0.000130766,2.00264e-05,1.54679e-05,0.000193038],[-0.000652782,-0.00228384,-0.000368826,0.00216505,0.000143253,0.000176874,-3.58198e-05,3.74308e-05,-0.000397359],[0.000192534,-8.15396e-06,1.01669e-05,0.000143253,5.33867e-05,-3.02626e-05,3.9444e-06,4.59759e-05,5.57958e-05],[-0.00653806,-0.00178564,-0.000130766,0.000176874,-3.02626e-05,0.0108776,-3.06853e-05,-0.000192678,-0.000435299],[0.000149028,4.22497e-05,2.00264e-05,-3.58198e-05,3.9444e-06,-3.06853e-05,6.04673e-06,3.71325e-07,4.96089e-05],[0.0228537,0.0227373,1.54679e-05,3.74308e-05,4.59759e-05,-0.000192678,3.71325e-07,0.00751184,0.00132701],[0.0185622,0.0176666,0.000193038,-0.000397359,5.57958e-05,-0.000435299,4.96089e-05,0.00132701,0.00291092]]
vc = bioMatrix(9,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
