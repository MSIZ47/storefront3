from locust import HttpUser,task,between
from random import randint


# hint : alwayes end urls with / otherwise you will get failiure on locust

class WebsiteUser(HttpUser):
    #locust will randomly wait 1 to 5 seconds between task
    wait_time =between(1,5) 

    #1 first task = Viewing products
    @task(2)
    def view_products(self):
        collection_id = randint(2,6)
        self.client.get(f'/store/products/?collection_id={collection_id}', name = '/store/products/')

    #2 first task = Viewing product details
    @task(4)
    def view_product(self):
        product_id = randint(1,1000)
        self.client.get(f'/store/products/{product_id}', name = 'store/products/:id')
         
    #3 third task = Add product to cart
    @task(1)
    def add_to_cart(self):
        product_id = randint(1,10)
        self.client.post(f'/store/carts/{self.cart_id}/items/',
                         name = '/store/carts/items',
                         json={'product_id':product_id,'quantity': 1})

    #this function create a cart whenever a user start browsing in our site an we get the cart_id of that and give it to add_to_cart task
    def on_start(self):
        response = self.client.post(f'/store/carts/')
        result=response.json()#we create this object so that we get json object in the response and its a dict
        self.cart_id = result['id']  