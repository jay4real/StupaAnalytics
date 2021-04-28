import pandas as pd
import pyodbc
import numpy as np
connectionString = "Driver={ODBC Driver 17 for SQL Server};Server=stupa-testdb.cf0xlnbvxxos.us-east-1.rds.amazonaws.com;Database=StupaAiProdDb;uid=admin;pwd=stupa-ai-dev1"
connection = pyodbc.connect(connectionString)
cursor = connection.cursor()
df = pd.read_sql("SELECT * FROM temp_tbl_Game where IsSynchronize=0", connection)

def GetShotCode(shot_full_form):
    # Remove this fetch and use the same before the function call
    tbl_shot_code = pd.read_sql("SELECT * FROM tbl_shot_code", connection)
    #-----------------------------------------
    code = tbl_shot_code[tbl_shot_code['ShotFullForm'] == shot_full_form]['ShotCode'] #Fetching the shot code using the fullForm
    if(len(code) == 0): # If the code is not present returning the empty string
        return ''
    else:
        # Typecast if it is required to string
        return code.values[0] # If the code value is present returning the corresponding value

def GetShotCodeID(shot_full_form):
    # Remove this fetch and use the same before the function call
    tbl_shot_code = pd.read_sql("SELECT * FROM tbl_shot_code", connection)
    code = tbl_shot_code[tbl_shot_code['ShotFullForm'] == shot_full_form]['ShotDefId'] #Fetching the shot code using the fullForm
    if(len(code) == 0):
        return ""
    else:
        # Typecast if it is required to string
        return code.values[0]

def GetScoreOnPointLevel(matchNo, gameNo, point):
    # Remove this fetch and use the same before the function call
    tbl_Primary_Database = pd.read_sql("SELECT * FROM tbl_Primary_Database", connection)
    # requiredTable = tbl_Primary_Database[(tbl_Primary_Database['Match_No'] == matchNo) & (tbl_Primary_Database['Game'] == gameNo) && (tbl_Primary_Database[POINT]<=point) && tbl_Primary_Database['ErrorType'] is not None && (tbl_Primary_Database['ErrorType'] > 1)]
    # print(requiredTable)
    print(len(tbl_Primary_Database['ErrorType']))