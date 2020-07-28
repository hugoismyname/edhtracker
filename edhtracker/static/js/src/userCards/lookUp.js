import lookUp from '../lookup/lookup'

export function apiAddCard(callback,data) {
    lookUp("POST", "/add_card/",callback,data)
}
export function apiUserCardsList(user,callback,nextUrl) {
    let endpoint = '/user_cards/'
    if (user){
      endpoint = `/user_cards/?user_id=${user}`
    }
    if (nextUrl !== null && nextUrl !== undefined) {
    endpoint = nextUrl.replace("http://localhost:8000/api", "")
    }
    lookUp("GET", endpoint,callback)
  }
export function apiUserCardsDelete(callback,pk){
  lookUp("GET", `/user_cards/${pk}/delete/`,callback)
}
export function apiUserCardsUpdate(callback,pk,data){
  lookUp("POST", `/user_cards/${pk}/update/`,callback,data)
}