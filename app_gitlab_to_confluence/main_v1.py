from gitlab import Gitlab
from markdown2 import Markdown
from atlassian import Confluence
import json

CONFIG_FILE = "config.json"

def conexion():

    #CARGAR DATOS USERNAME, URL, PASSWORD
    with open(CONFIG_FILE, "r") as file:
        data = json.load(file)
    
    #CONEXION GITLAB
    gl = Gitlab(url=data[0]['gitlab']['url'],
                private_token=data[0]['gitlab']['private_token'])
    
    #CONEXION CONFLUENCE
    confluence = Confluence(data[1]['confluence']['url'],
                            data[1]['confluence']['usernames'], 
                            data[1]['confluence']['private_token'])

    return gl, confluence
    
def gitlab_respo():

    conexion_gitlab, _ = conexion()
    
    #CONTENIDO README
    proyecto_id = "45094327"
    project = conexion_gitlab.projects.get(proyecto_id)
    commit = project.commits.list(get_all=False)[0]
    tree = project.repository_tree()
    
    #CONVERTIR HTTP A MARKDOWN
    n1 = project.files.get(file_path=tree[1]['path'], 
                           ref=commit.id).decode()
    
    owner = Markdown(extras=['tables', 'strike'])

    data = (
            f"---\n### Ultima modificacion\n"
            f"**ID**: *{commit.id}*\n"
            f"**Mail**: *{commit.committer_email}*\n"
            f"**Mensaje**: *{commit.title}*\n"
            f"**Autor**: *{commit.author_name}*\n"
            f"**Date**: **{commit.created_at}**\n"
            "---"
            ).replace(".000+00:00", "")
    
    html_2 = f"{owner.convert(n1)}\n{owner.convert(data)}"

    return html_2

def confluence_page():

    _ , conexion_confluence = conexion()
    contenido_md = gitlab_respo()
    page_id = "327694"
    
    #ACTUALIZAR CONTENIDO
    n2 = conexion_confluence.update_page(page_id, 
    title='test_api',
    version_comment='nueva_tabla', 
    body=contenido_md, 
    representation='storage')

confluence_page()