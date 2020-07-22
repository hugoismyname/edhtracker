const userImage = document.getElementById('user-image')
const subMenu = document.querySelector('.user-submenu')

userImage.addEventListener("mouseover", function(){
    subMenu.style.display = 'flex'
})
userImage.addEventListener("mouseout", function(){
    subMenu.style.display = 'none'
})
subMenu.addEventListener("mouseover", function(){
    subMenu.style.display = 'flex'
})
subMenu.addEventListener("mouseout", function(){
    subMenu.style.display = 'none'
})
