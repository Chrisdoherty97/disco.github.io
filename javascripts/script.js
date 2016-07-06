  // Init PubNub

var p = PUBNUB.init({
  subscribe_key: 'sub-c-d5b343d8-3943-11e6-a169-02ee2ddab7fe',
  publish_key:   'pub-c-61695fa6-317d-42aa-8f73-1bead73191ad'
});

// Sending data

function disco() {
  p.publish({
    channel : 'channel', // This is the channel name you are subscribing in remote-led.py
    message : {led: 1}
  });
}

// Click event
document.querySelector('button').addEventListener('click', disco);


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
