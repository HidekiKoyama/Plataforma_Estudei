from rolepermissions.roles import AbstractUserRole

class teacher(AbstractUserRole):
     available_permissions = {'post_curse': True}

class student(AbstractUserRole):
     available_permissions = {'feedbak_curse': True}