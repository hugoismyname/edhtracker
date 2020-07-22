import { lookUp } from '../lookup/lookup'

export function lookUpDeckRecs(callBack,username){
    lookUp('GET',`/decks_rec/?username=${username}`,callBack,)
}