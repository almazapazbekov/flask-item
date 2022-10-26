from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, IntegerField, SelectField, DateField, validators, ValidationError

from .models import Item


class ItemForm(FlaskForm):
    name = StringField(label='Название товара', validators=[validators.DataRequired()])  # не отправит пустую форму
    price = IntegerField(label='Цена товара', validators=[validators.DataRequired()])
    submit = SubmitField(label='Сохранить товар')

    def validate_price(self, price):
        if price.data < 100:
            raise ValidationError("товар не может стоить менее 100 единиц")


class PurchaseForm(FlaskForm):
    name = StringField(label='Имя клиента', validators=[validators.DataRequired()])
    age = IntegerField(label='возраст', validators=[validators.DataRequired()])
    item_id = SelectField(label='Что купил', validators=[validators.DataRequired()])
    date_purchase = DateField('Дата', validators=[validators.DataRequired()])
    submit = SubmitField(label='Сохранить покупку')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        result = []
        for item in Item.query.all():
            result.append((item.id, item.name))
        self.item_id.choices = result

    def validate_age(self, age):
        if age.data < 18:
            raise ValidationError('ограничение по возрасту - 18 лет.')
