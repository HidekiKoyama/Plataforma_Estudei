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
        script = f"SELECT name, description, id FROM sistema_categorie_curses WHERE ID = {id}"
        return script

    def insertCourses(self, name, description):
        script = f"INSERT INTO sistema_categorie_curses (name, description, delete) VALUES ('{name}', '{description}', 'True')"
        return script

    def requestUser(self):
        script = "SELECT * FROM auth_user WHERE ID <> 1 ORDER BY ID"
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
