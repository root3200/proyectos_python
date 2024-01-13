import gitlab

token = "glpat-daYggcmvKYwaKzTvK29q"
#Conexion a gitlab
gl = gitlab.Gitlab('https://gitlab.com', private_token=token)

# Obtener datos del proyecto.
project_id = '44845711'
project = gl.projects.get(project_id)

print(project)

