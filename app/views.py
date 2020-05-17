from flask import Blueprint, redirect, render_template, request
from app.forms import MessageForm
from app.models import Message
from app import db

message_blueprint = Blueprint("message", __name__)


@message_blueprint.route("/meuform", methods=['GET', 'POST'])
def meuform():
    form = MessageForm()
    messages = Message.query.all()

    if form.validate_on_submit():
        mensagem = Message()
        mensagem.name = form.name.data
        mensagem.text = form.text.data
        mensagem.user_id  = 1

        db.session.add(mensagem)
        db.session.commit()

        return redirect('/meuform')

    return render_template("meuform.html", form=form, messages=messages)