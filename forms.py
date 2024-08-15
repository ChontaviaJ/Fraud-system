from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired

class AnalysisForm(FlaskForm):
    method = SelectField('Choose Data Analysis Method:', choices=[
        ('logistic_regression', 'Logistic Regression'),
        ('random_forest', 'Random Forest'),
        ('svm', 'Support Vector Machine')
    ], validators=[DataRequired()])
    submit = SubmitField('Run Analysis')
