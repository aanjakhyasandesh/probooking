const sec=document.querySelectorAll(".sec1");
// const call1=function(entries =>{}{
//     console.log(entries[0]);
//     sec.className += " sec1-active";
// }


const call = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      // Add 'active' class if observation target is inside viewport
    //   if (entry.intersectionRatio > 0) {
        console.log(entry)
        entry.target.classList.add('sec1-active');
    //   }
    //   // Remove 'active' class otherwise
    //   else {
    //     entry.target.classList.remove('active');
    //   }
    })
  })
// const observer=new IntersectionObserver(call);
// for (let i=0;i<sec.length;i++){
    sec.forEach((el) => {
        call.observe(el);
      })
// call.observe(sec);
