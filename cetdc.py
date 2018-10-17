from flask import Flask
app = Flask(__name__)

server_ip=''
server_port=''
client_ver='1'

@app.route('/server/<ip>/<port>')
def server_side(ip,port):
   global server_ip
   global server_port
   server_ip=ip
   server_port=port
   return 'DONE'

@app.route('/clientver/<vers>')
def clientver_side(vers):
   global client_ver
   client_ver=vers
   return 'DONE'

@app.route('/client')
def client_side():
   global server_ip
   global server_port
   global client_ver
   return  '{} {} {}'.format(server_ip,server_port,client_ver) 

if __name__ == '__main__':
   app.run(debug = True)
