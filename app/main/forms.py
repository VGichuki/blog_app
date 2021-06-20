from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField
from wtforms.validators import Required,Email,EqualTo

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class UploadBlogForm(FlaskForm):
    title = TextAreaField('Blog Title',validators=[Required()])
    blog =  TextAreaField('your blog',validators=[Required()])
    submit = SubmitField('Post')

class CommentsForm(FlaskForm):
    comment = TextAreaField('Blog Title',validators=[Required()])
    submit = SubmitField('Comment')
