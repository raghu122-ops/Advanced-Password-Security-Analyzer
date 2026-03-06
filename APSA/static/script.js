function checkPassword(){

let password=document.getElementById("password").value;

fetch("/check",{

method:"POST",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify({password:password})

})

.then(res=>res.json())

.then(data=>{

document.getElementById("strength").innerText=data.strength;

document.getElementById("entropy").innerText=data.entropy;

document.getElementById("time").innerText=data.time;

let breach=document.getElementById("breach");

breach.innerText=data.breach;

if(data.breach.includes("WARNING")){

breach.className="warning";

}

else{

breach.className="safe";

}

let list=document.getElementById("suggestions");

list.innerHTML="";

data.suggestions.forEach(function(s){

let li=document.createElement("li");

li.innerText=s;

list.appendChild(li);

});

});

}