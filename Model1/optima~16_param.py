# This file has automatically been generated
# biogeme 2.5 [Die Okt 4 11:31:19 CEST 2016]
# <a href='http://people.epfl.ch/michel.bierlaire'>Michel Bierlaire</a>, <a href='http://transp-or.epfl.ch'>Transport and Mobility Laboratory</a>, <a href='http://www.epfl.ch'>Ecole Polytechnique F&eacute;d&eacute;rale de Lausanne (EPFL)</a>
# Tue Nov 22 11:02:00 2016</p>
#
ASC_TRAIN = Beta('ASC_TRAIN',-0.859816,-10000,10000,0,'ASC_TRAIN' )

B_TRAIN_TIME = Beta('B_TRAIN_TIME',-0.0157175,-10000,10000,0,'B_TRAIN_TIME' )

B_COST_TRAIN = Beta('B_COST_TRAIN',0.0159793,-10000,10000,0,'B_COST_TRAIN' )

B_LANG_CODE = Beta('B_LANG_CODE',1.35488,-10000,10000,0,'B_LANG_CODE' )

ASC_CAR = Beta('ASC_CAR',1.01216,-10000,10000,0,'ASC_CAR' )

B_CAR_TIME = Beta('B_CAR_TIME',-0.0337634,-10000,10000,0,'B_CAR_TIME' )

B_COST_CAR = Beta('B_COST_CAR',0.0459101,-10000,10000,0,'B_COST_CAR' )

B_MALE_CAR = Beta('B_MALE_CAR',-0.0884179,-10000,10000,0,'B_MALE_CAR' )

B_TYPE_COMMUNE_CAR1 = Beta('B_TYPE_COMMUNE_CAR1',-0.0221277,-10000,10000,0,'B_TYPE_COMMUNE_CAR1' )

B_TYPE_COMMUNE_CAR2 = Beta('B_TYPE_COMMUNE_CAR2',1.03429,-10000,10000,0,'B_TYPE_COMMUNE_CAR2' )

B_CAR_AVAIL1 = Beta('B_CAR_AVAIL1',0.708119,-10000,10000,0,'B_CAR_AVAIL1' )

B_CAR_AVAIL2 = Beta('B_CAR_AVAIL2',-0.902473,-10000,10000,0,'B_CAR_AVAIL2' )

B_CAR_AVAIL3 = Beta('B_CAR_AVAIL3',-3.26712,-10000,10000,0,'B_CAR_AVAIL3' )

ASC_WALK = Beta('ASC_WALK',0,-10000,10000,1,'ASC_WALK' )

B_WALK_DIST = Beta('B_WALK_DIST',-0.231139,-10000,10000,0,'B_WALK_DIST' )

B_TRIP_PURPOSE = Beta('B_TRIP_PURPOSE',-0.241297,-10000,10000,0,'B_TRIP_PURPOSE' )


## Code for the sensitivity analysis
names = ['ASC_CAR','ASC_TRAIN','B_CAR_AVAIL1','B_CAR_AVAIL2','B_CAR_AVAIL3','B_CAR_TIME','B_COST_CAR','B_COST_TRAIN','B_LANG_CODE','B_MALE_CAR','B_TRAIN_TIME','B_TRIP_PURPOSE','B_TYPE_COMMUNE_CAR1','B_TYPE_COMMUNE_CAR2','B_WALK_DIST']
values = [[-2.45935e+10,1.17479e+10,-6.42649e+08,-9.24238e+07,9.39877e+09,1.00386e+08,-4.67868e+08,-3.99202e+07,3.9815e+08,-1.19292e+08,1.877e+07,-6.08468e+08,3.28045e+10,3.60539e+10,1.99825e+09],[0.11527,0.17243,-0.0051666,-0.00318431,0.00605511,0.000564177,-0.00228041,1.84066e-05,0.00131656,-0.000995928,6.96497e-05,0.0237837,0.0434585,0.0600751,0.0190323],[-0.21867,-0.0185337,0.0457284,0.0393259,0.0170915,-8.34604e-05,0.000556942,0.000112398,0.000826066,-0.0063745,-2.37033e-05,0.00193991,0.178208,0.166385,-0.0032393],[-0.24304,-0.0176476,0.0402895,0.0645797,0.0147969,-0.000419362,0.00113281,-6.28837e-05,-0.00212146,-0.00409558,-0.000100118,0.00168126,0.198231,0.185616,-0.0035789],[-0.676574,-0.0355061,0.0400239,0.0368212,0.146082,-8.55592e-05,0.000832511,1.97236e-05,-0.00792204,-0.00115602,5.51083e-05,0.00717282,0.61499,0.599059,-0.0061654],[-0.000222558,0.000549758,5.46154e-05,-0.000270629,0.000315751,0.000115481,-0.00035803,1.94981e-05,9.5897e-05,-0.000192554,2.12656e-05,3.97741e-05,-6.4231e-05,0.00090636,0.000204179],[0.00323298,-0.00217978,-0.000139216,0.000385312,-0.00109403,-0.000357633,0.00211358,0.000165752,-0.000365729,0.000175706,-3.81466e-05,-4.68979e-05,-0.00306505,-0.00429837,-0.000350227],[0.000814649,3.28203e-05,5.9333e-05,-0.000118728,-9.60522e-05,1.96429e-05,0.000165056,7.80719e-05,4.91912e-05,-9.31531e-05,4.55099e-06,5.90387e-05,-0.0010262,-0.000493395,7.82953e-05],[0.077797,0.00452455,0.00124084,-0.00142981,-0.000815114,0.000130271,-0.000542247,3.54125e-05,0.0267786,6.6996e-05,6.39488e-06,-0.000581141,-0.0495946,-0.0263489,0.000882254],[0.0152962,9.79236e-05,-0.00672728,-0.00440124,-0.000370479,-0.000181664,0.00012232,-9.67237e-05,0.000190219,0.0145764,-4.22789e-05,-0.000455265,-0.0173671,-0.0162327,-0.000145963],[1.09835e-05,6.925e-05,-8.06206e-06,-8.34407e-05,9.96545e-05,2.12697e-05,-3.81547e-05,4.5524e-06,2.7621e-06,-4.34917e-05,6.43908e-06,1.16652e-06,-5.81716e-05,0.00019899,5.50888e-05],[0.0193988,0.0239028,-0.000386759,-0.000867114,-9.51839e-05,3.73721e-05,-2.10554e-05,6.53338e-05,2.58343e-05,-0.000262439,8.40311e-07,0.00845955,0.00201458,0.00504594,0.00123397],[2.45935e+10,-1.17479e+10,6.42649e+08,9.24238e+07,-9.39877e+09,-1.00386e+08,4.67868e+08,3.99202e+07,-3.9815e+08,1.19292e+08,-1.877e+07,6.08468e+08,-3.28045e+10,-3.60539e+10,-1.99825e+09],[2.45935e+10,-1.17479e+10,6.42649e+08,9.24238e+07,-9.39877e+09,-1.00386e+08,4.67868e+08,3.99202e+07,-3.9815e+08,1.19292e+08,-1.877e+07,6.08468e+08,-3.28045e+10,-3.60539e+10,-1.99825e+09],[0.013235,0.0190296,-0.000777009,-0.000910011,0.00152373,0.000206984,-0.000370433,7.51571e-05,0.000286015,-0.000348184,5.52027e-05,0.00121094,0.00375211,0.0078781,0.00314604]]
vc = bioMatrix(15,names,values)
BIOGEME_OBJECT.VARCOVAR = vc
