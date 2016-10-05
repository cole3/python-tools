#! /usr/bin/python

import socket,time,string,random,thread,re

server_ip = "127.0.0.1"
server_port = 8554

m_Vars = {
	"bufLen" : 1024 * 10,
	"defaultServerIp" : server_ip,
	"defaultServerPort" : server_port,
	"defaultTestUrl" : "rtsp://" + server_ip + ":" + "server_port" + "/test",
	"defaultUserAgent" : "LibVLC/2.2.4 (LIVE555 Streaming Media v2016.02.22)"
}

def genmsg_OPTIONS(url,seq,userAgent):
	msgRet = "OPTIONS " + url + " RTSP/1.0\r\n"
	msgRet += "CSeq: " + str(seq) + "\r\n"
	msgRet += "User-Agent: " + userAgent + "\r\n"
	msgRet += "\r\n"
	return msgRet

def genmsg_DESCRIBE(url,seq,userAgent):
	msgRet = "DESCRIBE " + url + " RTSP/1.0\r\n"
	msgRet += "CSeq: " + str(seq) + "\r\n"
	msgRet += "User-Agent: " + userAgent + "\r\n"
	msgRet += "Accept: application/sdp\r\n"
	msgRet += "\r\n"
	return msgRet

def genmsg_SETUP(url,seq,userAgent):
	msgRet = "SETUP " + url + " RTSP/1.0\r\n"
	msgRet += "CSeq: " + str(seq) + "\r\n"
	msgRet += "User-Agent: " + userAgent + "\r\n"
	msgRet += "Transport: RTP/AVP;unicast;client_port=50500-50501\r\n"
	msgRet += "\r\n"
	return msgRet

def genmsg_SETUP2(url,seq,userAgent,sessionId):
	msgRet = "SETUP " + url + " RTSP/1.0\r\n"
	msgRet += "CSeq: " + str(seq) + "\r\n"
	msgRet += "User-Agent: " + userAgent + "\r\n"
	msgRet += "Transport: RTP/AVP;unicast;client_port=50502-50503\r\n"
	msgRet += "Session: " + sessionId + "\r\n"
	msgRet += "\r\n"
	return msgRet

def genmsg_PLAY(url,seq,userAgent,sessionId):
	msgRet = "PLAY " + url + " RTSP/1.0\r\n"
	msgRet += "CSeq: " + str(seq) + "\r\n"
	msgRet += "User-Agent: " + userAgent + "\r\n"
	msgRet += "Session: " + sessionId + "\r\n"
	msgRet += "Range: npt=0.000-\r\n"
	msgRet += "\r\n"
	return msgRet

def genmsg_TEARDOWN(url,seq,userAgent,sessionId):
	msgRet = "TEARDOWN " + url + " RTSP/1.0\r\n"
	msgRet += "CSeq: " + str(seq) + "\r\n"
	msgRet += "User-Agent: " + userAgent + "\r\n"
	msgRet += "Session: " + sessionId + "\r\n"
	msgRet += "\r\n"
	return msgRet

def decodeMsg(strContent):
	for line in strContent.strip().replace('\r\n', '\n').split('\n'):
		print line
		mapRetInf = re.search('Session: (.*);', line)
		print mapRetInf
		if mapRetInf:
			print mapRetInf.group(1)
			return mapRetInf.group(1)
	return ""
	
def procCmd(s, msg, ack):
	print msg
	s.send(msg)
	while ack:
		#s.settimeout(3)
		ret = s.recv(m_Vars["bufLen"])
		print ret
		ack = ack -1
	print "------------------------------------\r\n\r\n"
	return ret
	
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((m_Vars["defaultServerIp"],m_Vars["defaultServerPort"]))	
seq  = 1

procCmd(s, genmsg_OPTIONS(m_Vars["defaultTestUrl"],seq,m_Vars["defaultUserAgent"]), 1)
seq = seq + 1

procCmd(s, genmsg_DESCRIBE(m_Vars["defaultTestUrl"],seq,m_Vars["defaultUserAgent"]), 2) # 2
seq = seq + 1

time.sleep(3)

msg1 = procCmd(s, genmsg_SETUP(m_Vars["defaultTestUrl"] + "/trackID=0",seq,m_Vars["defaultUserAgent"]), 1)
seq = seq + 1

sessionId = decodeMsg(msg1)

procCmd(s, genmsg_SETUP2(m_Vars["defaultTestUrl"] + "/trackID=1",seq,m_Vars["defaultUserAgent"],sessionId), 1)
seq = seq + 1

procCmd(s, genmsg_PLAY(m_Vars["defaultTestUrl"],seq,m_Vars["defaultUserAgent"],sessionId), 1)
seq = seq + 1

'''
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
sock.bind((server_ip, 8554))  
while True :
	msgRcv = sock.recv(m_Vars["bufLen"])
	if 0 == len(msgRcv) : break
	print len(msgRcv)
sock.close()
'''

time.sleep(5)

procCmd(s, genmsg_TEARDOWN(m_Vars["defaultTestUrl"],seq,m_Vars["defaultUserAgent"],sessionId), 1)

s.close()