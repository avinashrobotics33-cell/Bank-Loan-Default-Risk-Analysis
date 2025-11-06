Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import itertools
%matplotlib inline
import warnings
warnings.filterwarnings('ignore')
applicationDF=pd.read_csv(r"C:\Users\Lenovo\Desktop\Pyhton_Practice\01-03-2022\application_data.csv")

previousDF=pd.read_csv(r"C:\Users\Lenovo\Desktop\Pyhton_Practice\01-03-2022\previous_application.csv")
applicationDF
        SK_ID_CURR  TARGET  ... Unnamed: 122 descrip
0           100002       1  ...          NaN     NaN
1           100003       0  ...          NaN     NaN
2           100004       0  ...          NaN     NaN
3           100006       0  ...          NaN     NaN
4           100007       0  ...          NaN     NaN
...            ...     ...  ...          ...     ...
307506      456251       0  ...          NaN     NaN
307507      456252       0  ...          NaN     NaN
307508      456253       0  ...          NaN     NaN
307509      456254       1  ...          NaN     NaN
307510      456255       0  ...          NaN     NaN

[307511 rows x 124 columns]
previousDF
         SK_ID_PREV  SK_ID_CURR  ... DAYS_TERMINATION  NFLAG_INSURED_ON_APPROVAL
0           2030495      271877  ...            -37.0                        0.0
1           2802425      108129  ...         365243.0                        1.0
2           2523466      122040  ...         365243.0                        1.0
3           2819243      176158  ...           -177.0                        1.0
4           1784265      202054  ...              NaN                        NaN
...             ...         ...  ...              ...                        ...
1048570     2230795      255000  ...              NaN                        NaN
1048571     1823303      158245  ...              NaN                        NaN
1048572     1730537      429268  ...          -2118.0                        1.0
1048573     2100360      389043  ...          -2616.0                        1.0
1048574     1283481      250078  ...          -2420.0                        1.0

[1048575 rows x 37 columns]
previousDF.head()
   SK_ID_PREV  SK_ID_CURR  ... DAYS_TERMINATION  NFLAG_INSURED_ON_APPROVAL
0     2030495      271877  ...            -37.0                        0.0
1     2802425      108129  ...         365243.0                        1.0
2     2523466      122040  ...         365243.0                        1.0
3     2819243      176158  ...           -177.0                        1.0
4     1784265      202054  ...              NaN                        NaN

[5 rows x 37 columns]
print("Database dimension-applicationDF :",applicationDF.shape)
Database dimension-applicationDF : (307511, 124)
previousDF.shape
(1048575, 37)
applicationDF.shape
(307511, 124)
print("Database size-applicationDF :",applicationDF.size)
Database size-applicationDF : 38131364
print("Database-previousDF :",previousDF.size)
Database-previousDF : 38797275
applicationDF.info(verbose=True)
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 307511 entries, 0 to 307510
Data columns (total 124 columns):
 #    Column                        Dtype  
