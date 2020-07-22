import lookUp from '../lookup/lookup'

export function apiCardsLookUp(callback,set){
    let endpoint = '/cards/'
    if (set){
        endpoint =`/cards/?set=${set}`
    }
    lookUp("GET",endpoint,callback)
}