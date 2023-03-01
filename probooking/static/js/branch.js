let zoom = 8;
let first = true;

// let leftBranch = document.getElementsByClassName("l-br")[0];
// let branch = document.getElementsByClassName("branch")[0];
// let rightBranch = document.getElementsByClassName("r-br")[0];
mapdiv = document.getElementById("map");
function responsive() {
  width = Math.max(
    document.documentElement.clientWidth,
    window.innerWidth || 0,
  );
  //   height = Math.max(
  //     document.documentElement.clientHeight,
  //     window.innerHeight || 0,
  //   );
  mapdiv.style.width = "1 00%";
  if (width > 1000) {
    rightBranch.style.width =
      branch.offsetWidth - leftBranch.offsetWidth + "px";
  } else {
    // zoom = 6;
    // if(first==true){
    zoom = 9;
    rightBranch.style.width = "100%";
    // first=false
    // console.log("first");

    // }
  }
}
// responsive();
// setInterval(responsive, 100);

// mapdiv.style.height = "100%";
// mapdiv.style.width = "100%";

var map = L.map("map",{dragging: false}).setView([27.7172, 85.324], zoom);
L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  attribution:
    '&copy; <a href="https://www.openstreetmap.org/copyright">hashtag</a>',
}).addTo(map);
map.scrollWheelZoom.disable();


// map.invalidateSize();
function markeradd() {
  let markers = document.getElementsByClassName("map");
  for (let i = 0; i < markers.length; i++) {
    let longtat = markers[i].getAttribute("datalong").split("-");
    longtitude = longtat[0];
    latitude = longtat[1];
    console.log(parseFloat(longtitude),"asd", parseFloat(latitude));
    L.marker([longtitude, latitude], { title: "My marker" }).addTo(map);

    // console.log(markers[i].getAttribute("datalat"));
  }
}
markeradd();

function zoomenable(){
    const doc=document.getElementsByClassName("map-transparent")[0];
    doc.style.display="none";
    map.dragging.enable();
    // map.scrollWheelZoom.enable();
}

// markeradd();