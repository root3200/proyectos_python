import json
from gitlab import Gitlab
from markdown2 import Markdown
from atlassian import Confluence

CONFIG_FILE = "config.json"

def conexion_api():

    #CARGAR DATOS USERNAME, URL, PASSWORD
    with open(CONFIG_FILE, "r") as file:
        data = json.load(file)

    gl = Gitlab(url=data[0]['gitlab']['url'],
                private_token=data[0]['gitlab']['private_token'])
    
    proyecto_id = "45094327"
    #return gl, proyecto_id
    
    project = gl.projects.get(proyecto_id)
    commit = project.commits.list(get_all=False)[0]
    tree = project.repository_tree()

    print(tree[1].keys())
    n1 = project.files.get(file_path=tree[1]['path'], ref=commit.id).decode()
    owner = Markdown(extras=['tables', 'strike'])
    #html = owner.convert(n1)
    #n6 = base64.b64decode(n5).decode('html')  
    data_2 = f"---\n### Ultima modificacion\n**ID**: *{commit.id}* \n**Mail**: *{commit.committer_email}* \n**Mensaje**: *{commit.title}* \n**Autor**: *{commit.author_name}* \n**Date**: **{commit.created_at}** \n ---".replace(".000+00:00", "")
    html_2 = f"{owner.convert(n1)}\n{owner.convert(data_2)}"
    
    print(data_2)
    return data, html_2
    """
    author_name
    created_at
    author_name
    committed_date
    """
    # for file in tree:
    #     if file['name'].lower() == "readme.md":
    #         file_content = project.files.get(file['path'], ref=commit.id).decode()

    # print(file_content)

def test_confluence():
    
    data, html_2 = conexion_api()
    # url = data[1]['confluence']['url']
    # username = data[1]['confluence']['usernames']
    # token = data[1]['confluence']['private_token']
    
    conexion = Confluence(data[1]['confluence']['url'],
                          data[1]['confluence']['usernames'], 
                          data[1]['confluence']['private_token'])
    n_sapace = '~6341ceb4b2e3c5ad0fa7cad6'
    n1 = conexion.get_all_spaces()

    print(n1.keys())
    
    test = " "

    

    n2 = conexion.update_page(page_id='327694', title='test_api',version_comment='test', body=html_2, representation='storage')
    #n2 = conexion.get_page_by_title(space=n_sapace, title='test_api', start=None, limit=None)
    # if conexion.page_exists(space=n_sapace, title='test_api3', type=None) == True:
    #     print("la pagina existe")
    # else:
    #     print("la pagina no existe\nCreando pagina nueva....")
    #     conexion.create_page(space=n_sapace, title='test_api3', body=html_, parent_id=None, type='page', representation='storage', editor='v2', full_width=False)
    #conexion.remove_page(page_id='1015810', status=None, recursive=None)
    
test_confluence()