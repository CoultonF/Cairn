import React, { useState, useEffect } from 'react';
import * as PropTypes from 'prop-types'
import Button from './Button'
import SearchBar from './SearchBar'

import Typography from '@material-ui/core/Typography';

const Header = ({title}) => {

    const [input, setInput] = useState('');
    
    const updateInput = async (input) => {
        setInput(input);
    }
    return (
        <header className='header'>
            <Typography variant="h3" gutterBottom>{title}</Typography>
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
