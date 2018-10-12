from flask import Flask
app = Flask(__name__)

server_ip=''
server_port=''

@app.route('/server/<ip>/<port>')
def server_side(ip,port):
   global server_ip
   global server_port
   server_ip=ip
   server_port=port
   return 'DONE'


@app.route('/client')
def client_side():
   global server_ip
   global server_port
   return  '{} {}'.format(server_ip,server_port) 

if __name__ == '__main__':
   app.run(debug = True)
