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
#B_MALE_CAR = Beta('B_MALE_CAR',0,-10000,10000,0)
#B_MALE_TRAIN = Beta('B_MALE_TRAIN',0,-10000,10000,0)
B_TRIP_PURPOSE = Beta('B_TRIP_PURPOSE',0,-10000,10000,0)
#B_URBAN_RURAL = Beta('B_URBAN_RURAL',0,-10000,10000,0)
#B_TYPE_COMMUNE_TRAIN = Beta('B_TYPE_COMMUNE_TRAIN',0,-10000,10000,0)
#B_TYPE_COMMUNE_CAR1 = Beta('B_TYPE_COMMUNE_CAR1',0,-10000,10000,1)
#B_TYPE_COMMUNE_CAR2 = Beta('B_TYPE_COMMUNE_CAR2',0,-10000,10000,1)
B_LANG_CODE = Beta('B_LANG_CODE',0,-10000,10000,0)
#B_AGE = Beta('B_AGE',0,-10000,10000,0)
#B_MOTHER_TONGUE = Beta('B_MOTHER_TONGUE',0,-10000,10000,0), same as lang code

# non-linear
B_CAR_AVAIL1 = Beta('B_CAR_AVAIL1',0,-10000,10000,0)
B_CAR_AVAIL2 = Beta('B_CAR_AVAIL2',0,-10000,10000,0)
B_CAR_AVAIL3 = Beta('B_CAR_AVAIL3',0,-10000,10000,0)
B_FreqCarPar1 = Beta('B_FreqCarPar1',0,-10000,10000,1)
B_FreqCarPar2 = Beta('B_FreqCarPar2',0,-10000,10000,0)
B_FreqCarPar34 = Beta('B_FreqCarPar3',0,-10000,10000,0)
#B_FreqCarPar4 = Beta('B_FreqCarPar4',0,-10000,10000,0)
#Box-Cox
LAMBDA = Beta('LAMBDA', 1, -10, 10 ,0 )
#LAMBDA_CAR	 = Beta('LAMBDA_CAR',1,-100,100,0)
#LAMBDA_TRAIN	 = Beta('LAMBDA_TRAIN',1,-100,100,0)
LAMBDA_WALK =   Beta('LAMBDA_WALK',1,-10,10,0)

# Interaction
#B_INCOME_OVER_PRICE1 = Beta('B_INCOME_OVER_PRICE1',0,-10000,10000,0)
#B_INCOME_OVER_PRICE2 = Beta('B_INCOME_OVER_PRICE2',0,-10000,10000,0)


# parameters relevant to the nests
#MU_classic = Beta('MU_classic',1,1,10,0)

#########################################################################################################
# [Expressions]one  = DefineVariable('one',1)
one  = DefineVariable('one',1)
CAR_TIME  = DefineVariable('TimeCar1', TimeCar)
TRAIN_TIME  = DefineVariable('TimePT1', TimePT)
DISTANCE  = DefineVariable('DISTANCE1', distance_km)
TRAIN_COST  = DefineVariable('TRAIN_COST1', MarginalCostPT)
CAR_COST = DefineVariable('CAR_COST1', CostCarCHF)
#MALE = DefineVariable('MALE', Gender == 1)
TRIP_PURPOSE = DefineVariable('TRIP_PURPOSE1', TripPurpose)
#URBAN_RURAL = DefineVariable('URBAN_RURAL1', UrbRur)
#TYPE_COMMUNE_TRAIN = DefineVariable('TYPE_COMMUNE_TRAIN1', TypeCommune)
#TYPE_COMMUNE_CAR1 = DefineVariable('TYPE_COMMUNE_CAR1', TypeCommune == 1)
#TYPE_COMMUNE_CAR2 = DefineVariable('TYPE_COMMUNE_CAR2', TypeCommune != 1)
LANG_CODE = DefineVariable('LANG_CODE1', LangCode)
#AGE = DefineVariable('AGE1', age)
#MOTHER_TONGUE = DefineVariable('MOTHER_TONGUE1', Mothertongue)
CAR_AVAIL1 = DefineVariable('CAR_AVAIL1',CarAvail == 1)
CAR_AVAIL2 = DefineVariable('CAR_AVAIL2',CarAvail == 2)
CAR_AVAIL3 = DefineVariable('CAR_AVAIL3',CarAvail == 3)
FREQ_CAR_PAR1 = DefineVariable('FREQ_CAR_PAR1', FreqCarPar == 1)
FREQ_CAR_PAR2 = DefineVariable('FREQ_CAR_PAR2', FreqCarPar == 2)
FREQ_CAR_PAR34 = DefineVariable('FREQ_CAR_PAR34', FreqCarPar >= 3)
#FREQ_CAR_PAR4 = DefineVariable('FREQ_CAR_PAR4', FreqCarPar == 4)

# Interaction
#INCOME_OVER_PRICE = DefineVariable('INCOME_OVER_PRICE1',Income/)


#########################################################################################################
#[Utilities]

#  + B_INCOME_OVER_PRICE2 * CAR_COST/Income
V1 = ASC_TRAIN * one + B_COST_TRAIN * TRAIN_COST + B_LANG_CODE * LANG_CODE + ( ( ( TRAIN_TIME   **  LAMBDA   ) -  1  ) /  LAMBDA   ) * B_TRAIN_TIME
V2 = ASC_CAR * one + B_COST_CAR * CAR_COST + B_CAR_AVAIL1 * CAR_AVAIL1 + B_CAR_AVAIL2 * CAR_AVAIL2 + B_CAR_AVAIL3 * CAR_AVAIL3 + B_FreqCarPar1*FREQ_CAR_PAR1 + B_FreqCarPar2*FREQ_CAR_PAR2 + B_FreqCarPar34*FREQ_CAR_PAR34 + B_CAR_TIME * ( ( ( CAR_TIME   **  LAMBDA   ) -  1  ) /  LAMBDA  )
V3 = ASC_WALK * one + B_TRIP_PURPOSE * TRIP_PURPOSE+ B_LANG_CODE * LANG_CODE + B_WALK_DIST *  ( ( ( DISTANCE ** LAMBDA_WALK ) - 1 ) / LAMBDA_WALK )

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


