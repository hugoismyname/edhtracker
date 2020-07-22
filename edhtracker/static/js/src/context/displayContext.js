import React from 'react';

const displayContext = React.createContext({
    display: "visual",
    changeDisplay: () =>{}
});

export default displayContext;