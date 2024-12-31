from datetime import datetime

# IDGenerator Class: Generate the Invoice ID and Order ID for the Customer bill
class IDGenerator:
    def __init__(self):
        self.invoice_counter = 0
        self.order_counter = 0
        
    # return Invoice ID with fixed sequence - IVFKA<last two digit of year>DAC<5 digits in order starting from 1>
    def generate_invoice_id(self, current_time):
        start_order_chars = "IFVKA"        
        middle_order_chars = "DAC"
        #random.choice(string.ascii_uppercase)
        self.invoice_counter = (self.invoice_counter + 1) % 100000
        return f"{start_order_chars}{str(int(current_time.year%100))}{middle_order_chars}{self.invoice_counter:05d}"
        
    # return Order ID with 9 digits starting from 1
    def generate_order_id(self):
        return (self.order_counter + 1) % 1000000000