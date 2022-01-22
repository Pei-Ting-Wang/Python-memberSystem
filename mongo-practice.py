import pymongo
from bson.objectid import ObjectId
#連線到MongoDb雲端資料庫
client = pymongo.MongoClient("mongodb+srv://root:root123@mycluster.yufcy.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test #選擇操作<<test>>資料庫
#把資料放進資料庫中
collection=db.users #選擇操作users集合
#把資料新增到集合中

# 1. 新增單筆資料
# result=collection.insert_one({
#     "name":"penny",
#     "gender":"女"
# })
#新增多筆資料
# result=collection.insert_many([{
#     "name":"Amy",
#     "gender":"女",
   
# },{
#     "name":"Betty",
#     "gender":"男"
# },{
#     "name":"Jason",
#     "gender":"男"
# },{
#     "name":"Ted",
#     "gender":"男"
# }])
# print(result.inserted_id)
# print(result.inserted_ids)

# 2. 查詢資料
#單筆
#第一筆資料取得
# data=collection.find_one()
# print(data)
#特定某筆id資料
# data=collection.find_one(ObjectId("61ea425ff05ab357a54cc1bf"))
# print(data["name"])
#取得所有資料
# cusor=collection.find()
# print(cusor)
# for data in cusor:
#     print(data)

# 3. 更新資料
#更新集合的一筆資料
# result=collection.update_one({
#     "name":"penny"
# },{
#     # $set 更新/覆蓋
#     # $unset 刪除此欄位
#     # $mul 除法 / $inc 加號
#     "$set":{
#         "gender":"男"
#     }
# })
#更新集合的多筆資料
# result=collection.update_many({
#     "name":"penny"
# },{
#     # $set 更新/覆蓋
#     # $unset 刪除此欄位
#     # $mul 除法 / $inc 加號
#     "$set":{
#         "gender":"女"
#     }
# })
# print(result.matched_count)
# print(result.modified_count)

# 3. 刪除資料
#刪除一筆資料
# result= collection.delete_one({"name":"ddd"})
#刪除多筆資料
# result= collection.delete_many({"name":"alex"})
#刪除多筆資料
#取得刪除結果
# print(result.deleted_count)

# 4. 複合篩選條件
# result=collection.find_one({
#     # "$or"
#     "$and":[
#         { "name":"Jason"},
#         {"gender":"男"}
#     ]
# })
result=collection.find(
    sort=[("name",pymongo.ASCENDING)])
for data in result:
    print(data)