---   ------                        -----  
 0    SK_ID_CURR                    int64  
 1    TARGET                        int64  
 2    NAME_CONTRACT_TYPE            object 
 3    CODE_GENDER                   object 
 4    FLAG_OWN_CAR                  object 
 5    FLAG_OWN_REALTY               object 
 6    CNT_CHILDREN                  int64  
 7    AMT_INCOME_TOTAL              float64
 8    AMT_CREDIT                    float64
 9    AMT_ANNUITY                   float64
 10   AMT_GOODS_PRICE               float64
 11   NAME_TYPE_SUITE               object 
 12   NAME_INCOME_TYPE              object 
 13   NAME_EDUCATION_TYPE           object 
 14   NAME_FAMILY_STATUS            object 
 15   NAME_HOUSING_TYPE             object 
 16   REGION_POPULATION_RELATIVE    float64
 17   DAYS_BIRTH                    int64  
 18   DAYS_EMPLOYED                 int64  
 19   DAYS_REGISTRATION             float64
 20   DAYS_ID_PUBLISH               int64  
 21   OWN_CAR_AGE                   float64
 22   FLAG_MOBIL                    int64  
 23   FLAG_EMP_PHONE                int64  
 24   FLAG_WORK_PHONE               int64  
 25   FLAG_CONT_MOBILE              int64  
 26   FLAG_PHONE                    int64  
 27   FLAG_EMAIL                    int64  
 28   OCCUPATION_TYPE               object 
 29   CNT_FAM_MEMBERS               float64
 30   REGION_RATING_CLIENT          int64  
 31   REGION_RATING_CLIENT_W_CITY   int64  
 32   WEEKDAY_APPR_PROCESS_START    object 
 33   HOUR_APPR_PROCESS_START       int64  
 34   REG_REGION_NOT_LIVE_REGION    int64  
 35   REG_REGION_NOT_WORK_REGION    int64  
 36   LIVE_REGION_NOT_WORK_REGION   int64  
 37   REG_CITY_NOT_LIVE_CITY        int64  
 38   REG_CITY_NOT_WORK_CITY        int64  
 39   LIVE_CITY_NOT_WORK_CITY       int64  
 40   ORGANIZATION_TYPE             object 
 41   EXT_SOURCE_1                  float64
 42   EXT_SOURCE_2                  float64
 43   EXT_SOURCE_3                  float64
 44   APARTMENTS_AVG                float64
 45   BASEMENTAREA_AVG              float64
 46   YEARS_BEGINEXPLUATATION_AVG   float64
 47   YEARS_BUILD_AVG               float64
 48   COMMONAREA_AVG                float64
 49   ELEVATORS_AVG                 float64
 50   ENTRANCES_AVG                 float64
 51   FLOORSMAX_AVG                 float64
 52   FLOORSMIN_AVG                 float64
 53   LANDAREA_AVG                  float64
 54   LIVINGAPARTMENTS_AVG          float64
 55   LIVINGAREA_AVG                float64
 56   NONLIVINGAPARTMENTS_AVG       float64
 57   NONLIVINGAREA_AVG             float64
 58   APARTMENTS_MODE               float64
 59   BASEMENTAREA_MODE             float64
 60   YEARS_BEGINEXPLUATATION_MODE  float64
 61   YEARS_BUILD_MODE              float64
 62   COMMONAREA_MODE               float64
 63   ELEVATORS_MODE                float64
 64   ENTRANCES_MODE                float64
 65   FLOORSMAX_MODE                float64
 66   FLOORSMIN_MODE                float64
 67   LANDAREA_MODE                 float64
 68   LIVINGAPARTMENTS_MODE         float64
 69   LIVINGAREA_MODE               float64
 70   NONLIVINGAPARTMENTS_MODE      float64
 71   NONLIVINGAREA_MODE            float64
 72   APARTMENTS_MEDI               float64
 73   BASEMENTAREA_MEDI             float64
 74   YEARS_BEGINEXPLUATATION_MEDI  float64
 75   YEARS_BUILD_MEDI              float64
 76   COMMONAREA_MEDI               float64
 77   ELEVATORS_MEDI                float64
 78   ENTRANCES_MEDI                float64
 79   FLOORSMAX_MEDI                float64
 80   FLOORSMIN_MEDI                float64
 81   LANDAREA_MEDI                 float64
 82   LIVINGAPARTMENTS_MEDI         float64
 83   LIVINGAREA_MEDI               float64
 84   NONLIVINGAPARTMENTS_MEDI      float64
 85   NONLIVINGAREA_MEDI            float64
 86   FONDKAPREMONT_MODE            object 
 87   HOUSETYPE_MODE                object 
 88   TOTALAREA_MODE                float64
 89   WALLSMATERIAL_MODE            object 
 90   EMERGENCYSTATE_MODE           object 
 91   OBS_30_CNT_SOCIAL_CIRCLE      float64
 92   DEF_30_CNT_SOCIAL_CIRCLE      float64
 93   OBS_60_CNT_SOCIAL_CIRCLE      float64
 94   DEF_60_CNT_SOCIAL_CIRCLE      float64
 95   DAYS_LAST_PHONE_CHANGE        float64
 96   FLAG_DOCUMENT_2               int64  
 97   FLAG_DOCUMENT_3               int64  
 98   FLAG_DOCUMENT_4               int64  
 99   FLAG_DOCUMENT_5               int64  
 100  FLAG_DOCUMENT_6               int64  
 101  FLAG_DOCUMENT_7               int64  
 102  FLAG_DOCUMENT_8               int64  
 103  FLAG_DOCUMENT_9               int64  
 104  FLAG_DOCUMENT_10              int64  
 105  FLAG_DOCUMENT_11              int64  
 106  FLAG_DOCUMENT_12              int64  
 107  FLAG_DOCUMENT_13              int64  
 108  FLAG_DOCUMENT_14              int64  
 109  FLAG_DOCUMENT_15              int64  
 110  FLAG_DOCUMENT_16              int64  
 111  FLAG_DOCUMENT_17              int64  
 112  FLAG_DOCUMENT_18              int64  
 113  FLAG_DOCUMENT_19              int64  
 114  FLAG_DOCUMENT_20              int64  
 115  FLAG_DOCUMENT_21              int64  
 116  AMT_REQ_CREDIT_BUREAU_HOUR    float64
 117  AMT_REQ_CREDIT_BUREAU_DAY     float64
 118  AMT_REQ_CREDIT_BUREAU_WEEK    float64
 119  AMT_REQ_CREDIT_BUREAU_MON     float64
 120  AMT_REQ_CREDIT_BUREAU_QRT     float64
 121  AMT_REQ_CREDIT_BUREAU_YEAR    float64
 122  Unnamed: 122                  float64
 123  descrip                       float64
dtypes: float64(67), int64(41), object(16)
memory usage: 290.9+ MB

previousDF.info(verbose=True)
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1048575 entries, 0 to 1048574
Data columns (total 37 columns):
 #   Column                       Non-Null Count    Dtype  
