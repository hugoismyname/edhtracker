import { lookUp } from '../lookup/lookup'

export function lookUpcardsInDeck(callBack,cardId,username){
    let endpoint = `/card_detail/?pk=${cardId}`
    if (username){
        endpoint = `/card_detail/?pk=${cardId}&username=${username}`
    }
    lookUp('GET',endpoint,callBack,)
}