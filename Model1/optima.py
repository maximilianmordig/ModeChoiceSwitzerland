#########################################################################################################
# Translated to .py by Evanthia Kazagli
# Oct. 2016
#########################################################################################################

# NL
from biogeme import *
from headers import *
from mev import *
from nested import *
from loglikelihood import *
from statistics import *
  

## Choice
__chosenAlternative = (Choice + 1)

#########################################################################################################
# [Parameters]
# Arguments:
#   Beta('Name', starting value, lower bound, upper bound, 0: estimate the parameter, 1: keep it fixed)
ASC_CAR	= Beta('ASC_CAR',0,-10000,10000,0)
ASC_TRAIN	= Beta('ASC_TRAIN',0,-10000,10000,0)
ASC_WALK = Beta('ASC_WALK',0,-10000,10000,1)
B_CAR_TIME = Beta('B_CAR_TIME',0,-10000,10000,0)
B_TRAIN_TIME = Beta('B_TRAIN_TIME',0,-10000,10000,0)
B_WALK_DIST = Beta('B_WALK_DIST',0,-10000,10000,0)
B_COST_TRAIN = Beta('B_COST_TRAIN',0,-10000,10000,0)
B_COST_CAR = Beta('B_COST_CAR',-0,-10000,10000,0)
B_MALE_CAR = Beta('B_MALE_CAR',0,-10000,10000,0)
B_MALE_TRAIN = Beta('B_MALE_TRAIN',0,-10000,10000,0)
# parameters relevant to the nests
#MU_classic = Beta('MU_classic',1,1,10,0)

#########################################################################################################
# [Expressions]one  = DefineVariable('one',1)
one  = DefineVariable('one',1)
CAR_TIME  = DefineVariable('TimeCar1', TimeCar)
TRAIN_TIME  = DefineVariable('TimePT1', TimePT)
DISTANCE  = DefineVariable('DISTANCE1', distance_km)
TRAIN_COST  = DefineVariable('TRAIN_COST1', CostPT)
CAR_COST = DefineVariable('CAR_COST1', CostCarCHF)
MALE = DefineVariable('MALE', Gender == 1)
#########################################################################################################
#[Utilities]
V1 = ASC_TRAIN * one + B_TRAIN_TIME * TRAIN_TIME + B_COST_TRAIN * TRAIN_COST 
V2 = ASC_CAR * one + B_CAR_TIME * CAR_TIME + B_COST_CAR * CAR_COST + B_MALE_CAR * MALE
V3 = ASC_WALK * one + B_WALK_DIST *  DISTANCE + B_MALE_TRAIN * MALE

__V = {1: V1, 2: V2, 3: V3}

__av = {1: one,2: one,3: one}
#av = {1: TRAIN_AV_SP, 2: SM_AV, 3: CAR_AV_SP}

#[Exclude]
#exclude = (( PURPOSE != 1 ) * (  PURPOSE   !=  3  ) + ( CHOICE == 0 )) + ( AGE   ==  6  ) > 0
exclude = (Choice == -1)
BIOGEME_OBJECT.EXCLUDE = exclude

#########################################################################################################
#[Definition of nests]
#innovative = 1.0, [2]
#classic = MU_classic, [1, 3]

#nests = classic, innovative

#########################################################################################################
#[Model]
# NL
#logprob = lognested(V,av,nests,CHOICE)
prob = bioLogit(__V,__av,__chosenAlternative)
__l = log(prob)


# Defines an itertor on the data
rowIterator('obsIter')

# Define the likelihood function for the estimation
BIOGEME_OBJECT.ESTIMATE = Sum(__l,'obsIter')


#########################################################################################################
# [Estimation]
#BIOGEME_OBJECT.ESTIMATE = Sum(logprob,'obsIter')

#########################################################################################################
# [Statistics]
#nullLoglikelihood(__av,'obsIter')
#choiceSet = [1,2,3]
#cteLoglikelihood(choiceSet,choice,'obsIter')
#availabilityStatistics(av,'obsIter')

#########################################################################################################
# [BIOGEME_OBJECT]
#BIOGEME_OBJECT.PARAMETERS['optimizationAlgorithm'] = "BIO"

#BIOGEME_OBJECT.FORMULAS['Train utility'] = V1
#BIOGEME_OBJECT.FORMULAS['Swissmetro utility'] = V2
#BIOGEME_OBJECT.FORMULAS['Car utility'] = V3

# The following parameters are imported from bison biogeme. You may want to remove them and prefer the default value provided by pythonbiogeme.
BIOGEME_OBJECT.PARAMETERS['optimizationAlgorithm'] = "BIO"
BIOGEME_OBJECT.PARAMETERS['stopFileName'] = "STOP"


