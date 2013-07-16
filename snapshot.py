#!/usr/bin/python


import vlc
import sys
import Queue, threading

testbase    = "http://www.7po.com/interface.php?mod=Android"
testgood    = "http://ipadlive.cntv.soooner.com/cctv_p2p_hdcctv3.m3u8"
testbad     = "rtsp://74.82.62.53:1935/liverepeater/10.stream"
#testbad     = "rtsp://116.199.127.68/dongfang"


def play_shot(q,i,u):
	p=i.media_player_new()
	m=i.media_new(u)
	p.set_media(m)
	q.put(p.play())
	#if p.video_take_snapshot(0,'.',0,0) == -1:
	#	open('badfile.png', 'w').close()


if __name__ == '__main__':
	i=vlc.Instance()
	q=Queue.Queue()
	urls = [testgood, testbad]
	for u in urls:
		print u
		t = threading.Thread(target=play_shot, args=(q,i,u))
		t.daemon = True
		t.start()

#s = q.get()
#print s
