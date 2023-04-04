from flask import Flask
from flask import render_template, request, redirect, session
import socket


app = Flask(__name__)
ip_address = socket.gethostbyname(socket.gethostname())

# Print the IP address
print("IP address:", ip_address)

@app.route('/')
def index():  
    return render_template('index.html')



@app.route('/result',methods=['GET','POST'])
def result():  
    my_empty = []
    if request.method == 'POST':
           ip_address  = request.form.get('ip')
           port = request.form.get('port')
           start_port,end_port = port.split('-')
        
            # Loop through each port in the range and attempt to connect
    for port in range(int(start_port), int(end_port) + 1):
                # Create a new socket object
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                # Set a timeout of 1 second for the connection attempt
                s.settimeout(1)
                try:
                    # Attempt to connect to the port
                    s.connect((ip_address, port))
                    # If the connection is successful, print a message
                    with open('static/open_ports.txt','a') as appending:
                          appending.write(f"Port {port} is open\n")
                          
                   # print(f"Port {port} is open")
                except socket.error:
                    # If the connection fails, do nothing
                    pass
                # Always close the socket when finished
                s.close()
           
    return render_template('result.html')

app.run(debug=True)
