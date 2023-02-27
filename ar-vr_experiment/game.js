// define quotes to be used
let quotes_array = [
  "please type this text as fast as you can",
  "far far away behind the word mountains",
  "far from the countries vokalia and consonantia",
  "there live the blind texts separated they live",
  "right at the coast of the semantics a large",
  "a small river named duden flows by their place",
  "it with the necessary regelialia it is a",
  "in which roasted parts of sentences fly",
  "even the all powerful pointing has no control",
  "about the blind texts it is an almost",
  "life One day however a small line of blind text",
  "by the name of lorem ipsum decided to leave",
  "for the far world of grammar",
  "the big oxmox advised her not to do so",
  "because there were thousands of bad Commas",
  "wild question marks and devious semikoli",
  "but the little blind text did not listen",
  "she packed her versalia put her into the belt",
  "and made herself on the way",
  "when she reached the first hills of the mountains",
  "she had a last view back of her hometown",
  "the headline of alphabet village and the subline",
  "the Line Lane pityful question ran over her cheek",
];

// selecting required elements
let timer_text = document.querySelector(".curr_time");
let cpm_text = document.querySelector(".curr_cpm");
let wpm_text = document.querySelector(".curr_wpm");
let quote_text = document.querySelector(".quote");
let input_area = document.querySelector(".input_area");
let restart_btn = document.querySelector(".restart_btn");
let cpm_group = document.querySelector(".cpm");
let wpm_group = document.querySelector(".wpm");

let started = false;
let timeElapsed = 0;
let characterTyped = 0;
let current_quote = "";
let quoteNo = 0;
let timer = null;
let firstfocus = true;

let last_finger = null;
function send_msg(event, val) {
    console.log(`Send event ${event} to server`);
    wssend(`${event}?${val}`);
}

var ws = null;
if ("WebSocket" in window) {
    if (ws == null) {
        ws = new WebSocket(`ws://localhost:3000`);

        ws.onopen = function() { console.log('WebSocket openned.'); ws.send('Client connected') };

        ws.onmessage = function (evt) {
            console.log(`Message received.`);
            console.log(evt)
            evt.data.text().then((msg) => {
                console.log(msg)
                last_finger = { tag: msg, date: Date.now() }
            })
        };

        ws.onclose = function() { console.log('WebSocket closed.'); ws = null; };
    }
} else {
    console.log("WebSocket NOT supported by your Browser!");
}


function updateQuote() {
  quote_text.textContent = null;
  current_quote = quotes_array[quoteNo];

  // separate each character and make an element 
  // out of each of them to individually style them
  current_quote.split('').forEach(char => {
    const charSpan = document.createElement('span')
    charSpan.innerText = char
    quote_text.appendChild(charSpan)
  })

  // roll over to the first quote
  if (quoteNo < quotes_array.length - 1)
    quoteNo++;
  else
    quoteNo = 0;
}

function processCurrentText() {

  // get current input text and split it
  curr_input = input_area.value;
  curr_input_array = curr_input.split('');

  started = true;

  let finished = true;
  quoteSpanArray = quote_text.querySelectorAll('span');
  quoteSpanArray.forEach((char, index) => {
    let typedChar = curr_input_array[index]

    // characters not currently typed
    if (typedChar == null) {
      char.classList.remove('correct_char');
      char.classList.remove('incorrect_char');

      // correct characters
    } else if (typedChar === char.innerText) {
      char.classList.add('correct_char');
      char.classList.remove('incorrect_char');

      // incorrect characters
    } else {
      char.classList.add('incorrect_char');
      char.classList.remove('correct_char');

      // increment number of errors
      finished = false;
    }
  });

  if (curr_input.length == current_quote.length && finished) {
    clearInterval(timer);
    started = false;
  }
}

function updateTimer() {
  if(started){
    timeElapsed += 0.1;
    
    // calculate cpm and wpm
    curr_input = input_area.value;
    curr_input_array = curr_input.split(' ');
    let keys = curr_input.length;
    let words = curr_input_array.length;
    if (words == 1 && curr_input_array[0] == ''){
      words = 0;
    }
    cpm = (keys / timeElapsed)*60;
    wpm = (words / timeElapsed)*60;

    // update cpm and wpm text
    cpm_text.textContent = cpm.toFixed(1);
    wpm_text.textContent = wpm.toFixed(1);
    timer_text.textContent = timeElapsed.toFixed(1);
  }
}


function startGame() {
  if(firstfocus){
    updateQuote();
    firstfocus = false;
  }
  // clear old and start a new timer
  clearInterval(timer);
  timer = setInterval(updateTimer, 100);
}

function resetValues() {
  timeElapsed = 0;
  updateQuote();
  clearInterval(timer);
  timer = setInterval(updateTimer, 100);
  started = false;

  input_area.value = "";
  timer_text.textContent = '0.0';
  cpm_text.textContent = "0.0";
  wpm_text.textContent = "0.0";
}
