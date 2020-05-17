from flask_wtf import FlaskForm
from wtforms.fields import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class MessageForm(FlaskForm):
    name = StringField("Nome Completo", validators=[DataRequired("este campo é obrigatório")])
    text = TextAreaField("Mensagem", validators=[DataRequired("este campo é obrigatório")])
    register = SubmitField("Cadastrar")