import * as PropTypes from 'prop-types'
import Button from './Button'

const Header = ({title}) => {
    return (
        <header className='header'>
            <h1>{title}</h1>
            <Button color='green' text='Search'></Button>
        </header>
    )
}

Header.defaultProps = {
    title: 'Carin'
}

Header.propType = {
    title: PropTypes.string.isRequried,
}

export default Header
