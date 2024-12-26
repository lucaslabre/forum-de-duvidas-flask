from forumdeduvidas import app
from forumdeduvidas.models import Usuario
from forumdeduvidas import database

# with app.app_context():
#     database.create_all()

# with app.app_context():
#     usuario = Usuario(username='Fulano', senha='123', email='fulano@gmail.com')
#     usuario2 = Usuario(username='Ciclano', senha='teste2', email='ciclano@gmail.com')
#     usuario3 = Usuario(username='Beltrano', senha='teste3', email='beltrano@gmail.com')
#     database.session.add(usuario)
#     database.session.add(usuario2)
#     database.session.add(usuario3)
#     database.session.commit()

# with app.app_context():
#     meus_usuarios = Usuario.query.all()
#     primeiro_usuario = Usuario.query.first()
#     print(meus_usuarios)
#     print(primeiro_usuario)

# with app.app_context():
#     usuario_teste = Usuario.query.filter_by(username='Beltrano').first()
#     print(usuario_teste)
#     print(usuario_teste.email)

# with app.app_context():
#     meu_post = Post(titulo='Primeiro Post Teste', id_usuario=1, corpo='Esse é meu primeiro post!')
#     database.session.add(meu_post)
#     database.session.commit()

# with app.app_context():
#     post = Post.query.first()
#     print(post)
#     print(post.titulo)
#     print(post.autor)
#     print(post.autor.email)

with app.app_context():
    database.drop_all()
    database.create_all()

# with app.app_context():
#     usuario = Usuario.query.all()
#     print(usuario)