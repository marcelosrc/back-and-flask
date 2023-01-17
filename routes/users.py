from flask import Blueprint, request
from config.db import connection, cursor
import bcrypt

users_bp = Blueprint(name="users", import_name=__name__, url_prefix="/users")


def _hash_password(password):
    byte_password = password.encode("utf-8")
    return bcrypt.hashpw(byte_password, bcrypt.gensalt())


@users_bp.route("/")
def read_all():
    sql = "SELECT * FROM users;"
    cursor.execute(sql)
    users = cursor.fetchall()
    return users


@users_bp.route("/create", methods=["POST"])
def create():
    body = request.json
    email = body.get("email")
    password = body.get("password")
    name = body.get("name")
    surname = body.get("surname")
    dob = body.get("dob")
    profilepicpath = body.get("profilepicpath")
    sql = "INSERT INTO users(email, password, name, surname, dob, profilepicpath) VALUES(%s, %s, %s, %s, %s, %s)"
    try:
        register = (email, _hash_password(password),
                    name, surname, dob, profilepicpath)
        cursor.execute(sql, register)
        connection.commit()
        return {"message": "Usuário " + email + " criado com sucesso"}, 201
    except:
        return {"message": "Falha ao criar usuário"}, 400


@users_bp.route("delete/<id>", methods=["DELETE"])
def delete(id):
    sql = "DELETE FROM users WHERE id = %s"
    try:
        cursor.execute(sql, (id,))
        connection.commit()
        return {"message": "Usuário removido com sucesso"}, 200
    except:
        return {"message": "Falha ao remover usuário"}, 400
