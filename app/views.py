import datetime

from flask import render_template, request, redirect, url_for, flash
from . import app, db
from .models import Purchase, Item
from .forms import PurchaseForm, ItemForm


def item_views():
    title = 'Список товаров'
    items = Item.query.all()
    return render_template('items.html', items=items, title=title)


def item_create():
    title = 'Добавление товара'
    form = ItemForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            # new_item = request.form.get('name')
            # new_price = request.form.get('price')

            # new_item = form.name.data  # Тоже самое что request.form.get
            # new_price = form.price.data
            # item = Item(name=new_item, price=new_price)

            item = Item()
            form.populate_obj(item)  # в случае если слишком много данных (new_item, new_price и тд)

            db.session.add(item)
            db.session.commit()
            flash(f'Товар под номером {item.id}, {item.name} успешно добавлен', 'success')
            return redirect(url_for('item'))
        else:
            # print(form.errors)
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f'Ошибка в поле: "{field}", текст ошибки: "{error}"', 'danger')
    return render_template('item_form.html', form=form, title=title)


def get_single_item(item_id):
    item = Item.query.filter_by(id=item_id).first()
    return render_template('single_item.html', item=item)


def update_single_item(item_id):
    item = Item.query.filter_by(id=item_id).first()
    form = ItemForm(request.form, obj=item)
    if request.method == 'POST':
        if form.validate_on_submit():
            # name = request.form.get('name')
            # price = request.form.get('price')
            # item.name = name
            # item.price = price

            form.populate_obj(item)  # сам понимает что в form, что в item и сопоставляет (замена всего кода сверху)
            db.session.commit()
            flash(f'Товар под номером {item.id}, {item.name} успешно изменен', 'success')
            return redirect(url_for('single_item', item_id=item.id))
        else:
            # print(form.errors)
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f'Ошибка в поле: "{field}", текст ошибки: "{error}"', 'danger')
        return render_template('item_form.html', form=form, item=item)


def delete_single_item(item_id):
    item = Item.query.filter_by(id=item_id).first()
    if request.method == 'GET':
        return render_template('delete_item.html', item=item)
    if request.method == 'POST':
        db.session.delete(item)
        db.session.commit()
        return redirect(url_for('item'))


# ===================================
def purchase_views():
    title = 'данные о клиентах'
    purchases = Purchase.query.all()
    return render_template('purchase.html', purchases=purchases, title=title)


def purchase_create():
    title = 'создание нового клиента'
    form = PurchaseForm(request.form)
    if form.validate_on_submit():
        purchase = Purchase()
        form.populate_obj(purchase)  # в случае если слишком много данных (new_item, new_price и тд)

        db.session.add(purchase)
        db.session.commit()
        flash(f'Покупатель под номером {purchase.id}, {purchase.name} успешно добавлен', 'success')
        return redirect(url_for('purchase'))
    else:
        # print(form.errors)
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'Ошибка в поле: "{field}", текст ошибки: "{error}"', 'danger')

    return render_template('purchase_form.html', form=form, title=title)


def get_single_purchase(purchase_id):
    purchase = Purchase.query.filter_by(id=purchase_id).first()
    return render_template('single_purchase.html', purchase=purchase)


def update_single_purchase(purchase_id):
    title = 'изменение покупателя'
    purchase = Purchase.query.filter_by(id=purchase_id).first()
    form = PurchaseForm(request.form)
    if form.validate_on_submit():
        purchase = Purchase()
        form.populate_obj(purchase)  # в случае если слишком много данных (new_item, new_price и тд)

        db.session.add(purchase)
        db.session.commit()
        flash(f'Покупатель под номером {purchase.id}, {purchase.name} успешно добавлен', 'success')
        return redirect(url_for('single_purchase', purchase_id=purchase.id))
    else:
        # print(form.errors)
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'Ошибка в поле: "{field}", текст ошибки: "{error}"', 'danger')
    return render_template('purchase_form.html', form=form, title=title)


def delete_single_purchase(purchase_id):
    purchase = Purchase.query.filter_by(id=purchase_id).first()
    if request.method == 'GET':
        return render_template('delete_purchase.html', purchase=purchase)
    if request.method == 'POST':
        db.session.delete(purchase)
        db.session.commit()
        flash(f'Данные о продажах под номером {purchase.id} успешно удален', 'success')
        return redirect(url_for('purchase'))
