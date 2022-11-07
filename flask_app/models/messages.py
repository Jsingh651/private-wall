from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash
from flask_app import app
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
from flask_app.models import users
from datetime import datetime
import math


class Message:
    def __init__(self,data):
        self.id = data['id']
        self.content = data['content']
        self.sender_id = data['sender_id']
        self.reciver_id = data['reciver_id']
        self.created_at = data['created_at']
        self.updated_at  = data['updated_at']
        self.reciver = None
        self.sender = None

    def time_span(self):
        now = datetime.now()
        delta = now - self.created_at
        print(delta.days)



    @classmethod
    def create_message(cls,data):
        query = '''
        INSERT INTO messages (content, sender_id, reciver_id)
        VALUES (%(content)s,%(sender_id)s,%(reciver_id)s)
        '''
        return connectToMySQL('coding_dojo_wall').query_db(query,data)


    @classmethod
    def delete_message(cls,data):
        query = 'DELETE FROM messages WHERE id = %(id)s'
        return connectToMySQL('coding_dojo_wall').query_db(query,data)


    @classmethod
    def get_messages_with_user(cls):
        query = '''
            SELECT * FROM messages LEFT JOIN users 
            AS sender ON messages.sender_id = sender.id
            LEFT JOIN users AS reciver ON messages.reciver_id = reciver.id;
                '''
        results = connectToMySQL('coding_dojo_wall').query_db(query)
        print("RESULTS", results)
        messages = []
        for data in results:
            # one_message = cls(message_info)
            sender_info = {
                'id': data['sender.id'],
                'first_name':data['first_name'],
                'last_name': data['last_name'],
                'email': data['email'],
                'password': data['password'],
                'created_at': data['sender.created_at'],
                'updated_at': data['sender.updated_at']
            }
            reciver_info = {
                'id': data['reciver.id'],
                'first_name': data['reciver.first_name'],
                'last_name': data['reciver.last_name'],
                'email': data['reciver.email'],
                'password': data['reciver.password'],
                'created_at': data['reciver.created_at'],
                'updated_at': data['reciver.updated_at']
            }
            message_info = {
                'id': data['id'],
                'content': data['content'],
                'created_at': data['created_at'],
                'updated_at': data['updated_at'],
                'sender_id': data['sender_id'],
                'reciver_id': data['reciver_id']
            }
            one_message = cls(message_info)
            one_message.sender = users.User(sender_info)
            one_message.reciver = users.User(reciver_info)
            messages.append(one_message)
        return messages

    @classmethod
    def message_length(cls, data):
        query = '''
        SELECT * FROM messages JOIN 
        users AS sender ON messages.sender_id
        = sender.id JOIN users AS reciver ON messages.reciver_id 
        = reciver.id WHERE sender.id = %(id)s;
            '''
        results = connectToMySQL('coding_dojo_wall').query_db(query,data)
        print("RESULTS", results)
        messages = []
        for data in results:
            # one_message = cls(message_info)
            sender_info = {
                'id': data['sender.id'],
                'first_name':data['first_name'],
                'last_name': data['last_name'],
                'email': data['email'],
                'password': data['password'],
                'created_at': data['sender.created_at'],
                'updated_at': data['sender.updated_at']
            }
            reciver_info = {
                'id': data['reciver.id'],
                'first_name': data['reciver.first_name'],
                'last_name': data['reciver.last_name'],
                'email': data['reciver.email'],
                'password': data['reciver.password'],
                'created_at': data['reciver.created_at'],
                'updated_at': data['reciver.updated_at']
            }
            message_info = {
                'id': data['id'],
                'content': data['content'],
                'created_at': data['created_at'],
                'updated_at': data['updated_at'],
                'sender_id': data['sender_id'],
                'reciver_id': data['reciver_id']
            }
            one_message = cls(message_info)
            one_message.sender = users.User(sender_info)
            one_message.reciver = users.User(reciver_info)
            messages.append(one_message)
        return messages

    @classmethod
    def message_length_rec(cls, data):
        query = '''
        SELECT * FROM messages JOIN 
        users AS sender ON messages.sender_id
        = sender.id JOIN users AS reciver ON messages.reciver_id 
        = reciver.id WHERE reciver.id = %(id)s;
            '''
        results = connectToMySQL('coding_dojo_wall').query_db(query,data)
        print("RESULTS", results)
        messages = []
        for data in results:
            # one_message = cls(message_info)
            sender_info = {
                'id': data['sender.id'],
                'first_name':data['first_name'],
                'last_name': data['last_name'],
                'email': data['email'],
                'password': data['password'],
                'created_at': data['sender.created_at'],
                'updated_at': data['sender.updated_at']
            }
            reciver_info = {
                'id': data['reciver.id'],
                'first_name': data['reciver.first_name'],
                'last_name': data['reciver.last_name'],
                'email': data['reciver.email'],
                'password': data['reciver.password'],
                'created_at': data['reciver.created_at'],
                'updated_at': data['reciver.updated_at']
            }
            message_info = {
                'id': data['id'],
                'content': data['content'],
                'created_at': data['created_at'],
                'updated_at': data['updated_at'],
                'sender_id': data['sender_id'],
                'reciver_id': data['reciver_id']
            }
            one_message = cls(message_info)
            one_message.sender = users.User(sender_info)
            one_message.reciver = users.User(reciver_info)
            messages.append(one_message)
        return messages

