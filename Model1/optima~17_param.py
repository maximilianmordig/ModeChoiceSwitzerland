# This file has automatically been generated
# biogeme 2.5 [Die Okt 4 11:31:19 CEST 2016]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Tue Nov 22 11:02:27 2016</p>
#
ASC_TRAIN = Beta('ASC_TRAIN',-0.88724,-10000,10000,0,'ASC_TRAIN' )

B_TRAIN_TIME = Beta('B_TRAIN_TIME',-0.0161176,-10000,10000,0,'B_TRAIN_TIME' )

B_COST_TRAIN = Beta('B_COST_TRAIN',0.0157698,-10000,10000,0,'B_COST_TRAIN' )

B_LANG_CODE = Beta('B_LANG_CODE',1.24292,-10000,10000,0,'B_LANG_CODE' )

ASC_CAR = Beta('ASC_CAR',1.76851,-10000,10000,0,'ASC_CAR' )

B_CAR_TIME = Beta('B_CAR_TIME',-0.0350053,-10000,10000,0,'B_CAR_TIME' )

B_COST_CAR = Beta('B_COST_CAR',0.0481877,-10000,10000,0,'B_COST_CAR' )

B_MALE_CAR = Beta('B_MALE_CAR',-0.100728,-10000,10000,0,'B_MALE_CAR' )

B_TYPE_COMMUNE_CAR1 = Beta('B_TYPE_COMMUNE_CAR1',0,-10000,10000,1,'B_TYPE_COMMUNE_CAR1' )

B_TYPE_COMMUNE_CAR2 = Beta('B_TYPE_COMMUNE_CAR2',0,-10000,10000,1,'B_TYPE_COMMUNE_CAR2' )

B_CAR_AVAIL1 = Beta('B_CAR_AVAIL1',0.740737,-10000,10000,0,'B_CAR_AVAIL1' )

B_CAR_AVAIL2 = Beta('B_CAR_AVAIL2',-0.88747,-10000,10000,0,'B_CAR_AVAIL2' )

B_CAR_AVAIL3 = Beta('B_CAR_AVAIL3',-3.23981,-10000,10000,0,'B_CAR_AVAIL3' )

ASC_WALK = Beta('ASC_WALK',0,-10000,10000,1,'ASC_WALK' )

B_WALK_DIST = Beta('B_WALK_DIST',-0.234344,-10000,10000,0,'B_WALK_DIST' )

B_TRIP_PURPOSE = Beta('B_TRIP_PURPOSE',-0.250109,-10000,10000,0,'B_TRIP_PURPOSE' )


## Code for the sensitivity analysis
names = ['ASC_CAR','ASC_TRAIN','B_CAR_AVAIL1','B_CAR_AVAIL2','B_CAR_AVAIL3','B_CAR_TIME','B_COST_CAR','B_COST_TRAIN','B_LANG_CODE','B_MALE_CAR','B_TRAIN_TIME','B_TRIP_PURPOSE','B_WALK_DIST']
values = [[0.288288,0.17451,-0.0385982,-0.042653,-0.0371705,0.000456558,-0.000998794,0.000132797,0.0395281,-0.00128593,0.000146799,0.0244668,0.0202332],[0.17451,0.174861,-0.00459877,-0.00258845,0.00656644,0.00055705,-0.00238575,-2.05434e-05,0.000487098,-0.000780697,6.56481e-05,0.0243596,0.0191451],[-0.0385982,-0.00459877,0.0442183,0.0387585,0.0367783,8.56449e-05,-0.000183773,7.646e-05,0.00180982,-0.00644401,-4.81817e-07,-0.00028402,-0.000629007],[-0.042653,-0.00258845,0.0387585,0.0637934,0.0363573,-0.000230987,0.000305887,-0.000106066,-0.000929529,-0.00410285,-7.45182e-05,-0.000679773,-0.000796315],[-0.0371705,0.00656644,0.0367783,0.0363573,0.210094,0.000380794,-0.00138193,-0.000112224,-0.00501301,-0.00186397,0.000108004,-0.00018891,0.00166361],[0.000456558,0.00055705,8.56449e-05,-0.000230987,0.000380794,0.000115325,-0.000363882,1.81729e-05,-8.49e-06,-0.000198237,2.09987e-05,2.96158e-05,0.000204598],[-0.000998794,-0.00238575,-0.000183773,0.000305887,-0.00138193,-0.000363882,0.00216762,0.000171036,-0.000266825,0.000180145,-3.77257e-05,-2.0962e-05,-0.000372826],[0.000132797,-2.05434e-05,7.646e-05,-0.000106066,-0.000112224,1.81729e-05,0.000171036,7.76337e-05,-1.62539e-05,-9.67975e-05,4.48527e-06,5.55834e-05,7.25331e-05],[0.0395281,0.000487098,0.00180982,-0.000929529,-0.00501301,-8.49e-06,-0.000266825,-1.62539e-05,0.022728,0.00042921,-2.51064e-05,-5.95995e-05,-0.000122537],[-0.00128593,-0.000780697,-0.00644401,-0.00410285,-0.00186397,-0.000198237,0.000180145,-9.67975e-05,0.00042921,0.0145235,-4.48074e-05,-0.000241678,-0.000350129],[0.000146799,6.56481e-05,-4.81817e-07,-7.45182e-05,0.000108004,2.09987e-05,-3.77257e-05,4.48527e-06,-2.51064e-05,-4.48074e-05,6.36098e-06,-5.03482e-07,5.43529e-05],[0.0244668,0.0243596,-0.00028402,-0.000679773,-0.00018891,2.96158e-05,-2.0962e-05,5.55834e-05,-5.95995e-05,-0.000241678,-5.03482e-07,0.00859072,0.00124326],[0.0202332,0.0191451,-0.000629007,-0.000796315,0.00166361,0.000204598,-0.000372826,7.25331e-05,-0.000122537,-0.000350129,5.43529e-05,0.00124326,0.00314833]]
vc = bioMatrix(13,names,values)
BIOGEME_OBJECT.VARCOVAR = vc