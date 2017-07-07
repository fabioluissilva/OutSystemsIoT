//var connectionString = 'HostName=new-iot-device.azure-devices.net;DeviceId=new-iot-device;SharedAccessKey=mUalGCriwCO7elvTmfbPDdXmDQdn+tjY9u4Pfko/ScE=';
var connectionString = 'HostName=OS-Hackathon-IoT-Hub.azure-devices.net;DeviceId=new-iot-device;SharedAccessKey=bPTJG3IjlLrlu0z2Wvh2UKOOlSmODRBZ5UiPHvTcVsI=';

// use factory function from AMQP-specific package
var clientFromConnectionString = require('azure-iot-device-amqp').clientFromConnectionString;

// AMQP-specific factory function returns Client object from core package
var client = clientFromConnectionString(connectionString);

// use Message object from core package
var Message = require('azure-iot-device').Message;

var connectCallback = function (err) {
  if (err) {
    console.error('Could not connect: ' + err);
  } else {
    console.log('Client connected');
       setInterval(function() { 
       fs = require ('fs');
    fs.readFile('/sys/bus/w1/devices/10-0008020aa44c/w1_slave','utf-8',function(err,data) {
       if(err) {
          return console.log(err);
       }
       // console.log(data);
       var lines= data.trim().split('\n');
       var lastline= lines.slice(-1)[0];
       var re=/(.*)t\=(.*)/g;
       var newdata= '{"messageId":0,"deviceId":"RaspberryPiPhysical","temperature":'+Number(lastline.replace(re,'$2'))/1000+',"humidity":0}';
       console.log(newdata);
       var msg=new Message(newdata);
       client.sendEvent(msg, function (err) {
          if (err) {
            console.log(err.toString());
          } else {
            console.log('Message sent');
          }
  	 });});
       },10000);
   }
};

client.open(connectCallback);
