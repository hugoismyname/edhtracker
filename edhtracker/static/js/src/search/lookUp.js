import lookUp from '../lookup/lookup'

export function searchCards(callback,nextUrl,searchParam){
    let endpoint = '/search/'
    if (searchParam){
        endpoint =`/search/?searchParam=${searchParam}`
    }
    if (nextUrl !== null && nextUrl !== undefined) {
        endpoint = nextUrl.replace("http://localhost:8000/api", "")
    }
    
    lookUp('GET',endpoint,callback)
}