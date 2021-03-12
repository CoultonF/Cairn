import React, { useState, useEffect } from 'react';
import * as PropTypes from 'prop-types'
import Button from './Button'
import SearchBar from './SearchBar'

const Header = ({title}) => {

    const [input, setInput] = useState('');
    
    const updateInput = async (input) => {
        setInput(input);
    }
    return (
        <header className='header'>
            <h1>{title}</h1>
            <SearchBar input={input} onChange={updateInput}></SearchBar>
        </header>
    )
}

Header.defaultProps = {
    title: 'Cairn'
}

Header.propType = {
    title: PropTypes.string.isRequried,
}

export default Header
