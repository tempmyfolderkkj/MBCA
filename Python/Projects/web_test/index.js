//https://2017mrhi.github.io/web-test/

// 버튼 클릭하면 반응하는 함수이름 show를 만들기
function show(){
    alert("로그인 버튼 클릭")

}

function changeImage(){
    var img = document.getElementById("kk")

    if(img.getAttribute("src") == './image/im2.jpg'){
        img.src = './image/IMG_20251202.png'

    }else{
        img.src = "./image/im2.jpg"

    }
    
    

}

//'./image/im2.jpg'