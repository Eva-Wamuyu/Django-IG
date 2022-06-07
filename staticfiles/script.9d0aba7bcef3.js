let signupInputs = document.querySelectorAll("#signup input")
let loginInputs = document.querySelectorAll("#login input")
let addImage = document.querySelectorAll("#img input")
let comment = document.querySelectorAll("#comment input")
placeholders = ["","Email","Full Name", "Username","Password","Confirm Password"]
placeholders2 = ["","Username","Password"]
placeholders3 = ["","Image","Image Title","Caption"]
placeholders4 = ["","Add Comment"]
function styleSignUp (signupInputs,placeholders) {

  for(var i = 0; i < signupInputs.length; i++) {
    signupInputs[i].classList.add('shadow' ,'appearance-none', 'border' ,'rounded', 'w-full' ,'py-2', 'px-3' ,'text-gray-700', 'leading-tight' ,'focus:outline-none' ,'focus:shadow-outline','mb-3')
    signupInputs[i].placeholder = placeholders[i]
  }

}
styleSignUp(signupInputs,placeholders)
styleSignUp(loginInputs,placeholders2)
styleSignUp(addImage,placeholders3)
styleSignUp(comment,placeholders4)


let close = document.getElementById('closes')
let defaultModal = document.getElementById('defaultModal')
let closes = document.getElementById('close')
toggle = ()=> {
  defaultModal.classList.toggle('hidden');
  // defaultModal.classList.toggle('block');
  console.log('jj')
}

close.addEventListener('click',toggle)

closes.addEventListener('click',toggle)

function add(id){
  id = id+1

}