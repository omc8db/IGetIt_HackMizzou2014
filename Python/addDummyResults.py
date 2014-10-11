import dbClient

db = dbClient.db_Connect(3)

db.sendEvents([0,8.5,3000,"Jerry"]);
db.sendEvents([1,9,3000,"Owen"]);
db.sendEvents([2,8.75,3000,"Alec"]);