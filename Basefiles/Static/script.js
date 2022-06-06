let signupInputs = document.querySelectorAll("#signup input")
let loginInputs = document.querySelectorAll("#login input")

placeholders = ["","Email","Full Name", "Username",  "Password"]
placeholders2 = ["","Email","Password"]
function styleSignUp (signupInputs,placeholders) {

  for(var i = 0; i < signupInputs.length; i++) {
    signupInputs[i].classList.add('shadow' ,'appearance-none', 'border' ,'rounded', 'w-full' ,'py-2', 'px-3' ,'text-gray-700', 'leading-tight' ,'focus:outline-none' ,'focus:shadow-outline','mb-3')
    signupInputs[i].placeholder = placeholders[i]
  }

  
}
styleSignUp(signupInputs,placeholders)
styleSignUp(loginInputs,placeholders2)
