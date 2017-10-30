function event::onChannelText(prefix, channel, text)
{
	cmd = "python D:/document/python/irc/ircbot.py " +'"' +text +'"';
  	rtn=executeCommand(cmd);
  	log(rtn);
    send(channel,rtn);
}

