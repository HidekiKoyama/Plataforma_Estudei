from django.db import models


class categorie_course(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(max_length=150)
    delete = models.BooleanField(default=True, blank=False)

    def __str__(self):
        return self.name


class courses(models.Model):
    user_log = models.ForeignKey("auth.user", blank=True, null=True, on_delete=models.SET_NULL, default="")
    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=155)
    categorie_course = models.IntegerField(null=False, blank=True, default="")
    delete = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.name

'''
CREATE SEQUENCE SEQ_SYSTEM_FRIENDS;

CREATE TABLE SYSTEM_FRIENDS (
	ID INTEGER DEFAULT (NEXTVAL('SEQ_SYSTEM_FRIENDS')),
	F1 INTEGER,
	F2 INTEGER,
	
	CONSTRAINT PK_SYS_FRIEND PRIMARY KEY (ID),
	
	CONSTRAINT FK_SYS_FRIEND1 FOREIGN KEY (F1)
		REFERENCES AUTH_USER (ID),

	CONSTRAINT FK_SYS_FRIEND2 FOREIGN KEY (F2)
		REFERENCES AUTH_USER (ID)
)
'''