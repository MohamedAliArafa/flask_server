from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging
import sys

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

from database_setup import Base, Shop, Items

engine = create_engine('sqlite:///shopitems.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)


@app.route('/')
def summery():
    return render_template('summery.html')


@app.route('/GetAllShops/JSON')
def get_all_hops():
    shops = session.query(Shop).all()
    return jsonify(Shop=[i.serialize for i in shops])


@app.route('/GetShop/<int:shop_id>/JSON')
def get_shop(shop_id):
    shops = session.query(Shop).filter_by(id=shop_id)
    return jsonify(Shop=[i.serialize for i in shops])


@app.route('/GetShopItems/<int:shop_id>/JSON')
def get_shop_items_json(shop_id):
    items = session.query(Items).filter_by(shop_id=shop_id)
    return jsonify(Items=[i.serialize for i in items])


@app.route('/GetItem/<int:item_id>/JSON')
def get_item_json(item_id):
    items = session.query(Items).filter_by(id=item_id)
    return jsonify(Items=[i.serialize for i in items])


@app.route('/GetShopItems/<int:shop_id>/')
def get_shop_items(shop_id):
    shop = session.query(Shop).filter_by(id=shop_id).one()
    items = session.query(Items).filter_by(shop_id=shop_id)
    return render_template('menu.html', shop=shop, items=items)


@app.route('/newShopItem/<int:shop_id>/', methods=['GET', 'POST'])
# Task 1: Create route for newShopItem function here
def new_shop_item(shop_id):
    global new_item
    shop = session.query(Shop).filter_by(id=shop_id).one()
    if request.method == 'POST':
        if request.form['name'] and request.form['quantity']:
            new_item = Items(name=request.form['name'], quantity=request.form['quantity'], shop_id=shop_id)
        session.add(new_item)
        session.commit()
        flash("New Item Added!!")
        return redirect(url_for('get_shop_items', shop_id=shop_id))
    else:
        return render_template('newMenuItem.html', shop=shop)


@app.route('/editShopItem/<int:shop_id>/<int:item_id>/', methods=['GET', 'POST'])
# Task 2: Create route for editShopItem function here
def edit_shop_item(shop_id, item_id):
    shop = session.query(Shop).filter_by(id=shop_id).one()
    item = session.query(Items).filter_by(id=item_id, shop_id=shop_id).one()
    if request.method == 'POST':
        if request.form['name']:
            item.name = request.form['name']
        session.add(item)
        session.commit()
        flash("New Item Edited!!")
        return redirect(url_for('GetShopItems', shop_id=shop_id))
    else:
        return render_template('editMenuItem.html', shop=shop, item=item)


@app.route('/deleteShopItem/<int:shop_id>/<int:item_id>/', methods=['GET', 'POST'])
# Task 3: Create route for deleteShopItem function here
def delete_shop_item(shop_id, item_id):
    shop = session.query(Shop).filter_by(id=shop_id).one()
    item = session.query(Items).filter_by(id=item_id, shop_id=shop_id).one()
    if request.method == 'POST':
        session.delete(item)
        session.commit()
        flash("New Item DELETED!!")
        return redirect(url_for('GetShopItems', shop_id=shop_id))
    else:
        return render_template('deleteMenuItem.html', shop=shop, item=item)


if __name__ == '__main__':
    app.secret_key = "My_Super_Secret_Key"
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
