from datetime import datetime

import numpy as np
import pandas as pd
import json
import pymysql
from pandas import json_normalize

start_time = datetime.now();
from Tools.scripts.dutree import display

# sql insert tutorial
# https://www.dataquest.io/blog/sql-insert-tutorial/
# ----------------------------------------------
# (1) database introduce area
# make connection to database
connection = pymysql.connect(host='hanaglitched.xyz',
                             port=3306,
                             user='admin',
                             password='#Rdunet690801',
                             db='hanaglitched',
                             charset='utf8')
# create cursor
cursor = connection.cursor()
# -----------------------------------------------

# -----------------------------------------------
# (2) dataframe introduce area
# open json file
with open('D:/my projects/jsonintodb2/venv/data/json/AllPrintings.json', 'r', encoding='utf-8') as file:
    getImport = json.load(file)
dict_get = getImport.get("data")
# get original dataframe
df = pd.DataFrame(dict_get)
# rotate it so you could get set name
_df = df.transpose().get("cards")
df = df.transpose()
# update MAGICNOTIFY_SET_INFO first
# for i in range(0, len(_df.index)):
#     print(i)
#     val_set = ""
#     setCode = _df.index[i]
#     releaseDate = df.iloc[i]["releaseDate"]
#     setName = df.iloc[i]["name"]
#     val_set += "(\"" + setCode + "\",\"" + setName + "\",\"" + releaseDate + "\")"
#     sql_set = "INSERT INTO MagicnotifySetInfo (`set`, `setName`, `reldate`) VALUES " + val_set + ";"
#     cursor.execute(sql_set)
# connection.commit()
# for i in range(0, len(_df.index)):
#     # set initial query as empty
#     val_ = ""
#     # to get set name, use df.index[i], since row name represents set name
#     print(i)
#     # now df is made of dictionaries, make it dataframe again
#     temp = _df[i]
#     temp = pd.DataFrame(temp)
#     # make nan as none to get in inserted in database
#     temp = temp.replace({np.nan: None})
#     # check if "name" exist; if it doesn't exist don't run it
#     uuid = ""
#     if "name" in temp.transpose().index:
#         # set foreignData as foreignData only
#         foreignData = temp["foreignData"]
#         # since len(foreignData.index) and len(temp.index) is same, we could set it same
#         for j in range(0, len(foreignData.index)):
#             uuid = temp.iloc[j]["uuid"]
#             if uuid == None:
#                 uuid = ""
#             val_ += "(\"" + uuid + "\")"
#             if j < len(foreignData.index) - 1:
#                 val_ += ","
#     if val_ != "":
#         sql_ = "INSERT INTO MagicnotifyUuidName (`key`) VALUES " + val_ + ";"
#         cursor.execute(sql_)
# connection.commit()
# now update MAGICNOTIFY_CARD_INFO
print(len(_df.index))
for i in range(0, len(_df.index)):
    # set initial query as empty
    val_ = ""
    val = ""
    # to get set name, use df.index[i], since row name represents set name
    print(i)
    setCode = _df.index[i]
    releaseDate = df.iloc[i]["releaseDate"]
    setName = df.iloc[i]["name"]
    # now df is made of dictionaries, make it dataframe again
    temp = _df[i]
    temp = pd.DataFrame(temp)
    # make nan as none to get in inserted in database
    temp = temp.replace({np.nan: None})
    # check if "name" exist; if it doesn't exist don't run it
    cardkingdom = ""
    cardkingdomfoil = ""
    name = ""
    uuid = ""
    rarity = ""
    koname = ""
    if "name" in temp.transpose().index:
        # set foreignData as foreignData only
        foreignData = temp["foreignData"]
        purchaseUrls = temp["purchaseUrls"]
        # since len(foreignData.index) and len(temp.index) is same, we could set it same
        for j in range(0, len(foreignData.index)):
            # __temp is dictionary now
            __temp = purchaseUrls[j]
            # get a value from python dictionary
            if 'cardKingdom' in __temp:
                cardkingdom = __temp['cardKingdom']
            if 'cardKingdomFoil' in __temp:
                cardkingdomfoil = __temp['cardKingdomFoil']
            name = temp.iloc[j]["name"]
            # print(name)
            uuid = temp.iloc[j]["uuid"]
            # print(uuid)
            rarity = temp.iloc[j]["rarity"]
            # print(rarity)
            _temp = foreignData[j]
            _temp = pd.DataFrame(_temp)
            # if there is no koname, we cant set it null so set it empty
            koname = ""
            if "language" in _temp.transpose().index:
                for k in range(0, len(_temp.index)):
                    if _temp.iloc[k]["language"] == "Korean":
                        koname = _temp.iloc[k]["name"]
                        # print(koname)
                        break
            if cardkingdom == None:
                cardkingdom = ""
            if cardkingdomfoil == None:
                cardkingdomfoil = ""
            if name == None:
                name = ""
            if uuid == None:
                uuid = ""
            if rarity == None:
                rarity = ""
            if koname == None:
                koname = ""
            # in case data includes double quote
            koname = koname.replace("\"", "\\\"")
            name = name.replace("\"", "\\\"")
            val += "(\"" + koname + "\",\"" + name + "\",\"" + cardkingdom + "\",\"" + cardkingdomfoil + "\",\"" + setCode + "\",\"" + setName + "\",\"" + releaseDate + "\",\"" + rarity + "\",\"" + uuid + "\")"
            if j < len(foreignData.index) - 1:
                val += ",\n"
    if val != "":
        # https://chartio.com/learn/sql-tips/single-double-quote-and-backticks-in-mysql-queries/
        sql = "INSERT INTO MagicnotifyCardInfo (`koname`, `name`, `cardkingdom`, `cardkingdomfoil`, `set`, `setName`, `relDate`, `rarity`, `uuid`) VALUES " + val + ";"
        cursor.execute(sql)
connection.commit()


# get elapsed time (for test)
end_time = datetime.now()
elapsed_time = end_time - start_time
print(elapsed_time)
