import socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Socket created")
    #sender ke ander ip add receiver ka hi aayega hamesha 
    # and receiver ka hi aayega khud ka
    ip_add = " 192.168.129.21"
    port = 33445
    compelete_add = (ip_add, port)
    s.bind(compelete_add)

    while True:
        message , sender_address = s.recvfrom(1024)

        print("Raw Message", message)
        print("Sender Address", sender_address)

        decoded_msg = message.decode("ascii")
        print("Message", decoded_msg)

except Exception as e:
    print("An error occurred:", e)  

    