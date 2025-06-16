import socket
try:
    ##creating socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #dgram -- datagram
    print("Socket successfully created")
    ip_add = "192.168.129.117"
    port = 33445                                     #0 - 65535
    target_add = (ip_add, port)
    message = input("Enter the message: 😊")
    encoded_msg = message.encode("ascii")
    s.sendto(encoded_msg, target_add)
    print("Message sent successfully")
    s.close()

except Exception as e:
    print(" An Error occurred:", e)
    
    