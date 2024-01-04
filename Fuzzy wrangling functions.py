from typing import Callable
import jellyfish as jf

def jf_ElementWiseListPair(jfFunc: Callable, xList: list, yList: list):
    return [jfFunc(xList[i], yList[i]) for i in range(len(xList))]




import pandas as pd
import jellyfish as jf
import numpy as np
from itertools import product



def fuzzyScoreLists(df_WReceivingVals:pd.DataFrame,
                    col_ReceivingVals:str,
                    df_WValsCouldAssign:pd.DataFrame,
                    col_ValsCouldAssign:str,
                    groupingVarsDict:dict):

    col_ReceivingVals_Renamed = col_ReceivingVals + "_ReceivingVals"
    col_ValsCouldAssign_Renamed = col_ValsCouldAssign + "_ValsCouldAssign"

    ReceivingVals_Df = (df_WReceivingVals[[col_ReceivingVals] + list(groupingVarsDict.keys())]
                        .rename(columns = {col_ReceivingVals: col_ReceivingVals_Renamed})
                        )
    
    ValsCouldAssign_Df = (df_WValsCouldAssign[[col_ValsCouldAssign] + list(groupingVarsDict.values())]
                          .rename(columns = {col_ValsCouldAssign: col_ValsCouldAssign_Renamed})
                          )
                          

    if groupingVarsDict:
        LeftJoined_Df = pd.merge(ReceivingVals_Df,
                             ValsCouldAssign_Df,
                             how = "left",
                             left_on = list(groupingVarsDict.keys()),
                             right_on = list(groupingVarsDict.values())
                             )
        

        
    else:
        LeftJoined_Df = product(ReceivingVals_Df[col_ReceivingVals_Renamed],
                            ValsCouldAssign_Df[col_ValsCouldAssign_Renamed])     
        

#Get fuzzy scores, excluding cases where one of the two columns contains an NA.
    Conditions = [
        pd.isna(LeftJoined_Df[col_ReceivingVals_Renamed]) | pd.isna(LeftJoined_Df[col_ValsCouldAssign_Renamed])
        # You can add more conditions here if needed
    ]

    Choices = [
        np.nan
    ]


    FuzzyScores_Df = LeftJoined_Df

    
    FuzzyScores_Df['FuzzyScore'] = FuzzyScores_Df.apply(
        lambda row: np.nan if pd.isna(row[col_ReceivingVals_Renamed]) or pd.isna(row[col_ValsCouldAssign_Renamed])
        else jf_ElementWiseListPair(jf.damerau_levenshtein_distance, [row[col_ReceivingVals_Renamed]], [row[col_ValsCouldAssign_Renamed]])[0],
        axis=1
    )

    return FuzzyScores_Df


FuzzyMatchResults = fuzzyScoreLists(df_WReceivingVals = NonMatchingLocs_EttV6,
                                    col_ReceivingVals = "M-2453: Location Name",
                                    df_WValsCouldAssign = NonMatchingLocs_EttV7,
                                    col_ValsCouldAssign = "M-2453: Location Name",
                                    groupingVarsDict = {"M-0298: Region Name": "M-0298: Region Name",
                                                    "M-0299: District Name": "M-0299: District Name"}
                                   )

