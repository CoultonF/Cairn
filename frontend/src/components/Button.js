import PropTypes from 'prop-types'
import { FaSearch } from 'react-icons/fa'

const Button = ({color, text }) => {
    return (
        <button className='btn'style={{backgroundColor: color}}>{text}</button>
    )
}

Button.defaultProps = {
    color: 'green'
}

Button.propTypes = {
    text: PropTypes.string,
    color: PropTypes.string,
}
export default Button
