import React from 'react';
import ReactDOM from 'react-dom';
import {UserCardList} from './index'

const e = React.createElement
const userCardsElement = document.getElementById("userCards")

function UserCardsApp(props){
    return(
        <UserCardList  user={props.user} />
    )
}
if(userCardsElement){
    ReactDOM.render(e(UserCardsApp,userCardsElement.dataset), userCardsElement)
  }
export default UserCardsApp;