/*Sidebar Js*/
let btn = document.querySelector("#menu");
let sidebar = document.querySelector(".sidebar");
let home = document.querySelector(".home_section");

btn.onclick = function(){
    sidebar.classList.toggle("active");    
    home.classList.toggle("active");
}

let up = document.querySelector(".goUp");

up.onclick = function(){
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}

let heart = document.querySelector(".fa-heart-o");

heart.onclick = function() {
    
}