---  ------                       --------------    -----  
 0   SK_ID_PREV                   1048575 non-null  int64  
 1   SK_ID_CURR                   1048575 non-null  int64  
 2   NAME_CONTRACT_TYPE           1048575 non-null  object 
 3   AMT_ANNUITY                  815566 non-null   float64
 4   AMT_APPLICATION              1048575 non-null  float64
 5   AMT_CREDIT                   1048575 non-null  float64
 6   AMT_DOWN_PAYMENT             489179 non-null   float64
 7   AMT_GOODS_PRICE              807610 non-null   float64
 8   WEEKDAY_APPR_PROCESS_START   1048575 non-null  object 
 9   HOUR_APPR_PROCESS_START      1048575 non-null  int64  
 10  FLAG_LAST_APPL_PER_CONTRACT  1048575 non-null  object 
 11  NFLAG_LAST_APPL_IN_DAY       1048575 non-null  int64  
 12  RATE_DOWN_PAYMENT            489179 non-null   float64
 13  RATE_INTEREST_PRIMARY        3721 non-null     float64
 14  RATE_INTEREST_PRIVILEGED     3721 non-null     float64
 15  NAME_CASH_LOAN_PURPOSE       1048575 non-null  object 
 16  NAME_CONTRACT_STATUS         1048575 non-null  object 
 17  DAYS_DECISION                1048575 non-null  int64  
 18  NAME_PAYMENT_TYPE            1048575 non-null  object 
 19  CODE_REJECT_REASON           1048575 non-null  object 
 20  NAME_TYPE_SUITE              533435 non-null   object 
 21  NAME_CLIENT_TYPE             1048575 non-null  object 
 22  NAME_GOODS_CATEGORY          1048575 non-null  object 
 23  NAME_PORTFOLIO               1048575 non-null  object 
 24  NAME_PRODUCT_TYPE            1048575 non-null  object 
 25  CHANNEL_TYPE                 1048575 non-null  object 
 26  SELLERPLACE_AREA             1048575 non-null  int64  
 27  NAME_SELLER_INDUSTRY         1048575 non-null  object 
 28  CNT_PAYMENT                  815569 non-null   float64
 29  NAME_YIELD_GROUP             1048575 non-null  object 
 30  PRODUCT_COMBINATION          1048351 non-null  object 
 31  DAYS_FIRST_DRAWING           627867 non-null   float64
 32  DAYS_FIRST_DUE               627867 non-null   float64
 33  DAYS_LAST_DUE_1ST_VERSION    627867 non-null   float64
 34  DAYS_LAST_DUE                627867 non-null   float64
 35  DAYS_TERMINATION             627867 non-null   float64
 36  NFLAG_INSURED_ON_APPROVAL    627867 non-null   float64
dtypes: float64(15), int64(6), object(16)
memory usage: 296.0+ MB
applicationDF.describe()
          SK_ID_CURR         TARGET  ...  Unnamed: 122  descrip
count  307511.000000  307511.000000  ...           0.0      0.0
mean   278180.518577       0.080729  ...           NaN      NaN
std    102790.175348       0.272419  ...           NaN      NaN
min    100002.000000       0.000000  ...           NaN      NaN
25%    189145.500000       0.000000  ...           NaN      NaN
50%    278202.000000       0.000000  ...           NaN      NaN
75%    367142.500000       0.000000  ...           NaN      NaN
max    456255.000000       1.000000  ...           NaN      NaN

[8 rows x 108 columns]
previousDF.describe()
         SK_ID_PREV    SK_ID_CURR  ...  DAYS_TERMINATION  NFLAG_INSURED_ON_APPROVAL
count  1.048575e+06  1.048575e+06  ...     627867.000000              627867.000000
mean   1.922775e+06  2.784367e+05  ...      81985.701661                   0.331530
std    5.329366e+05  1.028569e+05  ...     153298.887247                   0.470764
min    1.000001e+06  1.000010e+05  ...      -2874.000000                   0.000000
25%    1.460642e+06  1.893860e+05  ...      -1269.000000                   0.000000
50%    1.923419e+06  2.788100e+05  ...       -498.000000                   0.000000
75%    2.384448e+06  3.677445e+05  ...        -44.000000                   1.000000
max    2.845382e+06  4.562550e+05  ...     365243.000000                   1.000000

[8 rows x 21 columns]
import missingno as mn
mn.matrix(applicationDF)
<Axes: >
plt.show()
round(applicationDF.isnull().sum()/applicationDF.shape[0]*100.00,2)
SK_ID_CURR                      0.0
TARGET                          0.0
NAME_CONTRACT_TYPE              0.0
CODE_GENDER                     0.0
FLAG_OWN_CAR                    0.0
                              ...  
