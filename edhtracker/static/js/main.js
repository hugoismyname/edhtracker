const userImage = document.getElementById('user-image')
const burger = document.getElementById('burger')
const responsiveMenu = document.getElementById('responsive-menu')
const subMenu = document.querySelector('.user-submenu')

if (userImage){
    userImage.addEventListener("mouseover", function(){
        subMenu.classList.toggle('visible') 
    })
    userImage.addEventListener("mouseout", function(){
        subMenu.classList.toggle('visible')
    })
    subMenu.addEventListener("mouseover", function(){
        subMenu.classList.toggle('visible') 
    })
    subMenu.addEventListener("mouseout", function(){
        subMenu.classList.toggle('visible')
    })
}
burger.addEventListener("click", function(){
    responsiveMenu.classList.toggle('visible-burger-menu')
})
