#Generic Consumer- Websocketconsumer- and AsynWebsocketConsumer
#also known as synconsumer
from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from asgiref.sync import async_to_sync

#real time data sending and reccieving
class MyWebSocketConsumer(WebsocketConsumer):
    #This handler is called when client initially opens a connection 
    #and is about to finish the websocket 
    def connect(self):
        print("My first Web Socket Conected!!")
        print("Channel layers:..",self.channel_layer)
        print("Channel Name:..",self.channel_name)
        self.group_name=self.scope['url_route']['kwargs']['groupkaname']
        print("Group Name: ",self.group_name)
        async_to_sync (self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept()       #To accept the connection
    
    # This handler is called when data recieve from client
    def receive(self, text_data=None, bytes_data=None):
        print("My first Message recient from client!!\n'{}'".format(text_data))
        
    #This handler is called when connection is closed from client, server or else
    def disconnect(self, code):
        print("My first WebSocket disconnected!!", code)

class MyAsyncWebSocketConsumer(AsyncWebsocketConsumer):
    #This handler is called when client initially opens a connection 
    #and is about to finish the websocket 
    async def connect(self):
        print("My first Web Socket Conected!!")
        await self.accept()       #To accept the connection
    
    # This handler is called when data recieve from client
    async def receive(self, text_data=None, bytes_data=None):
        print("My first Message recient from client!!\n'{}'".format(text_data))
        #to send data to client--------
        await self.send(text_data='I am sending message fromserver to client!!!')
        for i in range(20):
            await self.send(text_data=str(i)) #send data to client..
    #This handler is called when connection is closed from client, server or else
    async def disconnect(self, code):
        print("My first WebSocket disconnected!!", code)