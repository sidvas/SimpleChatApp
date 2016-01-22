$(function () {
var socket = io(); //Socket connection - client side
var $input = $('.input'); //get input from form
var $msgs = $('.msgdisplay'); //display window for chat
var user; //username for current socket
var numMsgs = 0;


var swear_words = ['anal', 'anus', 'arse', 'ass', 'asshole', 'ballsack', 'balls', 'bastard', 'behenchod', 'bitch',
 'biatch', 'bloody', 'blowjob', 'blow job', 'bollock', 'bollok', 'boner', 'boob', 'boobies', 
 'bugger', 'bum', 'butt', 'buttplug', 'chut', 'clitoris', 'cock', 'coon', 'crap', 'cunt',
 'damn', 'dick', 'dickhead', 'dildo', 'dyke', 'fag', 'faggot', 'feck', 'fellate', 'fellatio', 'felching',
 'fuck', 'f u c k', 'fudgepacker', 'fudge packer', 'flange', 'gandu', 'Goddamn', 'God damn',
 'hell', 'homo', 'jerk', 'jizz', 'knobend', 'knob end', 'labia', 'lmao', 'lmfao', 'motherfucker', 'muff',
 'nigger', 'nigga', 'omg', 'penis', 'piss', 'poop', 'prick', 'pube', 'pussy', 'queer', 'scrotum',
 'sex', 'shit', 's hit', 'sh1t', 'slut', 'smegma', 'spunk', 'sonofabitch', 'tit', 'titties',
 'tosser', 'trololol', 'turd', 'twat', 'vagina', 'wank', 'whore', 'wtf', 'xenophobe']; //Censored words on public channel


var setUser = function() {
	user = prompt('Pick a username!'); //Ask for username of page load
};

var createMsg = function() {
	var msg = $('<div>').text($input.val()).text();
	return { //Extract data from form
		username: user,
		msg: msg,  
	};
};
var sendMessage = function(data) { //Function to send message to every other user + server
	socket.emit('new msg', data);
};

var addToMsgDisplay = function(data) { //Function to add message from current socket to msg display window
	var $msgDiv = $("<div class='message'>"); //setup html
	var $msgHead = $("<span class='messageHead'>");
	var $msgBody = $("<span class='messageBody'>");

	$msgHead.html(data.username + " : ");
	$msgBody.html(data.msg);
	$msgDiv.append($msgHead, $msgBody);
	console.log(data.username + " : " + data.msg);
	$msgs.append($msgDiv);

	numMsgs++;

	if(numMsgs>50) {

		$msgs.find('message').first().remove();
		numMsgs--;
	}
	$msgs.scrollTop($msgs[0].scrollHeight);
};

var censorMsg = function(data) { //Function that censors msgs before they are displayed on public channel
	var wordsInMsg = data.msg.split(" "); 
	for(var i = 0; i < wordsInMsg.length; i++) {
		if($.inArray(wordsInMsg[i], swear_words)!=-1) {
			wordsInMsg[i] = "" + Array(wordsInMsg[i].length+1).join("*");
		}
	}

	return {
		username: data.username,
		msg: wordsInMsg.join(" "),
	}

};

$('.msgform').submit(function(event) { //What happens when the current socket submits a new message to chat
	event.preventDefault();
	var curmsg = censorMsg(createMsg());
	addToMsgDisplay(curmsg);
	sendMessage(curmsg);
	$input.val("");
});

socket.on('new msg', function(data) { //What happens when the current socket receives a msg
	console.log('msg received...');
	addToMsgDisplay(data);
});

setUser();
});