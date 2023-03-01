toggleBtn=document.getElementsByClassName("menu-svg")[0]
search=document.getElementsByClassName('search-box')[0]
navList=document.getElementsByClassName("navlist")[0]
searchText=document.getElementsByClassName("searchtext")[0]
searchButton=document.getElementsByClassName('search-button')[0]
searchCross=document.getElementsByClassName("search-cross")[0]
toggleBtn.addEventListener('click', ()=> {
    navList.classList.toggle('active');
    search.classList.toggle('active');
    searchText.classList.add('searchtext-effect');
    searchCross.classList.add('searchcross-active');



    
})
// searchButton.addEventListener('click',()=>{ 
//     if(searchText.classList.contains('searchtext-effect') ){
//     searchText.classList.remove('searchtext-effect');
//     navList.classList.remove('unactive');
//     }
//     else {
//     searchText.classList.add('searchtext-effect');
//     navList.classList.add('unactive');
//     searchCross.classList.add('searchcross-active')


// }
// })
searchCross.addEventListener('click',()=>{
    searchText.classList.remove('searchtext-effect');
    navList.classList.remove('unactive');
    searchCross.classList.remove('searchcross-active');

})

searchButton.addEventListener('click',()=>{ 
    searchText.classList.add('searchtext-effect');
    navList.classList.add('unactive');
    searchCross.classList.add('searchcross-active');
})


