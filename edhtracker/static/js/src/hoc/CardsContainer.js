import React from 'react'

import Classes from './cardsContainer.module.css'

function CardsContainer(props){
    return(
        <div className={Classes.CardsContainer}>{props.children}</div>
    )
} 

export default CardsContainer;