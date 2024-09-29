def loginUsuario(perfil):
    if perfil.lower() == 'admin':
        print('Bem-vindo, Administrador.')
    else:
        print('Bem-vindo, Usuário.')

loginUsuario('Admin')  # Exemplo 1
loginUsuario('admin')  # Exemplo 2
loginUsuario('User')   # Exemplo 3
loginUsuario('usuário') # Exemplo 4
