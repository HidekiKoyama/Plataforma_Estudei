from rolepermissions.roles import AbstractUserRole

class Professor(AbstractUserRole):
     available_permissions = {'cria_usuarios': True, 'ver_saldo': True}

class Aluno(AbstractUserRole):
     available_permissions = {'cria_usuarios': False, 'ver_saldo': True}