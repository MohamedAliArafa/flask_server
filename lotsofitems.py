from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Shop, Base, Items, Category, ShopCategory, SubCategory

engine = create_engine('sqlite:///shopitems.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

Cat1 = Category(name="Books", hasSub="true")
Cat2 = Category(name="Clothing", hasSub="true")
Cat3 = Category(name="Jewelry", hasSub="true")
Cat4 = Category(name="Home", hasSub="true")

SubCat1 = SubCategory(name="Comics", category=Cat1)
SubCat2 = SubCategory(name="Horror", category=Cat1)
SubCat3 = SubCategory(name="Novel", category=Cat1)

SubCat4 = SubCategory(name="Dresses", category=Cat2)
SubCat5 = SubCategory(name="Children", category=Cat2)
SubCat6 = SubCategory(name="Robes", category=Cat2)

SubCat7 = SubCategory(name="Necklaces", category=Cat3)
SubCat8 = SubCategory(name="Earrings", category=Cat3)
SubCat9 = SubCategory(name="Bracelets", category=Cat3)
SubCat10 = SubCategory(name="Rings", category=Cat3)

SubCat11 = SubCategory(name="Decor", category=Cat4)
SubCat12 = SubCategory(name="Lighting", category=Cat4)
SubCat13 = SubCategory(name="kitchen", category=Cat4)

SCat1 = ShopCategory(name="Book Store")
SCat2 = ShopCategory(name="Cloth Store")
SCat3 = ShopCategory(name="Jewelery Store")
SCat4 = ShopCategory(name="House Store")
SCat5 = ShopCategory(name="Adventure Store")

# Menu for UrbanBurger
Shop1 = Shop(name="Urban Burger", owner="Mohamed Arafa",
             profile_pic="d48e33b3-e4f6-4c71-8577-4abba285021c.jpg",
             avatar_pic="d48e33b3-e4f6-4c71-8577-4abba285021c.jpg",
             description="cool shop at tanta that sells the best and the best only", category=SCat1)

session.add(Shop1)
session.commit()

Items2 = Items(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce", quantity=10,
               price="$7.50", short_description="Entree", SubCategory=SubCat4, shop=Shop1)

session.add(Items2)
session.commit()

Items1 = Items(name="French Fries", description="with garlic and parmesan", quantity=10,
               price="$2.99", short_description="Appetizer", SubCategory=SubCat3, shop=Shop1)

session.add(Items1)
session.commit()

Items2 = Items(name="Chicken Burger", description="Juicy grilled chicken patty with tomato mayo and lettuce",
               quantity=10,
               price="$5.50", short_description="Entree", SubCategory=SubCat5, shop=Shop1)

session.add(Items2)
session.commit()

Items3 = Items(name="Chocolate Cake", description="fresh baked and served with ice cream", quantity=10,
               price="$3.99", short_description="Dessert", SubCategory=SubCat3, shop=Shop1)

session.add(Items3)
session.commit()

Items4 = Items(name="Sirloin Burger", description="Made with grade A beef", quantity=10,
               price="$7.99", short_description="Entree", SubCategory=SubCat11, shop=Shop1)

session.add(Items4)
session.commit()

Items5 = Items(name="Root Beer", description="16oz of refreshing goodness", quantity=10,
               price="$1.99", short_description="Beverage", SubCategory=SubCat2, shop=Shop1)

session.add(Items5)
session.commit()

Items6 = Items(name="Iced Tea", description="with Lemon", quantity=10,
               price="$.99", short_description="Beverage", SubCategory=SubCat4, shop=Shop1)

session.add(Items6)
session.commit()

Items7 = Items(name="Grilled Cheese Sandwich", description="On texas toast with American Cheese", quantity=10,
               price="$3.49", short_description="Entree", SubCategory=SubCat10, shop=Shop1)

session.add(Items7)
session.commit()

Items8 = Items(name="Veggie Burger", description="Made with freshest of ingredients and home grown spices", quantity=10,
               price="$5.99", short_description="Entree", SubCategory=SubCat3, shop=Shop1)

session.add(Items8)
session.commit()


# Menu for Super Stir Fry
Shop2 = Shop(name="Urban Burger", owner="Mohamed Arafa",
             profile_pic="d48e33b3-e4f6-4c71-8577-4abba285021c.jpg",
             avatar_pic="d48e33b3-e4f6-4c71-8577-4abba285021c.jpg",
             description="cool shop at tanta that sells the best and the best only", category=SCat2)

session.add(Shop2)
session.commit()

Items1 = Items(name="Chicken Stir Fry", description="With your choice of noodles vegetables and sauces", quantity=10,
               price="$7.99", short_description="Entree", SubCategory=SubCat4, shop=Shop2)

session.add(Items1)
session.commit()

Items2 = Items(
    name="Peking Duck",
    description=" A famous duck dish from Beijing[1] that has been prepared since the imperial era. The meat is prized for its thin, crisp skin, with authentic versions of the dish serving mostly the skin and little meat, sliced in front of the diners by the cook",
    price="$25", quantity=10, short_description="Entree", SubCategory=SubCat12, shop=Shop2)

session.add(Items2)
session.commit()

Items3 = Items(name="Spicy Tuna Roll", description="Seared rare ahi, avocado, edamame, cucumber with wasabi soy sauce ",
               quantity=10,
               price="15", short_description="Entree", SubCategory=SubCat3, shop=Shop2)

session.add(Items3)
session.commit()

Items4 = Items(name="Nepali Momo ", description="Steamed dumplings made with vegetables, spices and meat. ",
               quantity=10,
               price="12", short_description="Entree", SubCategory=SubCat5, shop=Shop2)

session.add(Items4)
session.commit()

Items5 = Items(name="Beef Noodle Soup",
               description="A Chinese noodle soup made of stewed or red braised beef, beef broth, vegetables and Chinese noodles.",
               quantity=10,
               price="14", short_description="Entree", SubCategory=SubCat2, shop=Shop2)

session.add(Items5)
session.commit()

Items6 = Items(name="Ramen",
               description="a Japanese noodle soup dish. It consists of Chinese-style wheat noodles served in a meat- or (occasionally) fish-based broth, often flavored with soy sauce or miso, and uses toppings such as sliced pork, dried seaweed, kamaboko, and green onions.",
               quantity=10,
               price="12", short_description="Entree", SubCategory=SubCat4, shop=Shop2)

session.add(Items6)
session.commit()


# Menu for Panda Garden
Shop1 = Shop(name="Urban Burger", owner="Mohamed Arafa",
             profile_pic="d48e33b3-e4f6-4c71-8577-4abba285021c.jpg",
             avatar_pic="d48e33b3-e4f6-4c71-8577-4abba285021c.jpg",
             description="cool shop at tanta that sells the best and the best only", category=SCat3)

session.add(Shop1)
session.commit()

Items1 = Items(name="Pho",
               description="a Vietnamese noodle soup consisting of broth, linguine-shaped rice noodles called banh pho, a few herbs, and meat.",
               quantity=10,
               price="$8.99", short_description="Entree", SubCategory=SubCat13, shop=Shop1)

session.add(Items1)
session.commit()

Items2 = Items(name="Chinese Dumplings",
               description="a common Chinese dumpling which generally consists of minced meat and finely chopped vegetables wrapped into a piece of dough skin. The skin can be either thin and elastic or thicker.",
               quantity=10,
               price="$6.99", short_description="Appetizer", SubCategory=SubCat3, shop=Shop1)

session.add(Items2)
session.commit()

Items3 = Items(name="Gyoza",
               description="The most prominent differences between Japanese-style gyoza and Chinese-style jiaozi are the rich garlic flavor, which is less noticeable in the Chinese version, the light seasoning of Japanese gyoza with salt and soy sauce, and the fact that gyoza wrappers are much thinner",
               quantity=10,
               price="$9.95", short_description="Entree", SubCategory=SubCat1, shop=Shop1)

session.add(Items3)
session.commit()

Items4 = Items(name="Stinky Tofu", description="Taiwanese dish, deep fried fermented tofu served with pickled cabbage.",
               quantity=10,
               price="$6.99", short_description="Entree", SubCategory=SubCat5, shop=Shop1)

session.add(Items4)
session.commit()

Items2 = Items(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce", quantity=10,
               price="$9.50", short_description="Entree", SubCategory=SubCat2, shop=Shop1)

session.add(Items2)
session.commit()


# Menu for Thyme for that
Shop1 = Shop(name="Urban Burger", owner="Mohamed Arafa",
             profile_pic="d48e33b3-e4f6-4c71-8577-4abba285021c.jpg",
             avatar_pic="d48e33b3-e4f6-4c71-8577-4abba285021c.jpg",
             description="cool shop at tanta that sells the best and the best only", category=SCat4)

session.add(Shop1)
session.commit()

Items1 = Items(name="Tres Leches Cake",
               description="Rich, luscious sponge cake soaked in sweet milk and topped with vanilla bean whipped cream and strawberries.",
               quantity=10,
               price="$2.99", short_description="Dessert", SubCategory=SubCat5, shop=Shop1)

session.add(Items1)
session.commit()

Items2 = Items(name="Mushroom risotto", description="Portabello mushrooms in a creamy risotto", quantity=10,
               price="$5.99", short_description="Entree", SubCategory=SubCat1, shop=Shop1)

session.add(Items2)
session.commit()

Items3 = Items(name="Honey Boba Shaved Snow",
               description="Milk snow layered with honey boba, jasmine tea jelly, grass jelly, caramel, cream, and freshly made mochi",
               quantity=10,
               price="$4.50", short_description="Dessert", SubCategory=SubCat3, shop=Shop1)

session.add(Items3)
session.commit()

Items4 = Items(name="Cauliflower Manchurian",
               description="Golden fried cauliflower florets in a midly spiced soya,garlic sauce cooked with fresh cilantro, celery, chilies,ginger & green onions",
               quantity=10,
               price="$6.95", short_description="Appetizer", SubCategory=SubCat4, shop=Shop1)

session.add(Items4)
session.commit()

Items5 = Items(name="Aloo Gobi Burrito",
               description="Vegan goodness. Burrito filled with rice, garbanzo beans, curry sauce, potatoes (aloo), fried cauliflower (gobi) and chutney. Nom Nom",
               quantity=10,
               price="$7.95", short_description="Entree", SubCategory=SubCat2, shop=Shop1)

session.add(Items5)
session.commit()

Items2 = Items(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce", quantity=10,
               price="$6.80", short_description="Entree", SubCategory=SubCat1, shop=Shop1)

session.add(Items2)
session.commit()


# Menu for Tony's Bistro
Shop1 = Shop(name="Urban Burger", owner="Mohamed Arafa",
             profile_pic="d48e33b3-e4f6-4c71-8577-4abba285021c.jpg",
             avatar_pic="d48e33b3-e4f6-4c71-8577-4abba285021c.jpg",
             description="cool shop at tanta that sells the best and the best only", category=SCat5)

session.add(Shop1)
session.commit()

Items1 = Items(name="Shellfish Tower",
               description="Lobster, shrimp, sea snails, crawfish, stacked into a delicious tower", quantity=10,
               price="$13.95", short_description="Entree", SubCategory=SubCat7, shop=Shop1)

session.add(Items1)
session.commit()

Items2 = Items(name="Chicken and Rice", description="Chicken... and rice", quantity=10,
               price="$4.95", short_description="Entree", SubCategory=SubCat8, shop=Shop1)

session.add(Items2)
session.commit()

Items3 = Items(name="Mom's Spaghetti", description="Spaghetti with some incredible tomato sauce made by mom",
               quantity=10,
               price="$6.95", short_description="Entree", SubCategory=SubCat5, shop=Shop1)

session.add(Items3)
session.commit()

Items4 = Items(name="Choc Full O\' Mint (Smitten\'s Fresh Mint Chip ice cream)", quantity=10,
               description="Milk, cream, salt, ..., Liquid nitrogen magic", price="$3.95", short_description="Dessert",
               shop=Shop1)

session.add(Items4)
session.commit()

Items5 = Items(name="Tonkatsu Ramen", description="Noodles in a delicious pork-based broth with a soft-boiled egg",
               quantity=10,
               price="$7.95", short_description="Entree", SubCategory=SubCat6, shop=Shop1)

session.add(Items5)
session.commit()


# Menu for Andala's
Shop1 = Shop(name="Urban Burger", owner="Mohamed Arafa",
             profile_pic="d48e33b3-e4f6-4c71-8577-4abba285021c.jpg",
             avatar_pic="d48e33b3-e4f6-4c71-8577-4abba285021c.jpg",
             description="cool shop at tanta that sells the best and the best only", category=SCat1)

session.add(Shop1)
session.commit()

Items1 = Items(name="Lamb Curry",
               description="Slow cook that thang in a pool of tomatoes, onions and alllll those tasty Indian spices. Mmmm.",
               quantity=10,
               price="$9.95", short_description="Entree", SubCategory=SubCat2, shop=Shop1)

session.add(Items1)
session.commit()

Items2 = Items(name="Chicken Marsala", description="Chicken cooked in Marsala wine sauce with mushrooms", quantity=10,
               price="$7.95", short_description="Entree", SubCategory=SubCat1, shop=Shop1)

session.add(Items2)
session.commit()

Items3 = Items(name="Potstickers", description="Delicious chicken and veggies encapsulated in fried dough.",
               quantity=10,
               price="$6.50", short_description="Appetizer", SubCategory=SubCat5, shop=Shop1)

session.add(Items3)
session.commit()

Items4 = Items(name="Nigiri Sampler", description="Maguro, Sake, Hamachi, Unagi, Uni, TORO!", quantity=10,
               price="$6.75", short_description="Appetizer", SubCategory=SubCat9, shop=Shop1)

session.add(Items4)
session.commit()

Items2 = Items(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce", quantity=10,
               price="$7.00", short_description="Entree", SubCategory=SubCat4, shop=Shop1)

session.add(Items2)
session.commit()


# Menu for Auntie Ann's
Shop1 = Shop(name="Urban Burger", owner="Mohamed Arafa",
             profile_pic="d48e33b3-e4f6-4c71-8577-4abba285021c.jpg",
             avatar_pic="d48e33b3-e4f6-4c71-8577-4abba285021c.jpg",
             description="cool shop at tanta that sells the best and the best only", category=SCat2)

session.add(Shop1)
session.commit()

Items9 = Items(name="Chicken Fried Steak",
               description="Fresh battered sirloin steak fried and smothered with cream gravy", quantity=10,
               price="$8.99", short_description="Entree", SubCategory=SubCat1, shop=Shop1)

session.add(Items9)
session.commit()

Items1 = Items(name="Boysenberry Sorbet",
               description="An unsettlingly huge amount of ripe berries turned into frozen (and seedless) awesomeness",
               quantity=10,
               price="$2.99", short_description="Dessert", SubCategory=SubCat2, shop=Shop1)

session.add(Items1)
session.commit()

Items2 = Items(name="Broiled salmon", description="Salmon fillet marinated with fresh herbs and broiled hot & fast",
               quantity=10,
               price="$10.95", short_description="Entree", SubCategory=SubCat9, shop=Shop1)

session.add(Items2)
session.commit()

Items3 = Items(name="Morels on toast (seasonal)",
               description="Wild morel mushrooms fried in butter, served on herbed toast slices", quantity=10,
               price="$7.50", short_description="Appetizer", SubCategory=SubCat1, shop=Shop1)

session.add(Items3)
session.commit()

Items4 = Items(name="Tandoori Chicken",
               description="Chicken marinated in yoghurt and seasoned with a spicy mix(chilli, tamarind among others) and slow cooked in a cylindrical clay or metal oven which gets its heat from burning charcoal.", quantity=10,
               price="$8.95", short_description="Entree", SubCategory=SubCat4, shop=Shop1)

session.add(Items4)
session.commit()

Items2 = Items(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce", quantity=10,
               price="$9.50", short_description="Entree", SubCategory=SubCat2, shop=Shop1)

session.add(Items2)
session.commit()

Items10 = Items(name="Spinach Ice Cream", description="vanilla ice cream made with organic spinach leaves", quantity=10,
                price="$1.99", short_description="Dessert", SubCategory=SubCat3, shop=Shop1)

session.add(Items10)
session.commit()


# Menu for Cocina Y Amor
Shop1 = Shop(name="Cocina Y Amor ", owner="Mohamed Arafa")

session.add(Shop1)
session.commit()

Items1 = Items(name="Super Burrito Al Pastor",
               description="Marinated Pork, Rice, Beans, Avocado, Cilantro, Salsa, Tortilla", quantity=10,
               price="$5.95", short_description="Entree", SubCategory=SubCat3, shop=Shop1)

session.add(Items1)
session.commit()

Items2 = Items(name="Cachapa",
               description="Golden brown, corn-based Venezuelan pancake; usually stuffed with queso telita or queso de mano, and possibly lechon. ", quantity=10,
               price="$7.99", short_description="Entree", SubCategory=SubCat5, shop=Shop1)

session.add(Items2)
session.commit()

Shop1 = Shop(name="Urban Burger", owner="Mohamed Arafa",
             profile_pic="d48e33b3-e4f6-4c71-8577-4abba285021c.jpg",
             avatar_pic="d48e33b3-e4f6-4c71-8577-4abba285021c.jpg",
             description="cool shop at tanta that sells the best and the best only", category=SCat3)
session.add(Shop1)
session.commit()

Items1 = Items(name="Chantrelle Toast",
               description="Crispy Toast with Sesame Seeds slathered with buttery chantrelle mushrooms", quantity=10,
               price="$5.95", short_description="Appetizer", SubCategory=SubCat2, shop=Shop1)

session.add(Items1)
session.commit()

Items1 = Items(name="Guanciale Chawanmushi", quantity=10,
               description="Japanese egg custard served hot with spicey Italian Pork Jowl (guanciale)",
               price="$6.95", short_description="Dessert", SubCategory=SubCat4, shop=Shop1)

session.add(Items1)
session.commit()

Items1 = Items(name="Lemon Curd Ice Cream Sandwich",
               description="Lemon Curd Ice Cream Sandwich on a chocolate macaron with cardamom meringue and cashews", quantity=10,
               price="$4.25", short_description="Dessert", SubCategory=SubCat3, shop=Shop1)

session.add(Items1)
session.commit()

print "added menu items!"
