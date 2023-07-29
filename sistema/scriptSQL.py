class RequestSQL():

    def updateCourses(self, name, description, id):
        script = f"UPDATE sistema_categorie_curses SET name = '{name}', description = '{description}' WHERE id = {id};"
        return script

    def requestCourses(self):
        script = "SELECT name, description, id FROM sistema_categorie_course"
        return script

    def dellCourses(self, id):
        script = f"DELETE FROM sistema_categorie_curses WHERE ID = {id}"
        return script

    def filterCourses(self, id):
        script = f"SELECT name, description, id FROM sistema_categorie_course WHERE ID = {id}"
        return script

    def insertCourses(self, name, description):
        script = f"INSERT INTO sistema_categorie_curses (name, description, delete) VALUES ('{name}', '{description}', 'True')"
        return script

    def requestUser(self):
        script = "SELECT * FROM auth_user WHERE ID <> 1 AND is_superuser = 'False' ORDER BY ID"
        return script

    def rankCourses(self):
        script = ("SELECT main.name, main.description, SCC.name, main.id FROM sistema_courses main " +
                    "JOIN(SELECT name, id FROM sistema_categorie_course) SCC ON SCC.id = main.categorie_course")
        return script

    def insertCourses(self, name, description, categorie, user):
        script = ("INSERT INTO SISTEMA_COURSES (NAME, DESCRIPTION, CATEGORIE_COURSE, USER_LOG_ID, DELETE) " +
                    f"VALUES ('{name}', '{description}', {categorie}, (SELECT ID FROM AUTH_USER WHERE USERNAME = '{user}'), false)")
        return script
    
    def requestCategorieCourses(self):
        script = "SELECT * FROM SISTEMA_CATEGORIE_COURSE WHERE DELETE <> False"
        return script
    
    def upadateBlockUser(self, id):
        script = f"UPDATE AUTH_USER SET is_active = False WHERE ID = {id}"
        return script
    
    def upadateUnblockUser(self, id):
        script = f"UPDATE AUTH_USER SET is_active = True WHERE ID = {id}"
        return script
    
    def addFriend(self, id1, id2):
        script = f"INSERT INTO SYSTEM_FRIENDS (F1, F2) VALUES ({id1}, {id2})"
        return script
    
    def isFriend(self, id):
        script = ("SELECT "+
	   "SYS.ID, " +
        "SYS.USERNAME, " +
        "CASE " +
            f"WHEN (SYS.ID IN (SELECT F2 FROM SYSTEM_FRIENDS WHERE (F1 = {id}) OR SYS.ID IN (SELECT F1 FROM SYSTEM_FRIENDS WHERE (F2 = {id})))) THEN True " +
            "ELSE False " +
            "END SITUAMIGO "+
            "FROM auth_user AS SYS "+
                f"WHERE SYS.is_superuser = 'False' AND SYS.ID <> {id};")
        return script