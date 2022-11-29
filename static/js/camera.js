feather.replace();

const controls = document.querySelector('.controls');
const cameraOptions = document.querySelector('.video-options>select');
const video = document.querySelector('video');
const canvas = document.querySelector('canvas');
const screenshotImage = document.querySelector('img');
// const screenshot = controls.querySelector('#screenshot');

let streamStarted = false;
const constraints = {
  video: {
    width: {
      min: 1280,
      ideal: 1920,
      max: 2560,
    },
    height: {
      min: 720,
      ideal: 1080,
      max: 1440
    },
    facingMode: {
      exact: 'environment'
    }
  }
};
const startStream = async (constraints) => {
  const stream = await navigator.mediaDevices.getUserMedia(constraints);
  handleStream(stream);
};

const handleStream = (stream) => {
  video.srcObject = stream;
  streamStarted = true;
};

var c = document.getElementById("myCanvas");
var ctx = c.getContext("2d");
// Red rectangle
c.width =120;
c.height =120;
ctx.beginPath();
ctx.lineWidth = "6";
ctx.strokeStyle = "white";
ctx.rect(0, 0, 120, 120);  
ctx.stroke();
// const doScreenshot = () => 
function printdmc() {
    console.log("acb")
    const xhttp1 = new XMLHttpRequest();
    var casting = document.getElementById("Castingcode").value;
    var ProductName = document.getElementById("ProductName").value;
    xhttp1.onload = function () {
        if (this.responseText.length != 29) {
            console.log(this.responseText.length);
            console.log(this.responseText);
            var popup = document.getElementById("myPopup");
            popup.style.visibility = "visible";
            popup.innerHTML = this.responseText;
            document.getElementById('QQ').value =this.responseText;
        } else {
            document.getElementById('QQ').value =this.responseText;
            window.location.href = "my.bluetoothprint.scheme://http://54.65.195.213/json/"+this.responseText;       
        }
    };
    xhttp1.open("POST", "/createdmc");
    xhttp1.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp1.send("casting=" + casting + "&product=" + ProductName);
}

document.getElementById("Castingcode").addEventListener("keypress", function (event) {
  // If the user presses the "Enter" key on the keyboard
  if (event.key === "Enter") {
    event.preventDefault();
    printdmc();
  }
});
function checkkq(){

  // setInterval(check,1000)
  if ((document.getElementById("ketqua").value !="Trung") | (document.getElementById("ketqua").value !="Can't Detect Datamatrix Code") )
  {
   // document.getElementById("ketqua").innerHTML=""  
  }
    canvas.width = 400;
    canvas.height = 400;
    canvas.getContext('2d').drawImage(video,-340,-760);
  // screenshotImage.value = canvas.toDataURL('image/webp');
    console.log(canvas.toDataURL('image/png').split(';base64,')[1]);
    const xhttp3 = new XMLHttpRequest();
    xhttp3.onload = function () {
      
      if (this.responseText!= "Trung")
      {
        document.getElementById("ketqua").innerHTML=this.responseText;
      }
      
        document.getElementById("ketqua").value=this.responseText;
        if ((this.responseText!="Trung") & (this.responseText!="Can't Detect Datamatrix Code") & (this.responseText!="")){
          //document.getElementById("ketqua").innerHTML="" 
          //await sleep(2000)
          //base64='UklGRr4DAABXRUJQVlA4WAoAAAAIAAAA/wEA/wEAVlA4IN4CAACwWQCdASoAAgACPpFIoU0lpCMiIAgAsBIJaW7hdrEbVLwrzmp2yvCfLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUTsAA/v+2MAAAAEVYSUa6AAAARXhpZgAASUkqAAgAAAAGABIBAwABAAAAAQAAABoBBQABAAAAVgAAABsBBQABAAAAXgAAACgBAwABAAAAAgAAABMCAwABAAAAAQAAAGmHBAABAAAAZgAAAAAAAAC11AEA6AMAALXUAQDoAwAABgAAkAcABAAAADAyMTABkQcABAAAAAECAwAAoAcABAAAADAxMDABoAMAAQAAAP//AAACoAQAAQAAAAACAAADoAQAAQAAAAACAAAAAAAA'
          var a = window.open("","","");
          a.document.write(this.responseText);
          a.document.close();
          setTimeout(function() {
              a.print(); 
            }, 3500);
          }
      if (this.responseText != "Can't Detect Datamatrix Code"){     
	  //const xhttp2 = new XMLHttpRequest();
        //xhttp2.open("GET", "https://54.65.195.213/save/"+this.responseText);
        //xhttp2.send();
        //window.location.href = "my.bluetoothprint.scheme://http://54.65.195.213/json/"+this.responseText;
	    
    }
  };
  base64='UklGRr4DAABXRUJQVlA4WAoAAAAIAAAA/wEA/wEAVlA4IN4CAACwWQCdASoAAgACPpFIoU0lpCMiIAgAsBIJaW7hdrEbVLwrzmp2yvCfLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUT5ciifLkUTsAA/v+2MAAAAEVYSUa6AAAARXhpZgAASUkqAAgAAAAGABIBAwABAAAAAQAAABoBBQABAAAAVgAAABsBBQABAAAAXgAAACgBAwABAAAAAgAAABMCAwABAAAAAQAAAGmHBAABAAAAZgAAAAAAAAC11AEA6AMAALXUAQDoAwAABgAAkAcABAAAADAyMTABkQcABAAAAAECAwAAoAcABAAAADAxMDABoAMAAQAAAP//AAACoAQAAQAAAAACAAADoAQAAQAAAAACAAAAAAAA'
  xhttp3.open("POST", "/decodedmc");
  xhttp3.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp3.send("anh=" + canvas.toDataURL('image/webp').split(';base64,')[1]);
  xhttp3.send("anh=" + base64);
};

startStream(constraints);
setInterval(checkkq,1000);
// screenshot.onclick = doScreenshot;
//var a = new Window()

