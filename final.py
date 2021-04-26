df = pd.read_csv('/content/drive/MyDrive/DoR/cases_train_processed.csv')



#drops all the columns not used in X_train
def colsToDrop(dataframe,drop_list):
  for column in drop_list:
    if column in dataframe.columns:
      dataframe = dataframe.drop(column,1)
      print('dropping Column {}'.format(column))
  return dataframe

def impute(dataframe,na_list):
  # n_list = dataframe.columns[dataframe.isna().any()].tolist()
  # print(n_list)
  print('na_list',na_list)
  for col in na_list:
    if dataframe[col].isna().any():
      dataframe[col].fillna(dataframe[col].mean(),inplace=True)

def setDtypes(dataframe,dt):
  if 'date_confirmation' in dataframe.columns:
    dataframe.date_confirmation = pd.to_datetime(dataframe.date_confirmation,infer_datetime_format=True)
    print('date format is ',dataframe.date_confirmation.dtype)

    for datatype, col_list in dt.items():
      impute(dataframe,col_list)
      for column in col_list:
        if column in dataframe.columns:
          dataframe[column] = dataframe[column].astype(datatype)
          print("{} is now {}".format(column,datatype))
  
  return dataframe   


def basicPreProcess(dataframe):
  drop_list = ['Combined_Key','Unnamed: 0','index','source','additional_information',
               'Last_Update','Lat_right','Long_right','Province_State','Country_Region',
               'dist_between_in_km']
  dtypeDict = {'float64':['Incidence_Rate','Case-Fatality_Ratio'],
               'int64':['Active','age','Confirmed','Deaths','Recovered']}
  print('Dropping unused columns')
  dataframe = colsToDrop(dataframe,drop_list)
  print('-------------------------------------------\n')
  print('Imputing any missing Data and Setting proper Datatypes')
  # dt = ['Incidence_Rate','Case-Fatality_Ratio','Active','age','Confirmed','Deaths','Recovered']
  # impute(dataframe,dt)
  dataframe = setDtypes(dataframe,dtypeDict) 
  print('-------------------------------------------\n')
  print("Binning dates into 2 week periods and creating date_labels column") 
  dateBinDict = getDateBins(dataframe.date_confirmation) # need to set dtypes before binning
  dataframe['date_labels'] = dataframe.date_confirmation.apply(lambda curr_date : binDate(curr_date,dateBinDict))
  print('-------------------------------------------\n')
  print("Dropping Date Confirmation Column")
  dataframe = colsToDrop(dataframe,['date_confirmation'])
  return dataframe
  
  


#step 1 basic preproc
preprocessedData = basicPreProcess(df) 
# step2 
# # Perform Oversampling before ohe.
# #so drop columns not used in independent var 
independentVars = colsToDrop(asd,['outcome'])
# #get list of categorical indices
catIndList = getCategoricalIndices(independentVars)
#oversample 
oversample = SMOTENC(categorical_features=catIndList,random_state=0,sampling_strategy='minority')
x_o,y_o = oversample.fit_resample(independentVars,asd.outcome)