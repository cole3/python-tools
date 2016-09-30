import sys, os, urllib
 
def getSpeech(phrase):
    googleAPIurl = "http://translate.google.com/translate_tts?tl=zh&"
    param = {'q': phrase}
    data = urllib.urlencode(param)
    googleAPIurl += data # Append the parameters
    print googleAPIurl
    return googleAPIurl
 
def talk(text): # This will call mplayer and will play the sound
    os.system('mplayer.exe ' + '\"' + getSpeech(text) + '\"')
 
if __name__ == "__main__":
	string = "于大雪"
	s = string.decode('utf-8').encode('gb2312')
	print s
	talk(s)
	
	
	
#	http://translate.google.com/translate_tts?tl=en&q=hello+world
#	http://translate.google.com/translate_tts?tl=zh&q=于大雪
#	http://translate.google.com/translate_tts?tl=zh&q=%E4%BA%8E%E5%A4%A7%E9%9B%AA