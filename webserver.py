from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Shop, Items, Base
import cgi

engine = create_engine('sqlite:///shopitems.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

session = DBSession()

class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith("/edit"):
                shopId = self.path.split("/")[2]
                myShopQuery = session.query(Shop).filter_by(id=shopId).one()
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>Edit Shop (%s)!" % myShopQuery.name
                output += "<form method='POST' enctype='multipart/form-data' action='/shops/{0}/edit'><h2>Rename your restaurant</h2>" \
                          "<input name='name' type='text' placeholder = '{1}'><input type='submit' value='Edit'></form>".format(myShopQuery.id, myShopQuery.name)
                output += "</body></html>"
                self.wfile.write(output)
                print "GET :" + output
                return
            if self.path.endswith("/delete"):
                shopId = self.path.split("/")[2]
                myShopQuery = session.query(Shop).filter_by(id=shopId).one()
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>Are You Sure you want to DELETE (%s)!" % myShopQuery.name
                output += "<form method='POST' enctype='multipart/form-data' action='/shops/{0}/delete'>" \
                          "<input type='submit' value='Delete'></form>".format(myShopQuery.id)
                output += "</body></html>"
                self.wfile.write(output)
                print "GET :" + output
                return
            if self.path.endswith("/shops"):
                shops = session.query(Shop).all()
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body> Shops <a href = '/hello'>Back to Hello </a> <br> <a href = '/shops/new'>New Shop </a>"
                for shop in shops:
                    output += "<br>  <br>"
                    output += "{1}: {0} <br> <a href = '/shop/{1}/edit'>Edit </a> <br> <a href = '/shop/{1}/delete'>Delete </a>".format(shop.name, shop.id)
                output += "</body></html>"
                self.wfile.write(output)
                print "GET :" + output
                return
            if self.path.endswith("/shops/new"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>Hello!"
                output += "<form method='POST' enctype='multipart/form-data' action='/shops/new'><h2>Make New Restaurant</h2>" \
                          "<input name='name' type='text'><input type='submit' value='Create'></form>"
                output += "</body></html>"
                self.wfile.write(output)
                print "GET :" + output
                return
        except IOError:
            self.send_error(404, "File Not Found %s" % self.path)

    def do_POST(self):
        global namecontent
        try:
            if self.path.endswith("/edit"):
                ctype, pdict = cgi.parse_header(self.headers.getheader('Content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    namecontent = fields.get('name')
                    shopId = self.path.split("/")[2]
                    myShop = session.query(Shop).filter_by(id=shopId).one()
                    if myShop:
                        myShop.name = namecontent[0]
                        session.add(myShop)
                        session.commit()
                        self.send_response(301)
                        self.send_header('Content-type', 'text/html')
                        self.send_header('Location', '/shops')
                        self.end_headers()
                        print "name :" + namecontent[0]
                    return
            if self.path.endswith("/delete"):
                ctype, pdict = cgi.parse_header(self.headers.getheader('Content-type'))
                if ctype == 'multipart/form-data':
                    shopId = self.path.split("/")[2]
                    myShop = session.query(Shop).filter_by(id=shopId).one()
                    if myShop:
                        session.delete(myShop)
                        session.commit()
                        self.send_response(301)
                        self.send_header('Content-type', 'text/html')
                        self.send_header('Location', '/shops')
                        self.end_headers()
                        print "name :" + namecontent[0]
                    return
            if self.path.endswith("/shops/new"):
                ctype, pdict = cgi.parse_header(self.headers.getheader('Content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    namecontent = fields.get('name')
                    shop = Shop(name=namecontent[0])
                    session.add(shop)
                    session.commit()
                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/shops')
                    self.end_headers()
                    print "name :" + namecontent[0]
                    return
            # self.send_response(301)
            # self.end_headers()
            # ctype, pdict = cgi.parse_header(self.headers.getheader('Content-type'))
            # if ctype == 'multipart/form-data':
            #     fields = cgi.parse_multipart(self.rfile, pdict)
            #     namecontent = fields.get('name')
            #     shop = Shop(name=namecontent[0])
            #     session.add(shop)
            #     print "name :" + namecontent[0]
            # output = ""
            # output += "<html><body>"
            # output += "<h2>Okay, Your new restaurant: </h2>"
            # output += "<h1> %s </h1>" % namecontent[0] + "<br>"
            # output += "<a href = '/shops'>Back to Shops </a>"
            # output += "</body></html>"
            # self.wfile.write(output)
            # print "POST :" + output
        except Exception,e:
            print str(e)
            pass


def main():
    global server
    try:
        port = 8080
        server = HTTPServer(('', port), webserverHandler)
        server.serve_forever()
        print "Web server running on port %s" % port
    except KeyboardInterrupt:
        print "^C entered, stopping web server..."
        server.socket.close()


if __name__ == '__main__':
    main()
