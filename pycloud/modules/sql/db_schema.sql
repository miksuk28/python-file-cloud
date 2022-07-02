
CREATE TABLE IF NOT EXISTS "users" (
	"id"	INTEGER,
	"username"	TEXT(30) NOT NULL UNIQUE,
	"fname"  TEXT(40),
	"lname"  TEXT(40),
	"disabled"  BOOLEAN NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "passwords" (
	"user_id"	INTEGER NOT NULL UNIQUE,
	"hashed"	TEXT NOT NULL,
	"salt"	TEXT NOT NULL,
	FOREIGN KEY("user_id") REFERENCES "users"("id")
);
CREATE TABLE IF NOT EXISTS "user_attrs" (
	"id"	INTEGER,
	"name"	TEXT NOT NULL UNIQUE,
	"type"	TEXT NOT NULL,
	"description"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "user_attrs_junctions" (
	"user_id"	INTEGER NOT NULL,
	"attr_id"	INTEGER NOT NULL,
	"VALUE"	TEXT,
	UNIQUE("user_id","attr_id"),
	FOREIGN KEY("user_id") REFERENCES "users"("id"),
	FOREIGN KEY("attr_id") REFERENCES "user_attrs"("id")
);
CREATE TABLE IF NOT EXISTS "sessions" (
	"created"	DATETIME DEFAULT CURRENT_TIMESTAMP,
	"user_id"	INTEGER NOT NULL,
	"token"	TEXT NOT NULL UNIQUE,
	"expires"	DATETIME NOT NULL,
	FOREIGN KEY("user_id") REFERENCES "users"("id")
);
CREATE TABLE IF NOT EXISTS "files" (
	"id"	INTEGER,
	"filename"	TEXT NOT NULL,
	"user_id"	INTEGER NOT NULL,
	"path"	TEXT NOT NULL,
	UNIQUE("user_id","path","filename"),
	FOREIGN KEY("user_id") REFERENCES "users"("id"),
	PRIMARY KEY("id" AUTOINCREMENT)
);
