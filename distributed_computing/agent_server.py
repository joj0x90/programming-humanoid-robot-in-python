'''In this file you need to implement remote procedure call (RPC) server

* There are different RPC libraries for python, such as xmlrpclib, json-rpc. You are free to choose.
* The following functions have to be implemented and exported:
 * get_angle
 * set_angle
 * get_posture
 * execute_keyframes
 * get_transform
 * set_transform
* You can test RPC server with ipython before implementing agent_client.py
'''

# add PYTHONPATH
import os
import sys
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'kinematics'))

from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

from inverse_kinematics import InverseKinematicsAgent

class ServerAgent(InverseKinematicsAgent):
    '''ServerAgent provides RPC service
    '''
    
    def __init__(self):
        super(InverseKinematicsAgent, self).__init__("test", 2)
        server = SimpleXMLRPCServer(('localhost', 8000))
        # server.register_introspection_functions()
        server.register_instance(self)
        server.serve_forever()
        self.transform = 0
    
    def get_angle(self, joint_name):
        '''get sensor value of given joint'''
        return perception.joint[joint_name]
    
    def set_angle(self, joint_name, angle):
        '''set target angle of joint for PID controller
        '''
        self.perception.joint[joint_name] = angle

    def get_posture(self):
        '''return current posture of robot'''
        return self.posture

    def execute_keyframes(self, keyframes):
        '''excute keyframes, note this function is blocking call,
        e.g. return until keyframes are executed
        '''
        self.keyframes = keyframes

    def get_transform(self, name):
        '''get transform with given name
        '''
        return self.transform

    def set_transform(self, effector_name, transform):
        '''solve the inverse kinematics and control joints use the results
        '''
        self.transform = transform

if __name__ == '__main__':
    agent = ServerAgent()
    agent.run()

