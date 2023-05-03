import os
from tkinter import *

nordConnectUS = 'nordvpn connect'
nordConnectDE = 'nordvpn connect germany'
nordConnectP2P = 'nordvpn connect p2p'
nordConnectOnion = 'nordvpn connect onion_over_vpn'
nordStatus = 'nordvpn status'
nordDiconnect = 'nordvpn disconnect'

root = Tk()
root.geometry('400x400')
root.title('NordVPN')

def connectUS():
    os.system(nordConnectUS)

def connectDE():
    os.system(nordConnectDE)

def connectP2P():
    os.system(nordConnectP2P)

def connectOnion():
    os.system(nordConnectOnion)

def vpnStatus():
    os.system(nordStatus)

def disconnect():
    os.system(nordDiconnect)

connectUSButton = Button(root, text='Connect US', command=connectUS)
connectUSButton.pack()
connectDEButton = Button(root, text="Connect DE", command=connectDE)
connectDEButton.pack()
connectP2PButton = Button(root, text='Connect P2P', command=connectP2P)
connectP2PButton.pack()
connectOnionButton = Button(root, text="Connect Onion", command=connectOnion)
connectOnionButton.pack()
vpnStatusButton = Button(root, text="Status", command=vpnStatus)
vpnStatusButton.pack()
disconnectButton = Button(root, text="Disconnect", command=disconnect)
disconnectButton.pack()

root.mainloop()
