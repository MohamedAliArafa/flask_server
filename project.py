from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Shop, Items

engine = create_engine('sqlite:///shopitems.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)


@app.route('/GetShopItems/<int:shop_id>/JSON')
def GetShopItemsJSON(shop_id):
    items = session.query(Items).filter_by(shop_id=shop_id)
    return jsonify(Items=[i.serialize for i in items])


@app.route('/GetItem/<int:item_id>/JSON')
def GetItemJSON(item_id):
    items = session.query(Items).filter_by(id=item_id)
    return jsonify(Items=[i.serialize for i in items])


@app.route('/')
@app.route('/GetShopItems/<int:shop_id>/')
def GetShopItems(shop_id):
    shop = session.query(Shop).filter_by(id=shop_id).one()
    items = session.query(Items).filter_by(shop_id=shop_id)
    return render_template('menu.html', shop=shop, items=items)


@app.route('/newShopItem/<int:shop_id>/', methods=['GET', 'POST'])
# Task 1: Create route for newShopItem function here
def newShopItem(shop_id):
    shop = session.query(Shop).filter_by(id=shop_id).one()
    if request.method == 'POST':
        if request.form['name']:
            newItem = Items(name=request.form['name'], shop_id=shop_id)
        session.add(newItem)
        session.commit()
        flash("New Item Added!!")
        return redirect(url_for('GetShopItems', shop_id=shop_id))
    else:
        return render_template('newMenuItem.html', shop=shop)


@app.route('/editShopItem/<int:shop_id>/<int:item_id>/', methods=['GET', 'POST'])
# Task 2: Create route for editShopItem function here
def editShopItem(shop_id, item_id):
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
def deleteShopItem(shop_id, item_id):
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
    #app.run(host='0.0.0.0', port=5000)
