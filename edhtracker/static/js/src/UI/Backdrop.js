import React from 'react';
import Classes from './backdrop.module.css'

const Backdrop = (props) =>(
    props.show ? <div onClick={props.clicked} className={Classes.Backdrop}></div> : null
);

export default Backdrop;