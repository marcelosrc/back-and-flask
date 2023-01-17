from flask import Blueprint, request
from config.db import connection, cursor

posts_bp = Blueprint("posts", __name__, url_prefix="/posts")


@posts_bp.route("/", methods=['GET'])
def read_all():
    sql = "SELECT * FROM posts;"
    cursor.execute(sql)
    posts = cursor.fetchall()
    return posts


@posts_bp.route("/create", methods=["POST"])
def create():
    body = request.json
    parentid = body.get("parentid")
    content = body.get("content")
    sql = "INSERT INTO posts(parentid, content) VALUES(%s, %s)"
    register = (parentid, content)
    try:
        cursor.execute(sql, register)
        connection.commit()
        return {"message": "Publicação criada com sucesso"}, 201
    except:
        return {"message": "Erro ao criar publicação"}, 400


@posts_bp.route("delete/<id>", methods=["DELETE"])
def delete(id):
    sql = "DELETE FROM posts WHERE id = %s"
    try:
        cursor.execute(sql, (id,))
        connection.commit()
        return {"message": "Publicação removida com sucesso"}, 200
    except:
        return {"message": "Erro ao remover publicação"}, 400


@posts_bp.route("update/<id>", methods=["PUT"])
def update(id):
    body = request.json
    content = body.get("content")
    sql = "UPDATE posts SET content = %s WHERE id = %s"
    try:
        cursor.execute(sql, (content, id))
        connection.commit()
        return {"message": "Publicação atualizada com sucesso"}, 200
    except:
        connection.close()
        cursor.close()
        return {"message": "Falha ao atualizar publicação"}, 400