AMT_REQ_CREDIT_BUREAU_MON      13.5
AMT_REQ_CREDIT_BUREAU_QRT      13.5
AMT_REQ_CREDIT_BUREAU_YEAR     13.5
Unnamed: 122                  100.0
descrip                       100.0
Length: 124, dtype: float64
null_applicationDF=pd.DataFrame((applicationDF.isnull().sum()))
null_applicationDF=pd.DataFrame((applicationDF.isnull().sum())*00/applicationDF.shape[0]).reset_index()
null_applicationDF.columns=['Column Name', 'Null Values Percentage']
fig=plt.figure(figsize=(18,6))
ax=sns.pointplot(x="Column Name",y="Null Values Percentage",data=null_applicationDF,color='blue')
plt.xticks(rotation=90,fontsize=7)
([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123], [Text(0, 0, 'SK_ID_CURR'), Text(1, 0, 'TARGET'), Text(2, 0, 'NAME_CONTRACT_TYPE'), Text(3, 0, 'CODE_GENDER'), Text(4, 0, 'FLAG_OWN_CAR'), Text(5, 0, 'FLAG_OWN_REALTY'), Text(6, 0, 'CNT_CHILDREN'), Text(7, 0, 'AMT_INCOME_TOTAL'), Text(8, 0, 'AMT_CREDIT'), Text(9, 0, 'AMT_ANNUITY'), Text(10, 0, 'AMT_GOODS_PRICE'), Text(11, 0, 'NAME_TYPE_SUITE'), Text(12, 0, 'NAME_INCOME_TYPE'), Text(13, 0, 'NAME_EDUCATION_TYPE'), Text(14, 0, 'NAME_FAMILY_STATUS'), Text(15, 0, 'NAME_HOUSING_TYPE'), Text(16, 0, 'REGION_POPULATION_RELATIVE'), Text(17, 0, 'DAYS_BIRTH'), Text(18, 0, 'DAYS_EMPLOYED'), Text(19, 0, 'DAYS_REGISTRATION'), Text(20, 0, 'DAYS_ID_PUBLISH'), Text(21, 0, 'OWN_CAR_AGE'), Text(22, 0, 'FLAG_MOBIL'), Text(23, 0, 'FLAG_EMP_PHONE'), Text(24, 0, 'FLAG_WORK_PHONE'), Text(25, 0, 'FLAG_CONT_MOBILE'), Text(26, 0, 'FLAG_PHONE'), Text(27, 0, 'FLAG_EMAIL'), Text(28, 0, 'OCCUPATION_TYPE'), Text(29, 0, 'CNT_FAM_MEMBERS'), Text(30, 0, 'REGION_RATING_CLIENT'), Text(31, 0, 'REGION_RATING_CLIENT_W_CITY'), Text(32, 0, 'WEEKDAY_APPR_PROCESS_START'), Text(33, 0, 'HOUR_APPR_PROCESS_START'), Text(34, 0, 'REG_REGION_NOT_LIVE_REGION'), Text(35, 0, 'REG_REGION_NOT_WORK_REGION'), Text(36, 0, 'LIVE_REGION_NOT_WORK_REGION'), Text(37, 0, 'REG_CITY_NOT_LIVE_CITY'), Text(38, 0, 'REG_CITY_NOT_WORK_CITY'), Text(39, 0, 'LIVE_CITY_NOT_WORK_CITY'), Text(40, 0, 'ORGANIZATION_TYPE'), Text(41, 0, 'EXT_SOURCE_1'), Text(42, 0, 'EXT_SOURCE_2'), Text(43, 0, 'EXT_SOURCE_3'), Text(44, 0, 'APARTMENTS_AVG'), Text(45, 0, 'BASEMENTAREA_AVG'), Text(46, 0, 'YEARS_BEGINEXPLUATATION_AVG'), Text(47, 0, 'YEARS_BUILD_AVG'), Text(48, 0, 'COMMONAREA_AVG'), Text(49, 0, 'ELEVATORS_AVG'), Text(50, 0, 'ENTRANCES_AVG'), Text(51, 0, 'FLOORSMAX_AVG'), Text(52, 0, 'FLOORSMIN_AVG'), Text(53, 0, 'LANDAREA_AVG'), Text(54, 0, 'LIVINGAPARTMENTS_AVG'), Text(55, 0, 'LIVINGAREA_AVG'), Text(56, 0, 'NONLIVINGAPARTMENTS_AVG'), Text(57, 0, 'NONLIVINGAREA_AVG'), Text(58, 0, 'APARTMENTS_MODE'), Text(59, 0, 'BASEMENTAREA_MODE'), Text(60, 0, 'YEARS_BEGINEXPLUATATION_MODE'), Text(61, 0, 'YEARS_BUILD_MODE'), Text(62, 0, 'COMMONAREA_MODE'), Text(63, 0, 'ELEVATORS_MODE'), Text(64, 0, 'ENTRANCES_MODE'), Text(65, 0, 'FLOORSMAX_MODE'), Text(66, 0, 'FLOORSMIN_MODE'), Text(67, 0, 'LANDAREA_MODE'), Text(68, 0, 'LIVINGAPARTMENTS_MODE'), Text(69, 0, 'LIVINGAREA_MODE'), Text(70, 0, 'NONLIVINGAPARTMENTS_MODE'), Text(71, 0, 'NONLIVINGAREA_MODE'), Text(72, 0, 'APARTMENTS_MEDI'), Text(73, 0, 'BASEMENTAREA_MEDI'), Text(74, 0, 'YEARS_BEGINEXPLUATATION_MEDI'), Text(75, 0, 'YEARS_BUILD_MEDI'), Text(76, 0, 'COMMONAREA_MEDI'), Text(77, 0, 'ELEVATORS_MEDI'), Text(78, 0, 'ENTRANCES_MEDI'), Text(79, 0, 'FLOORSMAX_MEDI'), Text(80, 0, 'FLOORSMIN_MEDI'), Text(81, 0, 'LANDAREA_MEDI'), Text(82, 0, 'LIVINGAPARTMENTS_MEDI'), Text(83, 0, 'LIVINGAREA_MEDI'), Text(84, 0, 'NONLIVINGAPARTMENTS_MEDI'), Text(85, 0, 'NONLIVINGAREA_MEDI'), Text(86, 0, 'FONDKAPREMONT_MODE'), Text(87, 0, 'HOUSETYPE_MODE'), Text(88, 0, 'TOTALAREA_MODE'), Text(89, 0, 'WALLSMATERIAL_MODE'), Text(90, 0, 'EMERGENCYSTATE_MODE'), Text(91, 0, 'OBS_30_CNT_SOCIAL_CIRCLE'), Text(92, 0, 'DEF_30_CNT_SOCIAL_CIRCLE'), Text(93, 0, 'OBS_60_CNT_SOCIAL_CIRCLE'), Text(94, 0, 'DEF_60_CNT_SOCIAL_CIRCLE'), Text(95, 0, 'DAYS_LAST_PHONE_CHANGE'), Text(96, 0, 'FLAG_DOCUMENT_2'), Text(97, 0, 'FLAG_DOCUMENT_3'), Text(98, 0, 'FLAG_DOCUMENT_4'), Text(99, 0, 'FLAG_DOCUMENT_5'), Text(100, 0, 'FLAG_DOCUMENT_6'), Text(101, 0, 'FLAG_DOCUMENT_7'), Text(102, 0, 'FLAG_DOCUMENT_8'), Text(103, 0, 'FLAG_DOCUMENT_9'), Text(104, 0, 'FLAG_DOCUMENT_10'), Text(105, 0, 'FLAG_DOCUMENT_11'), Text(106, 0, 'FLAG_DOCUMENT_12'), Text(107, 0, 'FLAG_DOCUMENT_13'), Text(108, 0, 'FLAG_DOCUMENT_14'), Text(109, 0, 'FLAG_DOCUMENT_15'), Text(110, 0, 'FLAG_DOCUMENT_16'), Text(111, 0, 'FLAG_DOCUMENT_17'), Text(112, 0, 'FLAG_DOCUMENT_18'), Text(113, 0, 'FLAG_DOCUMENT_19'), Text(114, 0, 'FLAG_DOCUMENT_20'), Text(115, 0, 'FLAG_DOCUMENT_21'), Text(116, 0, 'AMT_REQ_CREDIT_BUREAU_HOUR'), Text(117, 0, 'AMT_REQ_CREDIT_BUREAU_DAY'), Text(118, 0, 'AMT_REQ_CREDIT_BUREAU_WEEK'), Text(119, 0, 'AMT_REQ_CREDIT_BUREAU_MON'), Text(120, 0, 'AMT_REQ_CREDIT_BUREAU_QRT'), Text(121, 0, 'AMT_REQ_CREDIT_BUREAU_YEAR'), Text(122, 0, 'Unnamed: 122'), Text(123, 0, 'descrip')])
ax.axhline(40, ls='--',color='red')
<matplotlib.lines.Line2D object at 0x000001F06859FB10>
plt.title("Percentage of Missing values in applicationdata")
Text(0.5, 1.0, 'Percentage of Missing values in applicationdata')
plt.ylabel("Percentage of Missing values in applicationdata")
Text(0, 0.5, 'Percentage of Missing values in applicationdata')
plt.ylabel("Null Values PERCENTAGE")
Text(0, 0.5, 'Null Values PERCENTAGE')
plt.xlabel("COLUMNS")
Text(0.5, 0, 'COLUMNS')
plt.show()
plt.show()
plt.ylabel("Null Values PERCENTAGE")
Text(0, 0.5, 'Null Values PERCENTAGE')
plt.show()
null_applicationDF = pd.DataFrame((applicationDF.isnull().sum())*100/applicationDF.shape[0]).reset_index()
null_applicationDF.columns = ['Column Name', 'Null Values Percentage']
fig = plt.figure(figsize=(18,6))
ax = sns.pointplot(x="Column Name",y="Null Values Percentage",data=null_applicationDF,color='blue')
plt.xticks(rotation =90,fontsize =7)
([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123], [Text(0, 0, 'SK_ID_CURR'), Text(1, 0, 'TARGET'), Text(2, 0, 'NAME_CONTRACT_TYPE'), Text(3, 0, 'CODE_GENDER'), Text(4, 0, 'FLAG_OWN_CAR'), Text(5, 0, 'FLAG_OWN_REALTY'), Text(6, 0, 'CNT_CHILDREN'), Text(7, 0, 'AMT_INCOME_TOTAL'), Text(8, 0, 'AMT_CREDIT'), Text(9, 0, 'AMT_ANNUITY'), Text(10, 0, 'AMT_GOODS_PRICE'), Text(11, 0, 'NAME_TYPE_SUITE'), Text(12, 0, 'NAME_INCOME_TYPE'), Text(13, 0, 'NAME_EDUCATION_TYPE'), Text(14, 0, 'NAME_FAMILY_STATUS'), Text(15, 0, 'NAME_HOUSING_TYPE'), Text(16, 0, 'REGION_POPULATION_RELATIVE'), Text(17, 0, 'DAYS_BIRTH'), Text(18, 0, 'DAYS_EMPLOYED'), Text(19, 0, 'DAYS_REGISTRATION'), Text(20, 0, 'DAYS_ID_PUBLISH'), Text(21, 0, 'OWN_CAR_AGE'), Text(22, 0, 'FLAG_MOBIL'), Text(23, 0, 'FLAG_EMP_PHONE'), Text(24, 0, 'FLAG_WORK_PHONE'), Text(25, 0, 'FLAG_CONT_MOBILE'), Text(26, 0, 'FLAG_PHONE'), Text(27, 0, 'FLAG_EMAIL'), Text(28, 0, 'OCCUPATION_TYPE'), Text(29, 0, 'CNT_FAM_MEMBERS'), Text(30, 0, 'REGION_RATING_CLIENT'), Text(31, 0, 'REGION_RATING_CLIENT_W_CITY'), Text(32, 0, 'WEEKDAY_APPR_PROCESS_START'), Text(33, 0, 'HOUR_APPR_PROCESS_START'), Text(34, 0, 'REG_REGION_NOT_LIVE_REGION'), Text(35, 0, 'REG_REGION_NOT_WORK_REGION'), Text(36, 0, 'LIVE_REGION_NOT_WORK_REGION'), Text(37, 0, 'REG_CITY_NOT_LIVE_CITY'), Text(38, 0, 'REG_CITY_NOT_WORK_CITY'), Text(39, 0, 'LIVE_CITY_NOT_WORK_CITY'), Text(40, 0, 'ORGANIZATION_TYPE'), Text(41, 0, 'EXT_SOURCE_1'), Text(42, 0, 'EXT_SOURCE_2'), Text(43, 0, 'EXT_SOURCE_3'), Text(44, 0, 'APARTMENTS_AVG'), Text(45, 0, 'BASEMENTAREA_AVG'), Text(46, 0, 'YEARS_BEGINEXPLUATATION_AVG'), Text(47, 0, 'YEARS_BUILD_AVG'), Text(48, 0, 'COMMONAREA_AVG'), Text(49, 0, 'ELEVATORS_AVG'), Text(50, 0, 'ENTRANCES_AVG'), Text(51, 0, 'FLOORSMAX_AVG'), Text(52, 0, 'FLOORSMIN_AVG'), Text(53, 0, 'LANDAREA_AVG'), Text(54, 0, 'LIVINGAPARTMENTS_AVG'), Text(55, 0, 'LIVINGAREA_AVG'), Text(56, 0, 'NONLIVINGAPARTMENTS_AVG'), Text(57, 0, 'NONLIVINGAREA_AVG'), Text(58, 0, 'APARTMENTS_MODE'), Text(59, 0, 'BASEMENTAREA_MODE'), Text(60, 0, 'YEARS_BEGINEXPLUATATION_MODE'), Text(61, 0, 'YEARS_BUILD_MODE'), Text(62, 0, 'COMMONAREA_MODE'), Text(63, 0, 'ELEVATORS_MODE'), Text(64, 0, 'ENTRANCES_MODE'), Text(65, 0, 'FLOORSMAX_MODE'), Text(66, 0, 'FLOORSMIN_MODE'), Text(67, 0, 'LANDAREA_MODE'), Text(68, 0, 'LIVINGAPARTMENTS_MODE'), Text(69, 0, 'LIVINGAREA_MODE'), Text(70, 0, 'NONLIVINGAPARTMENTS_MODE'), Text(71, 0, 'NONLIVINGAREA_MODE'), Text(72, 0, 'APARTMENTS_MEDI'), Text(73, 0, 'BASEMENTAREA_MEDI'), Text(74, 0, 'YEARS_BEGINEXPLUATATION_MEDI'), Text(75, 0, 'YEARS_BUILD_MEDI'), Text(76, 0, 'COMMONAREA_MEDI'), Text(77, 0, 'ELEVATORS_MEDI'), Text(78, 0, 'ENTRANCES_MEDI'), Text(79, 0, 'FLOORSMAX_MEDI'), Text(80, 0, 'FLOORSMIN_MEDI'), Text(81, 0, 'LANDAREA_MEDI'), Text(82, 0, 'LIVINGAPARTMENTS_MEDI'), Text(83, 0, 'LIVINGAREA_MEDI'), Text(84, 0, 'NONLIVINGAPARTMENTS_MEDI'), Text(85, 0, 'NONLIVINGAREA_MEDI'), Text(86, 0, 'FONDKAPREMONT_MODE'), Text(87, 0, 'HOUSETYPE_MODE'), Text(88, 0, 'TOTALAREA_MODE'), Text(89, 0, 'WALLSMATERIAL_MODE'), Text(90, 0, 'EMERGENCYSTATE_MODE'), Text(91, 0, 'OBS_30_CNT_SOCIAL_CIRCLE'), Text(92, 0, 'DEF_30_CNT_SOCIAL_CIRCLE'), Text(93, 0, 'OBS_60_CNT_SOCIAL_CIRCLE'), Text(94, 0, 'DEF_60_CNT_SOCIAL_CIRCLE'), Text(95, 0, 'DAYS_LAST_PHONE_CHANGE'), Text(96, 0, 'FLAG_DOCUMENT_2'), Text(97, 0, 'FLAG_DOCUMENT_3'), Text(98, 0, 'FLAG_DOCUMENT_4'), Text(99, 0, 'FLAG_DOCUMENT_5'), Text(100, 0, 'FLAG_DOCUMENT_6'), Text(101, 0, 'FLAG_DOCUMENT_7'), Text(102, 0, 'FLAG_DOCUMENT_8'), Text(103, 0, 'FLAG_DOCUMENT_9'), Text(104, 0, 'FLAG_DOCUMENT_10'), Text(105, 0, 'FLAG_DOCUMENT_11'), Text(106, 0, 'FLAG_DOCUMENT_12'), Text(107, 0, 'FLAG_DOCUMENT_13'), Text(108, 0, 'FLAG_DOCUMENT_14'), Text(109, 0, 'FLAG_DOCUMENT_15'), Text(110, 0, 'FLAG_DOCUMENT_16'), Text(111, 0, 'FLAG_DOCUMENT_17'), Text(112, 0, 'FLAG_DOCUMENT_18'), Text(113, 0, 'FLAG_DOCUMENT_19'), Text(114, 0, 'FLAG_DOCUMENT_20'), Text(115, 0, 'FLAG_DOCUMENT_21'), Text(116, 0, 'AMT_REQ_CREDIT_BUREAU_HOUR'), Text(117, 0, 'AMT_REQ_CREDIT_BUREAU_DAY'), Text(118, 0, 'AMT_REQ_CREDIT_BUREAU_WEEK'), Text(119, 0, 'AMT_REQ_CREDIT_BUREAU_MON'), Text(120, 0, 'AMT_REQ_CREDIT_BUREAU_QRT'), Text(121, 0, 'AMT_REQ_CREDIT_BUREAU_YEAR'), Text(122, 0, 'Unnamed: 122'), Text(123, 0, 'descrip')])
ax.axhline(40, ls='--',color='red')
<matplotlib.lines.Line2D object at 0x000001F0683AE5D0>
plt.title("Percentage of Missing values in application data")
Text(0.5, 1.0, 'Percentage of Missing values in application data')
plt.ylabel("Null Values PERCENTAGE")
Text(0, 0.5, 'Null Values PERCENTAGE')
plt.xlabel("COLUMNS")
Text(0.5, 0, 'COLUMNS')
plt.show()
nullcol_40_application = null_applicationDF[null_applicationDF["Null Values Percentage"]>=40]
nullcol_40_application
                      Column Name  Null Values Percentage
