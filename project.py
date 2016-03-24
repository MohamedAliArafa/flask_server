from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from werkzeug import secure_filename
from werkzeug import SharedDataMiddleware
import uuid
import logging
import sys
import os

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

from database_setup import Base, Shop, Items, Category

engine = create_engine('sqlite:///shopitems.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.add_url_rule('/uploads/<filename>', 'uploaded_file', build_only=True)
app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {'/uploads': app.config['UPLOAD_FOLDER']})


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
def summery():
    return render_template('summery.html')


@app.route('/GetAllShops/JSON')
def get_all_shops():
    shops = session.query(Shop).all()
    return jsonify(Shop=[i.serialize for i in shops])


@app.route('/GetCategories/JSON')
def get_all_categories():
    categories = session.query(Category).all()
    return jsonify(Category=[i.serialize for i in categories])


@app.route('/newShop/', methods=['GET', 'POST'])
# Task 1: Create route for newShopItem function here
def new_shop():
    global new_shop, filename
    if request.method == 'POST':
        if request.form['name'] and request.form['owner']:
            image_file = request.files['profile_pic']
            if image_file and allowed_file(image_file.filename):
                # filename = secure_filename(image_file.filename)
                filename = str(uuid.uuid4())
                image_file.save(
                    os.path.join(app.config['UPLOAD_FOLDER'], filename + "." + image_file.filename.rsplit('.', 1)[1]))
                new_shop = Shop(name=request.form['name'],
                                profile_pic=filename + "." + image_file.filename.rsplit('.', 1)[1],
                                owner=request.form['owner'],
                                description=request.form['description'],
                                cat_id=request.form.get('cat_id'))
            session.add(new_shop)
            session.commit()
            flash("New Item Added!!")
        return redirect(url_for('get_all_shops'))
    else:
        return render_template('newShop.html')


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


@app.route('/GetItemByCategory/<int:cat_id>/JSON')
def get_item_by_cat_json(cat_id):
    items = session.query(Items).filter_by(cat_id=cat_id)
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
            image_file = request.files['image']
            if image_file and allowed_file(image_file.filename):
                # filename = secure_filename(image_file.filename)
                filename = str(uuid.uuid4())
                image_file.save(
                    os.path.join(app.config['UPLOAD_FOLDER'], filename + "." + image_file.filename.rsplit('.', 1)[1]))

                # category = session.query(Category).filter_by(id=request.form['category']).one()
                new_item = Items(name=request.form['name'], quantity=request.form['quantity'], shop_id=shop_id,
                                 cat_id=request.form.get('category'), price="$" + request.form['price'],
                                 description=request.form['description'], image=filename + "." + image_file.filename.rsplit('.', 1)[1])
            session.add(new_item)
            session.commit()
            # flash("New Item Added!!")
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
    app.secret_key = 'My_Super_Secret_Key'
    app.config['SESSION_TYPE'] = 'filesystem'
    # sess.init_app(app)
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
