import React, {useState,useEffect,useRef} from 'react'

import Classes from './controlBar.module.css'

function ControlBar(props){
    const wrapperRef = useRef(null);
    const [displayClass, setDisplayClass] = useState({"visual":Classes.selected,"list":null});
    const [isVisible, setIsVisible] = useState('none');
    const [sortParam, setSortParam] = useState('default')

    const changeDisplayHandler = (display) =>{
        display === "visual" ? setDisplayClass({"visual":Classes.selected,"list":null}) :
        setDisplayClass({"visual":"null","list":Classes.selected});
        props.switchDisplay(display)
    }
    const displayDropdown = () =>{
        setIsVisible('flex')
    }

    const changeOrderHandler = (event) =>{
        const orderValue = event.target.innerText
        setSortParam(orderValue)
        setIsVisible('none')
        event.stopPropagation()
        props.changeOrder(event.target.getAttribute('data-dbsort'))
    }
    useEffect(() => {
        document.addEventListener("click", handleClickOutside, false);
        return () => {
          document.removeEventListener("click", handleClickOutside, false);
        };
      }, []);
    
    const handleClickOutside = event => {
        if (wrapperRef.current && !wrapperRef.current.contains(event.target)) {
          setIsVisible('none');
        }
    };

    return(
        <div className={Classes.controlBarContainer}>
            <div className={Classes.currentSort} onClick={displayDropdown} ref={wrapperRef}>
                {sortParam}
                <i className={Classes.arrows}></i>
                <div className={Classes.dropdown} style={{display: isVisible}} >
                    <label data-dbsort="type_line" onClick={changeOrderHandler}>Set</label>
                    <label data-dbsort="date_added" onClick={changeOrderHandler}>Added</label>
                    <label data-dbsort="card_count" onClick={changeOrderHandler}>Quantity</label>
                    <label data-dbsort="name" onClick={changeOrderHandler}>Card Name</label>
                    <label data-dbsort="type_line" onClick={changeOrderHandler}>Type</label>
                </div>
            </div>

            <ul className={Classes.toggleCardDisplay}>
                <li className={displayClass["visual"]}><i onClick={() => changeDisplayHandler("visual")} className="fa fa-th-large" ></i></li>
                <li className={displayClass["list"]}><i onClick={() => changeDisplayHandler("list")} className="fa fa-th-list"></i></li>
            </ul>
        </div>
    )
}

export default ControlBar;