from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, SubmitField, validators, PasswordField
from wtforms.validators import DataRequired, Length
from flask_ckeditor import CKEditorField


class ToDoForm(FlaskForm):
    titleField = StringField('Title', validators=[
        DataRequired(),
        Length(max=50),
        ])
    descriptionField = CKEditorField('Description')
    deadlineField = DateTimeField('Due', format='%d-%m-%Y %H:%M', validators=[DataRequired()], id='DateField')
    submitField = SubmitField(label="Add Task")


class EditForm(FlaskForm):
    titleField = StringField('Title', validators=[DataRequired()])
    descriptionField = CKEditorField('Description')
    deadlineField = DateTimeField('Deadline', format='%d-%m-%Y %H:%M')
    startField = DateTimeField('Start Date', format='%d-%m-%Y %H:%M')
    endField = DateTimeField('End Date', format='%d-%m-%Y %H:%M')
    submitField = SubmitField(label='Update Task')


class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Sign Me Up!")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Let Me In!")

