class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'{self.name.title()} has {self.type} cuisine')

    def open_restaurant(self):
        print('The restaurant is open!')
    
    def set_number_served(self,served):
        self.number_served = served
        print(f'Served clients: {self.number_served}')
    
    def increment_number_served(self,plus_to_number_served):
        self.number_served += plus_to_number_served
        print(f'Served clients are grown now: {self.number_served}')