21                    OWN_CAR_AGE               65.990810
41                   EXT_SOURCE_1               56.381073
44                 APARTMENTS_AVG               50.749729
45               BASEMENTAREA_AVG               58.515956
46    YEARS_BEGINEXPLUATATION_AVG               48.781019
47                YEARS_BUILD_AVG               66.497784
48                 COMMONAREA_AVG               69.872297
49                  ELEVATORS_AVG               53.295980
50                  ENTRANCES_AVG               50.348768
51                  FLOORSMAX_AVG               49.760822
52                  FLOORSMIN_AVG               67.848630
53                   LANDAREA_AVG               59.376738
54           LIVINGAPARTMENTS_AVG               68.354953
55                 LIVINGAREA_AVG               50.193326
56        NONLIVINGAPARTMENTS_AVG               69.432963
57              NONLIVINGAREA_AVG               55.179164
58                APARTMENTS_MODE               50.749729
59              BASEMENTAREA_MODE               58.515956
60   YEARS_BEGINEXPLUATATION_MODE               48.781019
61               YEARS_BUILD_MODE               66.497784
62                COMMONAREA_MODE               69.872297
63                 ELEVATORS_MODE               53.295980
64                 ENTRANCES_MODE               50.348768
65                 FLOORSMAX_MODE               49.760822
66                 FLOORSMIN_MODE               67.848630
67                  LANDAREA_MODE               59.376738
68          LIVINGAPARTMENTS_MODE               68.354953
69                LIVINGAREA_MODE               50.193326
70       NONLIVINGAPARTMENTS_MODE               69.432963
71             NONLIVINGAREA_MODE               55.179164
72                APARTMENTS_MEDI               50.749729
73              BASEMENTAREA_MEDI               58.515956
74   YEARS_BEGINEXPLUATATION_MEDI               48.781019
75               YEARS_BUILD_MEDI               66.497784
76                COMMONAREA_MEDI               69.872297
77                 ELEVATORS_MEDI               53.295980
78                 ENTRANCES_MEDI               50.348768
79                 FLOORSMAX_MEDI               49.760822
80                 FLOORSMIN_MEDI               67.848630
81                  LANDAREA_MEDI               59.376738
82          LIVINGAPARTMENTS_MEDI               68.354953
83                LIVINGAREA_MEDI               50.193326
84       NONLIVINGAPARTMENTS_MEDI               69.432963
85             NONLIVINGAREA_MEDI               55.179164
86             FONDKAPREMONT_MODE               68.386172
87                 HOUSETYPE_MODE               50.176091
88                 TOTALAREA_MODE               48.268517
89             WALLSMATERIAL_MODE               50.840783
90            EMERGENCYSTATE_MODE               47.398304
122                  Unnamed: 122              100.000000
123                       descrip              100.000000
len(nullcol_40_application)
51
mn.matrix(previousDF)
<Axes: >
plt.show()
round(previousDF.isnull().sum()/previousDF.shape[0]*100.00,2)
SK_ID_PREV                      0.00
SK_ID_CURR                      0.00
NAME_CONTRACT_TYPE              0.00
AMT_ANNUITY                    22.22
AMT_APPLICATION                 0.00
AMT_CREDIT                      0.00
AMT_DOWN_PAYMENT               53.35
AMT_GOODS_PRICE                22.98
WEEKDAY_APPR_PROCESS_START      0.00
HOUR_APPR_PROCESS_START         0.00
FLAG_LAST_APPL_PER_CONTRACT     0.00
NFLAG_LAST_APPL_IN_DAY          0.00
RATE_DOWN_PAYMENT              53.35
RATE_INTEREST_PRIMARY          99.65
RATE_INTEREST_PRIVILEGED       99.65
NAME_CASH_LOAN_PURPOSE          0.00
NAME_CONTRACT_STATUS            0.00
DAYS_DECISION                   0.00
NAME_PAYMENT_TYPE               0.00
CODE_REJECT_REASON              0.00
NAME_TYPE_SUITE                49.13
NAME_CLIENT_TYPE                0.00
NAME_GOODS_CATEGORY             0.00
NAME_PORTFOLIO                  0.00
NAME_PRODUCT_TYPE               0.00
CHANNEL_TYPE                    0.00
SELLERPLACE_AREA                0.00
NAME_SELLER_INDUSTRY            0.00
CNT_PAYMENT                    22.22
NAME_YIELD_GROUP                0.00
PRODUCT_COMBINATION             0.02
DAYS_FIRST_DRAWING             40.12
DAYS_FIRST_DUE                 40.12
DAYS_LAST_DUE_1ST_VERSION      40.12
DAYS_LAST_DUE                  40.12
DAYS_TERMINATION               40.12
NFLAG_INSURED_ON_APPROVAL      40.12
dtype: float64
null_previousDF = pd.DataFrame((previousDF.isnull().sum())*100/previousDF.shape[0]).reset_index()
null_previousDF.columns = ['Column Name', 'Null Values Percentage']
fig = plt.figure(figsize=(18,6))
ax = sns.pointplot(x="Column Name",y="Null Values Percentage",data=null_previousDF,color ='blue')
plt.xticks(rotation =90,fontsize =7)
([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36], [Text(0, 0, 'SK_ID_PREV'), Text(1, 0, 'SK_ID_CURR'), Text(2, 0, 'NAME_CONTRACT_TYPE'), Text(3, 0, 'AMT_ANNUITY'), Text(4, 0, 'AMT_APPLICATION'), Text(5, 0, 'AMT_CREDIT'), Text(6, 0, 'AMT_DOWN_PAYMENT'), Text(7, 0, 'AMT_GOODS_PRICE'), Text(8, 0, 'WEEKDAY_APPR_PROCESS_START'), Text(9, 0, 'HOUR_APPR_PROCESS_START'), Text(10, 0, 'FLAG_LAST_APPL_PER_CONTRACT'), Text(11, 0, 'NFLAG_LAST_APPL_IN_DAY'), Text(12, 0, 'RATE_DOWN_PAYMENT'), Text(13, 0, 'RATE_INTEREST_PRIMARY'), Text(14, 0, 'RATE_INTEREST_PRIVILEGED'), Text(15, 0, 'NAME_CASH_LOAN_PURPOSE'), Text(16, 0, 'NAME_CONTRACT_STATUS'), Text(17, 0, 'DAYS_DECISION'), Text(18, 0, 'NAME_PAYMENT_TYPE'), Text(19, 0, 'CODE_REJECT_REASON'), Text(20, 0, 'NAME_TYPE_SUITE'), Text(21, 0, 'NAME_CLIENT_TYPE'), Text(22, 0, 'NAME_GOODS_CATEGORY'), Text(23, 0, 'NAME_PORTFOLIO'), Text(24, 0, 'NAME_PRODUCT_TYPE'), Text(25, 0, 'CHANNEL_TYPE'), Text(26, 0, 'SELLERPLACE_AREA'), Text(27, 0, 'NAME_SELLER_INDUSTRY'), Text(28, 0, 'CNT_PAYMENT'), Text(29, 0, 'NAME_YIELD_GROUP'), Text(30, 0, 'PRODUCT_COMBINATION'), Text(31, 0, 'DAYS_FIRST_DRAWING'), Text(32, 0, 'DAYS_FIRST_DUE'), Text(33, 0, 'DAYS_LAST_DUE_1ST_VERSION'), Text(34, 0, 'DAYS_LAST_DUE'), Text(35, 0, 'DAYS_TERMINATION'), Text(36, 0, 'NFLAG_INSURED_ON_APPROVAL')])
ax.axhline(40, ls='--',color='red')
<matplotlib.lines.Line2D object at 0x000001F053BC0190>
plt.title("Percentage of Missing values in previousDF data")
Text(0.5, 1.0, 'Percentage of Missing values in previousDF data')
plt.ylabel("Null Values PERCENTAGE")
Text(0, 0.5, 'Null Values PERCENTAGE')
plt.xlabel("COLUMNS")
Text(0.5, 0, 'COLUMNS')
plt.show()
nullcol_40_previous = null_previousDF[null_previousDF["Null Values Percentage"]>=40]
nullcol_40_previous
                  Column Name  Null Values Percentage
6            AMT_DOWN_PAYMENT               53.348211
12          RATE_DOWN_PAYMENT               53.348211
13      RATE_INTEREST_PRIMARY               99.645137
14   RATE_INTEREST_PRIVILEGED               99.645137
20            NAME_TYPE_SUITE               49.127626
31         DAYS_FIRST_DRAWING               40.121880
32             DAYS_FIRST_DUE               40.121880
33  DAYS_LAST_DUE_1ST_VERSION               40.121880
34              DAYS_LAST_DUE               40.121880
35           DAYS_TERMINATION               40.121880
36  NFLAG_INSURED_ON_APPROVAL               40.121880
len(nullcol_40_previous)
11
Source = applicationDF[["EXT_SOURCE_1","EXT_SOURCE_2","EXT_SOURCE_3","TARGET"]]
source_corr = Source.corr()
ax = sns.heatmap(source_corr,
            xticklabels=source_corr.columns,
            yticklabels=source_corr.columns,
            annot = True,
            cmap ="RdYlGn")
plt.show()
