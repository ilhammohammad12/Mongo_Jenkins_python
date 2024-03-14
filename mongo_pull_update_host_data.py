from pymongo import MongoClient

def connect_database(database_name=None, collection=None, collection2=None):
    client = MongoClient("mongodb://root:123@192.168.56.200:27017/")
    if client:
        print("connection successfull", client)
        database_details = client[database_name]
        hotel = database_details[collection]
        hotel_data = hotel.find()
        host = database_details[collection2]
    else:
        print("connection failed")
    return client, hotel_data , host

def data_mining_hotel_data(hotel_data,host):
    
    for data in hotel_data:
        com_data = data['host']
        hotel_data = {
        "Hotel_name": data['name'],
        "Hotel_id" : data['_id'],
        #"Host" : data['host']
        }
        com_data.update(hotel_data) 
        h_result = host.insert_one(com_data)
    return h_result
    
    

if __name__ == "__main__":

    client, hotel_data, host_data = connect_database(database_name='Airbnb', collection='hotel_records',collection2='host_data')
    Result = data_mining_hotel_data(hotel_data,host_data)
    print('Host data updated into the host collection')
    print("closing the collection")

    client.close()
